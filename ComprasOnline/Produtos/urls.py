from django.urls import path

from Produtos import views

app_name = 'produtos'

urlpatterns = [
    path('criar_produto/', views.criar_produto, name='criar_produto'),
    path('listar_produtos/', views.listar_produtos, name='listar_produtos'),
    path('listar_produtos_falta/', views.listar_produtos_falta, name='listar_produtos_falta'),
    path('detalhes/<int:pk>', views.detalhes_produto, name='detalhes_produto'),
    
]