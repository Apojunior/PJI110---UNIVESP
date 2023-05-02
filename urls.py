from django.urls import path
from .view import cadastrar_cliente

urlpatterns = [
    path('cadastrar_cliente/', cadastrar_cliente, name='cadastrar_cliente')
]

