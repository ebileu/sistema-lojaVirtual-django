from django.urls import path, include
from . import views

urlpatterns = [
    path('pagina-inicial', views.pagina_inicial, name='pagina_inicial'),
    path('cadastro-produto', views.cadastro_produto, name='cadastro_produto'),
    path('deletar-produto', views.deletar_produto, name='deletar_produto'),
    path('produto-perfil', views.produto_perfil, name='produto_perfil'),
    path('editar-produto/<int:id>', views.editar_produto, name='editar_produto')
]
