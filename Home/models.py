from django.db import models
from django.db.models import CharField

# Create your models here.
class Lagu(models.Model):
    judul = models.CharField(max_length=255)
    artis = models.CharField(max_length=255)
    teks = models.TextField(max_length=5000)
    def __str__(self):
        return self.judul