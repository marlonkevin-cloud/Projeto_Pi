from django.db import models

class Projeto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    data_inicio = models.DateField()

    def __str__(self):
        return self.nome

class Tarefa(models.Model):
    titulo = models.CharField()
    prioridade = models.CharField()
    concluido = models.BooleanField()
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
