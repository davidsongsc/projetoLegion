from django.db import models
from django.contrib.auth import get_user_model

class Produtos(models.Model):
    nomeproduto = models.TextField()
    nomefantasia = models.TextField()
    valor = models.TextField()  # This field type is a guess.
    descricao = models.TextField()
    avaliacao = models.IntegerField()
    disponibilidade = models.IntegerField()
    qtd = models.IntegerField()
    grupo = models.IntegerField()
    grupoc = models.IntegerField(blank=True, null=True)
    combinag = models.IntegerField(blank=True, null=True)
    combinac = models.IntegerField(blank=True, null=True)
    def __str__(self) -> str:
        return self.nomeproduto
    class Meta:
        managed = False
        db_table = 'produtos'


class Comanda(models.Model):
    chave = models.IntegerField(blank=True, null=True)
    mesa = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    datahora = models.TextField(blank=True, null=True)
    itens = models.IntegerField(blank=True, null=True)
    pagamento = models.IntegerField(blank=True, null=True)
    operador = models.TextField(blank=True, null=True)  # This field type is a guess.
    gorjeta = models.FloatField(blank=False, null=False)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Comanda'

class Inventario(models.Model):
    id = models.IntegerField(primary_key=True, blank=False, null=False)
    produto_id = models.IntegerField(blank=True, null=True)
    listaid = models.IntegerField(blank=True, null=True)
    push = models.IntegerField(blank=True, null=True)
    nomeproduto = models.TextField()
    nomefantasia = models.TextField()
    valor = models.TextField()  # This field type is a guess.
    descricao = models.TextField()
    avaliacao = models.IntegerField()
    disponibilidade = models.IntegerField()
    qtd = models.IntegerField()
    grupo = models.IntegerField()
    grupoc = models.IntegerField(blank=True, null=True)
    combinag = models.IntegerField(blank=True, null=True)
    combinac = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Inventario'


class Itens(models.Model):
    itens = models.IntegerField(blank=True, null=True)
    produto = models.ForeignKey(
        'Produtos', models.DO_NOTHING, db_column='produto', blank=True, null=True)
    # This field type is a guess.
    gorjeta = models.TextField(blank=True, null=True)
    # This field type is a guess.
    desconto = models.TextField(blank=True, null=True)
    tipoproduto = models.IntegerField(blank=True, null=True)
    avaliacao = models.IntegerField(blank=True, null=True)
    datahora = models.TextField(blank=True, null=True)
    combinac = models.IntegerField(blank=True, null=True)
    combinag = models.IntegerField(blank=True, null=True)
    descricao = models.IntegerField(blank=True, null=True)
    disponibilidade = models.IntegerField(blank=True, null=True)
    grupo = models.IntegerField(blank=True, null=True)
    grupoc = models.IntegerField(blank=True, null=True)
    qtd = models.IntegerField(blank=True, null=True)
    # This field type is a guess.
    valor = models.TextField(blank=True, null=True)
    nomefantasia = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Itens'


class Grupos(models.Model):
    nome = models.TextField(blank=True, null=True)
    grupo_chave = models.IntegerField(blank=True, null=True)
    grupo_desc = models.TextField(blank=True, null=True)
    estilo = models.IntegerField(blank=True, null=True)
    visibilidade = models.IntegerField(blank=True, null=True)
    novidade = models.IntegerField(blank=True, null=True)
    subnome = models.TextField(blank=True, null=True)
    img = models.TextField(blank=True, null=True)
    grupocombo = models.IntegerField(blank=True, null=True)
    cmd = models.TextField(blank=True, null=True)
    cmdl = models.TextField(blank=True, null=True)
    grupoc = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'grupos'


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    first_name = models.CharField(max_length=150)
    token = models.CharField(max_length=16)
    pedido = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_user'
    def __str__(self) -> str:
        return self.username

class Colaborador(models.Model):
    usuario = models.ForeignKey(get_user_model(), models.DO_NOTHING, db_column='usuario', blank=True, null=True)
    nivel = models.IntegerField(blank=True, null=True)
    auth = models.TextField(blank=True, null=True)
    senha = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Colaborador'
    def __str__(self) -> str:
        return self.usuario


class ConsoleData(models.Model):
    id = models.AutoField(primary_key=True)
    codigo = models.TextField()
    datahora = models.DateTimeField()
    nivel = models.TextField()
    projeto = models.TextField()

    class Meta:
        db_table = 'console_data'  # Nome da tabela no banco de dados 'console_data'

    def __str__(self):
        return f'{self.id} - {self.codigo}'
    


class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.CharField(max_length=255)
    telefone = models.CharField(max_length=20)
    pergunta_secreta = models.CharField(max_length=255)
    resposta_secreta = models.CharField(max_length=255)
    email = models.EmailField()
    datahora = models.DateTimeField(auto_now_add=True)
    staff = models.IntegerField()
    member = models.IntegerField()
    adm = models.IntegerField()

    class Meta:
        db_table = 'usuario'
    
    def __str__(self):
        return f'{self.usuario} - {self.telefone}'