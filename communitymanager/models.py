from django.db import models
from django.contrib.auth.models import User


class Communaute(models.Model):
    nom = models.CharField(max_length=30)
    abonnes = models.ManyToManyField(User)

    def __str__(self):
        return self.nom
