from rest_framework import routers
from . import views
from django.urls import path
from django.contrib.auth import views as auth_views

from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView
)

router = routers.DefaultRouter()

urlpatterns = [
    #urls User
    path('me/', views.Me.as_view()), # visualiza el usuario logueado
    path('register/', views.RegisterView.as_view()),# registro de usuario
    path('users/', views.UsersView.as_view()), # lista de usuario
    path('users/<int:pk>/', views.UserUpdate.as_view()), # actualizacion de usuarios pasando el "id"
    path('token/', views.MyTokenObtainPairView.as_view()), # token para acceso
    path('change-password/', views.ResetPasswordView.as_view()),# cambio de contraseña usuario
    path('recover-password/', views.RecoverPasswordView.as_view()),# envio de coreeo para restanlecer password (link)
    path('reset-password/<int:user_id>/<str:token>/', views.reset_password),
]

urlpatterns += router.urls


