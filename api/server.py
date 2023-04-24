import socketio
import eventlet
from eventlet import wsgi

sio = socketio.Server(async_mode='threading')
app = socketio.WSGIApp(sio)

@sio.on('connect')
def connect(sid, environ):
    print('connect', sid)

@sio.on('disconnect')
def disconnect(sid):
    print('disconnect', sid)

if __name__ == '__main__':
    wsgi.server(eventlet.listen(('192.168.0.50', 8000)), app)
