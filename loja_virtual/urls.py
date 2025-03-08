from django.urls import path, include
from . import views

urlpatterns = [
    path('pagina-inicial', views.pagina_inicial, name='pagina_inicial'),
    path('cadastro-produto', views.cadastro_produto, name='cadastro_produto')
]
