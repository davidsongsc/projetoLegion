from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'mesa/$', consumers.WebSocket.as_asgi()),
]
