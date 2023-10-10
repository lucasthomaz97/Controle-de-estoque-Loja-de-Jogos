from django.db import models

class Jogo(models.Model):
    nome = models.CharField(max_length=100)
    desc = models.TextField(blank=True)
    qtt = models.BigIntegerField(default=0)
    preco_venda = models.FloatField(default=350.0)
    preco_custo = models.FloatField(default=270.0)
    pedidos = models.BigIntegerField(default=0)

    def __str__(self):
        return self.nome