import socketio
import eventlet
from eventlet import wsgi
# Cria uma instância do servidor socket.IO
sio = socketio.Server()

# Define a função para lidar com a conexão de um novo cliente
@sio.on('connect')
def connect(sid, environ):
    print('Novo cliente conectado:', sid)

# Define a função para lidar com a desconexão de um cliente
@sio.on('disconnect')
def disconnect(sid):
    print('Cliente desconectado:', sid)

# Inicia o servidor Socket.IO
if __name__ == '__main__':
    app = socketio.WSGIApp(sio)
    wsgi.server(eventlet.listen(('', 8000)), app)
