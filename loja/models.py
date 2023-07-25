from distutils.command.upload import upload
from django.db import models

# Create your models here.

class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.nome

class Marca(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    descricao = models.TextField()
    valor = models.IntegerField()
    imagem = models.ImageField(upload_to='image', blank=True)

    