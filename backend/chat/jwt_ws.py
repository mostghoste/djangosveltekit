from urllib.parse import parse_qs
from channels.db import database_sync_to_async
from channels.middleware import BaseMiddleware
from django.contrib.auth.models import AnonymousUser
from rest_framework_simplejwt.authentication import JWTAuthentication

class JWTAuthMiddleware(BaseMiddleware):
    async def __call__(self, scope, receive, send):
        query = parse_qs(scope.get("query_string", b"").decode())
        token = (query.get("token") or [None])[0]
        scope["user"] = await self.get_user(token)
        return await super().__call__(scope, receive, send)

    @database_sync_to_async
    def get_user(self, raw_token):
        if not raw_token:
            return AnonymousUser()
        try:
            validator = JWTAuthentication()
            validated = validator.get_validated_token(raw_token)
            return validator.get_user(validated)
        except Exception:
            return AnonymousUser()
