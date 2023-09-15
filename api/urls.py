from django.urls import path, include
from . import views
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', views.api, name='portifolio'),
    path('index', views.index, name='index'),
    path('home', views.api, name='home'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('registro', views.register_user, name='registro'),
    path('comandas', views.listar_comandas, name='comandas'),
    path('itens', views.itens_omanda, name='itens'),
    path('produtos', views.listar_produtos, name='produtos'),
    path('inventario', views.listar_inventario, name='inventario'),
    path('grupos', views.listar_grupos, name='grupos'),
    path('loginadm', views.loginadm, name='loginadm'),
    path('cozinha', views.api, name='cozinha'),
    path('gprodutos', views.api, name='gprodutos'),
    path('caixa', views.api, name='caixa'),
    path('usuario', views.user_view, name='usuario'),
    path('getcookie', views.api, name='getcookie'),
    path('contato', views.api, name='contato'),
    path('todosroteiros/', views.todosRoteiros, name='todosroteiros'),
    path('pesquisar/<int:roteiro_id>/', views.pesquisarRoteiro, name='get_roteiro_by_id'),
    path('salvarroteiro/', views.salvar_roteiro, name='salvar_roteiro'),
    path('criar_usuario/', views.criar_usuario, name='criar_usuario'),
    path('login/', views.user_login, name='user_login'),
    # URL navegação
]
