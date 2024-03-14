from django.db import models
# No arquivo models.py dentro da sua pasta core

class Dados(models.Model):
    sensor = models.BooleanField()
    botao = models.BooleanField()
    liga_robo = models.BooleanField()
    reset_contador = models.BooleanField()
    valor_contagem = models.IntegerField()
