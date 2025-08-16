from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .serializers import RegisterSerializer

class RegisterView(CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def current_user(request):
    u = request.user
    return Response({"id": u.id, "username": u.username, "email": u.email})
