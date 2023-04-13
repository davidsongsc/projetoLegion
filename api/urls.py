from django.urls import path, include
from . import views

urlpatterns = [
    
    path('', views.api, name='index'),
    path('home', views.api, name='index'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='index'),
    path('registro', views.api, name='index'),
    path('comandas', views.api, name='index'),
    path('produtos', views.listar_produtos, name='produtos'),
    path('grupos', views.listar_grupos, name='index'),
    path('loginadm', views.loginadm, name='index'),
    path('cozinha', views.api, name='index'),
    path('gprodutos', views.api, name='index'),
    path('caixa', views.api, name='index'),
    path('usuario', views.user_view, name='index'),
    path('getcookie', views.api, name='index'),
    path('contato', views.api, name='index'),

   
    # URL navegação
    ]