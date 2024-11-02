from django.urls import path
from .views import SignupView, LoginView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('signin/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('token/generate/', jwt_views.TokenObtainPairView.as_view(), name ='token_generate'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name ='token_refresh'),
]
