from django.db import models

class Pessoas(models.Model):
    nome = models.CharField(max_length=50)
    sexo = models.CharField(max_length=30)
    idade = models.IntegerField(max_length=30)
    telefone = models.CharField(max_length=30)
    email = models.CharField(max_length=30)

class Unidades(models.Model):
    nindentifica = models.CharField(max_length=50)
    proprietario = models.CharField(max_length=30)
    condominio = models.CharField(max_length=30)
    endereco = models.CharField(max_length=30)
