import eventlet
import socketio
import sqlite3

sio = socketio.Server(cors_allowed_origins=['http://192.168.0.50:3000'])
app = socketio.WSGIApp(sio)

conn = sqlite3.connect('demas.sqlite3')
cursor = conn.cursor()

@sio.on('dados_usuario')
def dados_usuario(sid, data):
    # Aqui você pode acessar os dados enviados pelo cliente na variável `data`
    # e fazer o que desejar com eles (por exemplo, autenticar o usuário)

    # Exemplo de autenticação com dados de usuário armazenados no banco de dados:
    cursor.execute("SELECT Colaborador.*, auth_user.username FROM Colaborador JOIN auth_user ON Colaborador.usuario = auth_user.id WHERE Colaborador.senha = ?", (data['senha'],))
    colaborador = cursor.fetchone()

    if colaborador:
        sio.emit('autenticacao', {'success': True, 'nivel': colaborador[1], 'usuario': colaborador[5], 'auth': colaborador[3], }, room=sid)
    else:
        sio.emit('autenticacao', {'success': False}, room=sid)


# define evento para obter dados das comandas
@sio.on('get_comandas')
def get_comandas(sid):
    # executa query no banco de dados para obter as comandas
    cursor.execute("SELECT * FROM Comanda")
    comandas = cursor.fetchall()
    comandas_dict = []
    # adiciona os itens em cada comanda
    for comanda in comandas:
        cursor.execute("SELECT * FROM Itens WHERE id = ?", (comanda[0],))
        itens = cursor.fetchall()
        comanda_dict = {
            "chave": comanda[1],
            "datahora": comanda[4],
            "id": comanda[0],
            "itens": [{"id": i[0], "nome": i[1], "preco": i[2]} for i in itens],
            "mesa": comanda[2],
            "pagamento": comanda[6],
            "status": comanda[3],
            "atendente": comanda[7]
        }
        comandas_dict.append(comanda_dict)

    # envia as comandas com os itens para o cliente
    sio.emit('comandas', comandas_dict, room=sid)

# define evento para obter dados das mesas
@sio.on('get_mesas')
def get_mesas(sid):
    # executa query no banco de dados para obter as mesas
    cursor.execute("SELECT mesa, status FROM comanda")
    mesas = cursor.fetchall()

    # converte resultado em dicionário e envia para o cliente
    mesas_dict = {}
    for mesa, status in mesas:
        mesas_dict[str(mesa)] = {"ocupada": True if status != 0 else False}

    # adiciona as mesas que estão vazias
    for i in range(1, 67):
        if str(i) not in mesas_dict:
            mesas_dict[str(i)] = {"ocupada": False}

    sio.emit('mesas', mesas_dict, room=sid)

# função para atualizar os dados em intervalos regulares
def update_data():
    while True:
        # atualiza os dados das comandas e mesas
        get_comandas(None)
        get_mesas(None)
        
        # aguarda 5 segundos antes de atualizar novamente
        eventlet.sleep(5)

# inicia a atualização dos dados em um novo thread
eventlet.spawn(update_data)

if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('', 8000)), app)