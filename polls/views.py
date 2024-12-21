from django.http import HttpResponse
from django.shortcuts import render
from .models import Usuarios
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as loginDjango
from django.contrib.auth.decorators import login_required
# Create your views here.
def cadastro(request):
    if request.method == 'GET':
        return render(request, 'usuarios/cadastro.html')
    else:
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        user = User.objects.filter(email=email).first()
        if user:
            return HttpResponse('Já existe um usuário com este e-mail.')
       
        novo_usuario = User.objects.create_user(email=email, password=senha, first_name=nome, username=email)
        novo_usuario.save()

        return HttpResponse('Usuário cadastrado com sucesso.')


def login(request):
    if request.method == 'GET':
        return render(request, 'usuarios/login.html')
    else:
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        user = authenticate(email=email, password=senha)

        if user:
            loginDjango(request, user)
            return HttpResponse('Login realizado com sucesso.')
        else:
            return HttpResponse('E-mail ou senha inválidas')
        
@login_required(login_url="/auth/login/")
def index(request):
    return HttpResponse('Online.')
