from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenBlacklistView
from users.views import RegisterView, current_user

urlpatterns = [
    path('admin/', admin.site.urls),

    # auth
    path('api/register/', RegisterView.as_view(), name='auth_register'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/logout/', TokenBlacklistView.as_view(), name='token_blacklist'),
    path('api/user/', current_user, name='current_user'),

    # simple health
    path('api/health/', lambda r: __import__('django.http').http.JsonResponse({"ok": True})),
]
