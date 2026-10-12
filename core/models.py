from django.db import models


class Projeto(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    data_inicio = models.DateField()

    class Meta:
        ordering = ["-data_inicio"]

    def __str__(self):
        return self.nome


class Tarefa(models.Model):
    class Prioridade(models.IntegerChoices):
        BAIXA = 1, "Baixa"
        MEDIA = 2, "Média"
        ALTA = 3, "Alta"

    titulo = models.CharField("título", max_length=255)
    prioridade = models.SmallIntegerField(
        "prioridade",
        choices=Prioridade,
        default=Prioridade.BAIXA,
    )
    concluido = models.BooleanField("concluído", default=False)
    projeto = models.ForeignKey(
        Projeto,
        on_delete=models.CASCADE,
        related_name="tarefas",
        verbose_name="projeto",
    )

    class Meta:
        ordering = ("projeto__nome", "-prioridade", "titulo")

    def __str__(self):
        return self.titulo
