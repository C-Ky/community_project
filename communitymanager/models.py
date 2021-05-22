from django.db import models
from django.contrib.auth.models import User


class Communaute(models.Model):
    nom = models.CharField(max_length=30)
    abonnes = models.ManyToManyField(User)

    def __str__(self):
        return self.nom


class Priorite(models.Model):
    label = models.CharField(max_length=10)

    def __str__(self):
        return self.label


class Post(models.Model):
    titre = models.CharField(max_length=50)
    description = models.TextField()
    date_creation = models.DateTimeField(auto_now=True)
    communaute = models.ForeignKey('Communaute', on_delete=models.CASCADE)
    priorite = models.ForeignKey('Priorite', on_delete=models.CASCADE)
    evenementiel = models.BooleanField(default=False)
    date_evenement = models.DateTimeField(null=True, blank=True)
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "{0} - {1}".format(self.titre, self.date_creation)
