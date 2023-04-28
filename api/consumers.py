import asyncio
import json
from channels.generic.websocket import AsyncWebsocketConsumer

class MesaConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.mesa_id = self.scope['url_route']['kwargs']['mesa_id']
        await self.channel_layer.group_add(
            self.mesa_id,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.mesa_id,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        await self.channel_layer.group_send(
            self.mesa_id,
            {
                'type': 'mesa_message',
                'message': data['message']
            }
        )

    async def mesa_message(self, event):
        message = event['message']
        await self.send(text_data=json.dumps({
            'message': message
        }))
