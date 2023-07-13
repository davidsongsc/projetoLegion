import socketio
import eventlet

sio = socketio.Server(cors_allowed_origins=['https://main--marvelous-gaufre-f1183b.netlify.app',
                                            'https://main--idyllic-gumption-1a6de8.netlify.app',
                                            'http://192.168.0.50:3000',
                                            'http://192.168.0.50:3001',
                                            'http://192.168.0.50:30012'])

app = socketio.WSGIApp(sio)