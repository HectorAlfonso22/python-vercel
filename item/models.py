from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return f'{self.title}, {self.description}'