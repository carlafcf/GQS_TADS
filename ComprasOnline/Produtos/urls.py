from django.urls import path

from Produtos import views

app_name = 'produtos'

urlpatterns = [
    path('listar_produtos/', views.listar_produtos, name='listar_produtos'),
    path('listar_produtos_falta/', views.listar_produtos_falta, name='listar_produtos_falta'),
    path('criar_produto/', views.criar_produto, name='criar_produto')
]