from django.db import models


class Projeto(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    data_inicio = models.DateField()

    class Meta:
        ordering = ['-data_inicio']

    def __str__(self):
        return self.nome