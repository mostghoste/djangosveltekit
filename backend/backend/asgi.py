import os, django
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from chat.routing import websocket_urlpatterns
from chat.jwt_ws import JWTAuthMiddleware  # custom

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": JWTAuthMiddleware(  # attaches scope["user"] if ?token=...
        URLRouter(websocket_urlpatterns)
    ),
})
