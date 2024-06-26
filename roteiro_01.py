from flask import Flask, request, jsonify, render_template
from flask_socketio import SocketIO, emit
from flask_limiter import Limiter
import sqlite3


PORTA = 8011 # Porta servidor roteiro
HOST_PRODUCAO = ['https://main--marvelous-gaufre-f1183b.netlify.app',
                                            'https://main--idyllic-gumption-1a6de8.netlify.app',
                                            'http://192.168.1.50:3000',
                                            'http://192.168.1.50:3001',
                                            'http://192.168.1.50:30012']
app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="http://192.168.1.50:3000")
limiter = Limiter(app, default_limits=["1 per second"])  # Configuração do Limiter

# Função para criar a tabela no banco de dados
def create_table():
    conn = sqlite3.connect('console_db.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS console_data (
            id INTEGER PRIMARY KEY,
            codigo TEXT,
            datahora DATETIME DEFAULT CURRENT_TIMESTAMP,
            nivel TEXT
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('listar_roteiros')
def on_connect():
    emit('dados_atualizados', carregar_dados(), broadcast=False)

# Rota para inserir dados no banco de dados
@app.route('/api/inserir', methods=['POST'])
def inserir_dados():
    codigo = request.json.get('codigo')
    nivel = request.json.get('nivel')
    
    if codigo is None or nivel is None:
        return jsonify({'message': 'Dados inválidos'}), 400
    
    conn = sqlite3.connect('console_db.sqlite3')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO console_data (codigo, nivel) VALUES (?, ?)', (codigo, nivel))
    conn.commit()
    conn.close()

    # Enviar os dados atualizados para todos os clientes conectados via WebSocket
    socketio.emit('dados_atualizados', {'codigo': carregar_dados()}, broadcast=True)

    return jsonify({'message': 'Dados inseridos com sucesso'}), 201

@socketio.on('atualizar_roteiro')
@limiter.limit("1 per second")
def atualizar_roteiro_socket(data):
    id = data.get('id')
    codigo = data.get('codigo')
    print(data)
    if id is None or codigo is None:
        return jsonify({'message': 'Dados inválidos'}), 400
    
    atualizar_dados(id, codigo)  # Chamando a função que atualiza os dados no banco

    # Emitindo o evento 'dados_atualizados' para todos os clientes, incluindo o próprio servidor
    socketio.emit('dados_atualizados', carregar_dados())  # Remova o argumento 'broadcast'

    return jsonify({'message': 'Dados atualizados com sucesso'}), 200

@app.route('/api/atualizar/<int:id>/<string:codigo>', methods=['PUT'])
def atualizar_dados(id, codigo):
    if codigo is None:
        return jsonify({'message': 'Dados inválidos'}), 400
    
    conn = sqlite3.connect('console_db.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE console_data SET codigo = ? WHERE id = ?', (codigo, id))
    conn.commit()
    conn.close()
    
    socketio.emit('dados_atualizados', carregar_dados())
    
    return jsonify({'message': 'Dados atualizados com sucesso'}), 200

@app.route('/api/pesquisar-roteiros', methods=['POST'])
def pesquisar_roteiros():
    # Recebe o termo de pesquisa do corpo da requisição POST
    data = request.get_json()
    termo_pesquisa = data.get('termo')

    # Realiza a consulta no banco de dados
    conn = sqlite3.connect('console_db.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id FROM console_data WHERE titulo LIKE ?', ('%' + termo_pesquisa + '%',))
    resultados = cursor.fetchall()
    conn.close()

    # Retorna os IDs dos roteiros encontrados
    ids_roteiros = [resultado[0] for resultado in resultados]
    return jsonify({'ids_roteiros': ids_roteiros})

@app.route('/api/roteiros', methods=['GET'])
def get_roteiros():
    # Lógica para obter a lista de roteiros do banco de dados
    roteiros = carregar_dados()
    return jsonify({'roteiros': roteiros})

@socketio.on('dados_codigos')
@limiter.limit("1 per second")
def handle_dados_codigos():
    roteiros = carregar_dados()
    emit('roteiros_carregados', {'roteiros': roteiros}, broadcast=True)


def carregar_dados():
    conn = sqlite3.connect('console_db.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM console_data')
    data = cursor.fetchall()
    conn.close()

    dados_formatados = []
    for row in data:
        id, codigo, datahora, nivel, projeto = row
        dados_formatados.append({
            'id': id,
            'codigo': codigo,
            'datahora': datahora,
            'nivel': nivel,
            'projeto': projeto
        })

    return dados_formatados


if __name__ == '__main__':
    create_table()
    socketio.run(app, debug=True, host='0.0.0.0', port=PORTA)
