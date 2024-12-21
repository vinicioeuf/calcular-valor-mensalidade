from django.db import models

# Create your models here.

class Usuarios(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=200)
    email = models.TextField(max_length=200)
    senha = models.TextField(max_length=500)