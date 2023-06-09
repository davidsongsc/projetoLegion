# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Colaborador(models.Model):
    usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='usuario', blank=True, null=True)
    nivel = models.IntegerField(blank=True, null=True)
    column1 = models.TextField(db_column='Column1', blank=True, null=True)  # Field name made lowercase.
    senha = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Colaborador'


class Pedido(models.Model):
    chave = models.AutoField(primary_key=True, blank=True, null=True)
    local = models.TextField(blank=True, null=True)
    id = models.TextField(blank=True, null=True)
    vendedor = models.TextField(blank=True, null=True)
    produtos = models.IntegerField(blank=True, null=True)
    datahora = models.TextField(blank=True, null=True)
    saida = models.TextField(blank=True, null=True)
    tempopreparo = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Pedido'


class Usuario(models.Model):
    usuario = models.TextField(unique=True, blank=True, null=True)
    nome = models.TextField(blank=True, null=True)
    email = models.IntegerField(unique=True, blank=True, null=True)
    senha = models.TextField(blank=True, null=True)
    is_admin = models.IntegerField(blank=True, null=True)
    psecret = models.TextField(blank=True, null=True)
    rsecret = models.TextField(blank=True, null=True)
    telefone = models.TextField(blank=True, null=True)
    id_publico = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Usuario'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


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

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class GrupoProdutos(models.Model):
    grupo_nome = models.CharField()
    grupo_chave = models.CharField()
    grupo_desc = models.TextField()  # This field type is a guess.
    estilo = models.IntegerField()
    visibilidade = models.IntegerField()
    novidade = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'grupo_produtos'


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

    class Meta:
        managed = False
        db_table = 'grupos'


class PedidoProduto(models.Model):
    chave = models.AutoField(primary_key=True, blank=True, null=True)
    id_pedido = models.TextField(blank=True, null=True)
    produto = models.IntegerField(blank=True, null=True)
    qtd = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pedido_produto'


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

    class Meta:
        managed = False
        db_table = 'produtos'
