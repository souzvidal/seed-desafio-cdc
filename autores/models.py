from django.db import models


class Autor(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    descricao = models.CharField(max_length=400)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome
