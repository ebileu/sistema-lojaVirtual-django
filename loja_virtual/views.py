from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
def pagina_inicial(request):
    return render(request, 'pagina_inicial.html')