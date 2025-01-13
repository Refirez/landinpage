from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    whatsapp = models.CharField(max_length=15)

    def __str__(self):
        return self.nome

# Create your models here.
