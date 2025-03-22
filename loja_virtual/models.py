from django.db import models

# Create your models here.
class Produto(models.Model):
    nome_produto = models.CharField(max_length=255)
    descricao = models.TextField(max_length=255)
    preco = models.FloatField()
    quantidade = models.PositiveIntegerField()

    def __str__(self):
        return self.nome_produto

