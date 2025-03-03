from django.urls import path, include
from . import views

urlpatterns = [
    path('pagina-inicial', views.pagina_inicial, name='pagina_inicial')
]
