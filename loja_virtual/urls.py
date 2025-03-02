from django.urls import path, include

urlpatterns = [
    path('página-inicial', include('loja.urls'))
]
