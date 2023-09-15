from django.contrib import admin
from .models import Produtos, Comanda, Inventario, Itens, Grupos, AuthUser, Colaborador, ConsoleData

@admin.register(Produtos)
class ProdutosAdmin(admin.ModelAdmin):
    pass

@admin.register(Comanda)
class ComandaAdmin(admin.ModelAdmin):
    pass

@admin.register(Inventario)
class InventarioAdmin(admin.ModelAdmin):
    pass

@admin.register(Itens)
class ItensAdmin(admin.ModelAdmin):
    pass

@admin.register(Grupos)
class GruposAdmin(admin.ModelAdmin):
    pass

@admin.register(AuthUser)
class AuthUserAdmin(admin.ModelAdmin):
    pass

@admin.register(Colaborador)
class ColaboradorAdmin(admin.ModelAdmin):
    pass

@admin.register(ConsoleData)
class ConsoleDataAdmin(admin.ModelAdmin):
    using = 'console_data_db'  # Direciona as consultas deste admin para o banco de dados 'console_data_db'
    pass
