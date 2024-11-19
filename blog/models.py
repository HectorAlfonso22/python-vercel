from django.db import models

class Article(models.Model):  # Definición del modelo Article
    title = models.CharField(max_length=255)  # Campo de texto con longitud máxima de 255 caracteres
    content = models.TextField()  # Campo de texto más extenso para contenido