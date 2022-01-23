from django.db import models

class Inquilinos(models.Model):
    nome = models.CharField(max_length=50)
    sexo = models.CharField(max_length=30)
    idade = models.IntegerField(max_length=30)
    telefone = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
