from flask import Flask, request, jsonify
import sqlite3
from flask_cors import CORS
from eventlet import wsgi, websocket
import eventlet
from flask_socketio import SocketIO
import socketio
from datetime import datetime, timedelta
import pytz  # Pacote para gerenciar fusos horários

PORTA = 8010 # Porta servidor post
HOST_PRODUCAO = ['https://main--marvelous-gaufre-f1183b.netlify.app',
                                            'https://main--idyllic-gumption-1a6de8.netlify.app',
                                            'http://192.168.1.50:3000',
                                            'http://192.168.1.50:3001',
                                            'http://192.168.1.50:30012']

sio = socketio.Server(cors_allowed_origins=HOST_PRODUCAO)
app = socketio.WSGIApp(sio)
socketio = SocketIO(app, cors_allowed_origins="http://192.168.1.50:3000")


connected_clients = []  # Lista para armazenar as conexões WebSocket

# Função para enviar todos os posts para os clientes conectados
def emit_recent_posts_within_time(posts_list, sid, time_window_minutes=3):
    try:
        conn = sqlite3.connect('social_network.db')
        cursor = conn.cursor()

        # Calcula a data/hora há 3 minutos atrás
        three_minutes_ago = datetime.now() - timedelta(minutes=time_window_minutes)

        # Seleciona os posts criados nos últimos 3 minutos
        cursor.execute('SELECT * FROM posts WHERE timestamp >= ? ORDER BY timestamp DESC', (three_minutes_ago,))
        recent_posts = cursor.fetchall()

        conn.close()

        for post in recent_posts:
            post_details = {
                'id': post[0],
                'user': post[1],
                'content': post[2],
                'timestamp': post[3],
                'key_user_reference': post[4]
            }
            posts_list.append(post_details)

        sio.emit('recentes_posts', {
                 'conteudo': jsonify(posts_list)}, room=sid)
    except Exception as e:
        print('Error fetching recent posts:', e)
    
@sio.on('criar_post')
def create_post(sid, data):
    print('===='*25)
    conn = sqlite3.connect('social_network.db')
    cursor = conn.cursor()

    timestamp = datetime.now(pytz.timezone('America/Sao_Paulo'))  # Obtém a data/hora atual no fuso horário do Brasil (UTC-3)

    cursor.execute('''
        INSERT INTO posts (user, content, timestamp, key_user_reference)
        VALUES (?, ?, ?, ?)
    ''', (data['user'], data['content'], timestamp, data['user']))

    # Atualizar a contagem de postagens do usuário
    cursor.execute('UPDATE users SET posts = posts + 1 WHERE id = ?', (data['user'],))

    conn.commit()
    conn.close()
    
    sio.emit('status', {"status": 'Verdadeiro', "post": data['content']}, room=sid)

@sio.on('deletarPost')
def delete_post(sid ,data):
    print('===='*4 +'DELETAR POST' + '===='*4)
    
    try:
        conn = sqlite3.connect('social_network.db')
        cursor = conn.cursor()

        post_id = data['postId']

        # Excluir o post com o ID fornecido
        cursor.execute('DELETE FROM posts WHERE id = ?', (post_id,))

        # Você também pode implementar outras lógicas relacionadas à exclusão aqui, como atualizar contadores, etc.

        conn.commit()
        conn.close()

        # Emitir evento para confirmar a exclusão do post
        sio.emit('postDeletado', {'postId': post_id})

    except Exception as e:
        print('Error deleting post:', e)

@sio.on('post_todos')
def get_all_posts(sid):
    conn = sqlite3.connect('./social_network.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM posts')
    all_posts = cursor.fetchall()

    conn.close()

    posts_list = []
    for post in all_posts:
        post_details = {
            'id': post[0],
            'user': post[1],
            'content': post[2],
            'timestamp': post[3],
            'key_user_reference': post[4]
        }
        posts_list.append(post_details)

    sio.emit('todos', posts_list, room=sid)



    
# Rota para criar um novo usuário
@sio.on('criar')
def create_user():
    data = request.json
    if data:
        try:
            conn = sqlite3.connect('./social_network.db')
            cursor = conn.cursor()

            cursor.execute('''
                INSERT INTO users (username, password, full_name, idempresa, idempregado, posts, followers, following)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (data['username'], data['password'], data['full_name'], data['idempresa'], data['idempregado'], 0, 0, 0))

            conn.commit()
            conn.close()
            return jsonify({'message': 'User created successfully'}), 201
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    else:
        return jsonify({'error': 'Invalid data'}), 400

# Rota para obter detalhes de um usuário pelo ID
@sio.on('selecionar_usuario')
def get_user(user_id):
    try:
        conn = sqlite3.connect('social_network.db')
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM users WHERE id = ?', (user_id,))
        user = cursor.fetchone()

        conn.close()

        if user:
            user_details = {
                'id': user[0],
                'username': user[1],
                'full_name': user[3],
                'idempresa': user[4],
                'idempregado': user[5],
                'posts': user[6],
                'followers': user[7],
                'following': user[8]
            }
            return jsonify(user_details)
        else:
            return jsonify({'message': 'User not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Rota para obter posts de um usuário
@sio.on('selecionar_post_usuario')
def get_user_posts(user_id):
    try:
        conn = sqlite3.connect('social_network.db')
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM posts WHERE user = ?', (user_id,))
        user_posts = cursor.fetchall()

        conn.close()

        posts_list = []
        for post in user_posts:
            post_details = {
                'id': post[0],
                'user': post[1],
                'content': post[2],
                'timestamp': post[3],
                'key_user_reference': post[4]
            }
            posts_list.append(post_details)

        return jsonify(posts_list)
    except Exception as e:
        return jsonify({'error': str(e)}), 500


def update_data():
        while True:
            # atualiza os dados das comandas e mesas
            get_all_posts(None)

            # aguarda 5 segundos antes de atualizar no  vamente

            eventlet.sleep(1)

    # inicia a atualização dos dados em um novo thread
eventlet.spawn(update_data)

if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('', 8010)), app)
