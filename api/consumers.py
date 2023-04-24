import asyncio
import json
from django_socketio import sockets

class ChatConsumer(sockets.AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Entrar no grupo da sala
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Sair do grupo da sala
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receber mensagem do WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Enviar mensagem para o grupo da sala
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    # Receber mensagem do grupo da sala
    async def chat_message(self, event):
        message = event['message']

        # Enviar mensagem para o WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))
