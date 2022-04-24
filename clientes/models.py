from django.db import models


class Person(models.Model):
    nome = models.CharField(max_length=30)
    sobrenome = models.CharField(max_length=30)
    idade = models.IntegerField()
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    biografia = models.TextField()
    foto = models.ImageField(upload_to='clients_photos', null=True, blank=True)
    # null e blank true deixam o campo opcional

    def __str__(self):  # display do usuário
        return f'{self.nome} {self.sobrenome}'