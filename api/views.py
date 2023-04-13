from django.shortcuts import render, redirect, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Produtos, Grupos
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import AccessToken

# Tokens para autenticação de requisições
import secrets

TOKEN = secrets.token_hex(16)

# Create your views here.

TOKEN = "abc123"


def listar_produtos(request):
    print(TOKEN)
    nome = request.GET.get('nome', '')
    token = request.GET.get('token', '')

    if not token or token != TOKEN:
        # Se o token não for fornecido ou não for válido, retornar erro 401
        return HttpResponse("Token inválido.", status=401)

    if not nome:
        # Se o nome não for fornecido, retornar erro 400
        return HttpResponse("O parâmetro 'nome' é obrigatório.", status=400)

    if len(nome) < 3:
        # Se o nome tiver menos de 3 caracteres, retornar erro 400
        return HttpResponse("O nome deve ter pelo menos 3 caracteres.", status=400)

    if not nome.isalnum():
        # Se o nome contiver caracteres não alfanuméricos, retornar erro 400
        return HttpResponse("O nome não pode conter caracteres especiais.", status=400)

    # Se o nome for válido e o token for válido, prosseguir com a lógica do endpoint
    produto = Produtos.objects.all()
    data = {"produtos": list(produto.values())}
    return JsonResponse(data)


def listar_grupos(request):
    print(TOKEN)
    nome = request.GET.get('nome', '')
    token = request.GET.get('token', '')

    if not token or token != TOKEN:
        # Se o token não for fornecido ou não for válido, retornar erro 401
        return HttpResponse("Token inválido.", status=401)

    if not nome:
        # Se o nome não for fornecido, retornar erro 400
        return HttpResponse("O parâmetro 'nome' é obrigatório.", status=400)

    if len(nome) < 3:
        # Se o nome tiver menos de 3 caracteres, retornar erro 400
        return HttpResponse("O nome deve ter pelo menos 3 caracteres.", status=400)

    if not nome.isalnum():
        # Se o nome contiver caracteres não alfanuméricos, retornar erro 400
        return HttpResponse("O nome não pode conter caracteres especiais.", status=400)

    # Se o nome for válido e o token for válido, prosseguir com a lógica do endpoint
    grupo = Grupos.objects.all()
    data = {"grupos": list(grupo.values())}
    return JsonResponse(data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_view(request):
    user = request.user
    return Response({'nome': user.first_name, 'colaborador': user.is_staff, 'email': user.email})

# Login Administrativo API


def loginadm(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/usuario')
        else:
            return render(request, 'login.html', {'error_message': 'Usuário ou senha inválidos.'})
    else:
        return render(request, 'login.html')

# Metodo de Login (React, Django API)


@api_view(['POST'])
def login_view(request):
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            token = AccessToken.for_user(user)
            return Response({'message': 'Login realizado com sucesso!', 'usuario': username, 'access_token': str(token)}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Usuário ou senha inválidos.'}, status=status.HTTP_401_UNAUTHORIZED)
    else:
        return render(request, 'login.html')


# Logout Administrativo API
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/usuario')


@api_view(['POST'])
def register_user(request):
    username = request.data.get('username')
    password = request.data.get('password')
    email = request.data.get('email')

    # Validar dados
    if not username or not password or not email:
        return Response({'message': 'Por favor, preencha todos os campos'}, status=status.HTTP_400_BAD_REQUEST)

    # Verificar se usuário já existe
    if User.objects.filter(username=username).exists():
        return Response({'message': 'Usuário já existe'}, status=status.HTTP_400_BAD_REQUEST)

    # Criar novo usuário
    user = User.objects.create_user(
        username=username, password=password, email=email)
    user.save()

    # Retornar resposta de sucesso
    return Response({'message': 'Usuário criado com sucesso'}, status=status.HTTP_201_CREATED)


def api(request):
    titulo = 'Demas & Divas'
    texto = 'Area restrita!'
    return render(request, 'api.html', {'titulo': titulo,
                                        'texto': texto,
                                        })
