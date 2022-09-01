from unicodedata import name
from django.urls import path
from . import views


urlpatterns = [
    path('', views.Registro.as_view(), name='autenticacion'),
    path('logout/', views.cerrar_sesion, name='cerrar_sesion'),
    path('login/', views.login_user, name='login_user'),
]
