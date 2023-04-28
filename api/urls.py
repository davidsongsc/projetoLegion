from django.urls import path, include
from . import views
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', views.api, name='index'),
    path('home', views.api, name='index'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='index'),
    path('registro', views.api, name='index'),
    path('comandas', views.listar_comandas, name='index'),
    path('itens', views.itens_omanda, name='index'),
    path('produtos', views.listar_produtos, name='produtos'),
    path('inventario', views.listar_inventario, name='inventario'),
    path('grupos', views.listar_grupos, name='index'),
    path('loginadm', views.loginadm, name='index'),
    path('cozinha', views.api, name='index'),
    path('gprodutos', views.api, name='index'),
    path('caixa', views.api, name='index'),
    path('usuario', views.user_view, name='index'),
    path('getcookie', views.api, name='index'),
    path('contato', views.api, name='index'),
    path('api', views.listar_colaboradores, name='listar_colaboradores'),

    # URL navegação
]
