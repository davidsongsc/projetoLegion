from django.shortcuts import render, redirect, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Produtos, Grupos, AuthUser, Comanda,Usuario, Itens, Inventario, Colaborador, ConsoleData
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import AccessToken
import json
from .kripto import criptografaTexto as ctext
# Tokens para autenticação de requisições
import secrets
from django.views.decorators.http import require_POST
from django.views.decorators.http import require_http_methods
from socketio import AsyncServer
from django.shortcuts import render
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.http import HttpResponse
from django.shortcuts import redirect
from django.db import connections



@csrf_exempt
def websocket(request):
    # Recupera o objeto do canal para usar para enviar mensagens
    channel_layer = get_channel_layer()
    # Aceita a conexão WebSocket
    ws = request.websocket
    # Adiciona o canal ao grupo 'mesas'
    async_to_sync(channel_layer.group_add)('mesas', ws.channel_name)
    try:
        # Loop infinito para lidar com as mensagens recebidas
        while True:
            message = ws.receive()
            if message is not None:
                # Envia a mensagem para todos os clientes no grupo 'mesas'
                async_to_sync(channel_layer.group_send)(
                    'mesas', {'type': 'send_message', 'text': message})
    finally:
        # Remove o canal do grupo 'mesas' quando a conexão é fechada
        async_to_sync(channel_layer.group_discard)('mesas', ws.channel_name)


def ws_connect(request, room_name):
    # Obtém a camada de canal (channel layer)
    channel_layer = get_channel_layer()
    # Cria um grupo com o nome da sala (room)
    async_to_sync(channel_layer.group_add)(
        room_name,
        request.channel_name
    )
    # Aceita a conexão WebSocket
    request.websocket.accept()
    # Loop infinito que escuta mensagens do WebSocket
    while True:
        message = request.websocket.receive()
        if message is None:
            # A conexão foi fechada
            async_to_sync(channel_layer.group_discard)(
                room_name,
                request.channel_name
            )
            break
        # Envia a mensagem recebida para o grupo da sala (room)
        async_to_sync(channel_layer.group_send)(
            room_name,
            {
                "type": "chat.message",
                "message": message.decode('utf-8')
            }
        )


def ws_message(message):
    # Envia a mensagem recebida para o cliente
    message.reply_channel.send({
        'text': message.content['message']
    })


def ws_disconnect(message):
    pass


TOKEN = secrets.token_hex(16)

# Create your views here.

TOKEN = "abc123"



def todosRoteiros(request):
    data = {
        'console_data': list(ConsoleData.objects.using('console_data_db').all().values()),
    }
    return JsonResponse(data, safe=False)

def pesquisarRoteiro(request, roteiro_id):
    # Define o banco de dados apropriado para a consulta
    using_db = 'console_data_db'  # Substitua pelo nome correto do banco de dados
    with connections[using_db].cursor() as cursor:
        try:
            cursor.execute("SELECT * FROM console_data WHERE id = %s", [roteiro_id])
            row = cursor.fetchone()

            if row:
                roteiro_id, codigo, datahora, nivel, projeto = row
                response_data = {
                    'id': roteiro_id,
                    'codigo': codigo,
                    'datahora': datahora,
                    'nivel': nivel,
                    'projeto': projeto,
                    # Outras propriedades que você deseja incluir na resposta
                }
                return JsonResponse(response_data)
            else:
                return JsonResponse({'error': 'Roteiro not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

@csrf_exempt
def criar_usuario(request):
    print(request.method)
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            
            # Define o banco de dados apropriado para salvar o novo usuário
            using_db = 'console_data_db'  # Substitua pelo nome correto do banco de dados
            with connections[using_db].cursor() as cursor:
                cursor.execute(
                    "INSERT INTO usuario (usuario, telefone, pergunta_secreta, resposta_secreta, email) "
                    "VALUES (%s, %s, %s, %s, %s)",
                    [
                        data.get('usuario'),
                        data.get('telefone'),
                        data.get('pergunta_secreta'),
                        data.get('resposta_secreta'),
                        data.get('email')
                    ]
                )

            return JsonResponse({'success': True})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)

@csrf_exempt
def salvar_roteiro(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            roteiro_id = data.get('id')
            codigo = data.get('codigo')

            # Define o banco de dados apropriado para a consulta
            using_db = 'console_data_db'  # Substitua pelo nome correto do banco de dados
            with connections[using_db].cursor() as cursor:
                try:
                    cursor.execute("UPDATE console_data SET codigo = %s WHERE id = %s", [codigo, roteiro_id])
                    # Ou use outro método de atualização apropriado com base no seu modelo
                    return JsonResponse({'success': True})
                except Exception as e:
                    return JsonResponse({'error': str(e)}, status=500)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)

@csrf_exempt
def user_login(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data.get('username')
            telefone = str(data.get('telefone'))

            # Especifique o banco de dados apropriado
            using_db = 'console_data_db'
            with connections[using_db].cursor() as cursor:
                cursor.execute(
                    "SELECT * FROM usuario WHERE usuario = %s AND telefone = %s",
                    [username, telefone]
                )
                row = cursor.fetchone()

            if row:
                user = row[0]  # O primeiro campo é o ID do usuário
                login(request, user)
                return JsonResponse({'success': True})
            else:
                return JsonResponse({'error': 'Invalid credentials'}, status=401)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)
    
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


@csrf_exempt
def criar_colaborador(request):
    if request.method == 'POST':
        # Recupera os dados do POST
        usuario_id = request.POST.get('usuario_id')
        nivel = request.POST.get('nivel')
        auth = request.POST.get('auth')
        senha = request.POST.get('senha')

        # Cria um novo colaborador com os dados do POST
        colaborador = Colaborador(
            usuario_id=usuario_id, nivel=nivel, auth=auth, senha=senha)
        colaborador.save()

        # Cria um dicionário com os dados do colaborador criado
        data = {"colaborador": {
            "id": colaborador.id,
            "usuario_id": colaborador.usuario_id,
            "nivel": colaborador.nivel,
            "auth": colaborador.auth,
            "senha": colaborador.senha
        }}

        # Retorna uma resposta JSON com os dados do colaborador criado
        return JsonResponse(data)
    else:
        # Se o método HTTP não for POST, retorna um erro 405 (Método não permitido)
        return HttpResponse("Método não permitido.", status=405)


def listar_inventario(request):
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
    inventario = Inventario.objects.all()
    data = {"inventario": list(inventario.values())}
    return JsonResponse(data)


def listar_colaboradores(request):

    colaboradores = Colaborador.objects.all()
    data = {"colaboradores": list(colaboradores.values())}
    return JsonResponse(data)


def listar_comandas(request):

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
    comandas = Comanda.objects.all()
    comandas = list(comandas.values())

    for comanda in comandas:

        itens = Itens.objects.filter(itens=comanda['itens'])

        comanda["itens"] = [list(itens.values())]

    # ite = Itens.objects.filter(itens=1)
    # itens = {"itens": list(ite.values())}

    jsondata = json.dumps(comandas)
    return HttpResponse(jsondata, content_type='application/json')


def itens_omanda(request):

    print(TOKEN)
    nome = request.GET.get('nome', '')
    token = request.GET.get('token', '')
    numero = request.GET.get('numero', '')

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
    itens = Produtos.objects.filter(id=numero)
    ite = list(itens.values())[0]
    # ite = Itens.objects.filter(itens=1)
    # itens = {"itens": list(ite.values())}

    jsondata = json.dumps(ite)
    return HttpResponse(jsondata, content_type='application/json')


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
def user_view(request):
    print(TOKEN)
    print(ctext(TOKEN))
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
    usuario = AuthUser.objects.filter(username=nome)
    data = list(usuario.values())
    return Response({'id': data[0]['id'],'nome': data[0]['first_name'], 'sobrenome': data[0]['last_name'], 'colaborador': data[0]['is_staff'], 'email': data[0]['email'], 'pedido': data[0]['pedido']})

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
            usuario = AuthUser.objects.filter(
            username=request.data.get('username'))
            data = list(usuario.values())
            return Response({'message': 'Login realizado com sucesso!',  'id': data[0]['id'], 'pedido': data[0]['pedido'], 'usuario': username,  'access_token': str(token)}, status=status.HTTP_200_OK)
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
    username = request.data.get('usuario')
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
    titulo = 'Legion'
    texto = 'Sistema & Controle'
    # Substitua 'outra_pagina' pela URL da página para redirecionar
    return redirect('/portifolio')
    # return render(request, 'api.html', {'titulo': titulo,
    #                                    'texto': texto,
    #                                    })


def index(request):
    titulo = 'Legion'
    texto = 'Sistema & Controle'
    return render(request, 'api.html', {'titulo': titulo,
                                        'texto': texto,
                                        })
