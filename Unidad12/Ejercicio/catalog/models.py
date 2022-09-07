from django.db import models
from django.urls import reverse
# Create your models here.

class Movie(models.Model):
    name = models.CharField(max_length=64, help_text="Pon el nombre de la Pelicula")
    summary = models.TextField(max_length=100, help_text="Sinopsis de la pelicula")
    directedby = models.ForeignKey('Director', on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('movie detail', args=[str(self.id)])

class Director(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)
    movies = models.ManyToManyField(Movie)

    def get_absolute_url(self):
        return reverse('director-detail', args=[str(self.id)])

    def __str__(self):
        return "%s, %s" % (self.last_name, self.first_name)