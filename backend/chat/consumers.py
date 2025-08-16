import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    group_name = "public_chat"

    async def connect(self):
        # only signed-in users
        if not (getattr(self.scope, "user", None) and self.scope["user"].is_authenticated):
            await self.close(code=4401)  # unauthorized
            return
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()
        await self.send_json({"type":"system","message":f"Welcome {self.scope['user'].username}!"})

    async def disconnect(self, code):
        await self.channel_layer.group_discard(self.group_name, self.channel_name)

    async def receive(self, text_data=None, bytes_data=None):
        if not text_data:
            return
        data = json.loads(text_data)
        msg = (data.get("message") or "").strip()
        if not msg:
            return
        await self.channel_layer.group_send(
            self.group_name,
            {
                "type": "chat.message",
                "payload": {
                    "user": self.scope["user"].username,
                    "message": msg
                }
            }
        )

    async def chat_message(self, event):
        await self.send(text_data=json.dumps({"type":"chat","...":event["payload"]}))
