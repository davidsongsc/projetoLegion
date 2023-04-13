from django.db import models

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