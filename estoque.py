# API IMPRESSORA

import eventlet
import socketio

sio = socketio.Server(cors_allowed_origins='http://192.168.0.50:3000')
app = socketio.WSGIApp(sio)

@sio.on('connect')
def connect(sid, environ):
    print('Conexão estabelecida: ', sid)

@sio.on('disconnect')
def disconnect(sid):
    print('Desconectado: ', sid)

@sio.on('imprimir')
def imprimir(sid, data):
    print('Imprimir: ', data)
    # Aqui você pode adicionar a lógica para lidar com a impressão


if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('', 8200)), app)
