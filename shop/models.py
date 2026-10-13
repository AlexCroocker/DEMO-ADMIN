from django.db import models

class Pelicula(models.Model):
    nombre = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    fecha_estreno = models.DateField()
    stock = models.PositiveSmallIntegerField()
    sinopsis = models.TextField(blank=True)
    oferta = models.BooleanField()

    def __str__(self):
        return self.nombre

class Juego(models.Model):
    nombre = models.CharField(max_length=100)
    desarrollador = models.CharField(max_length=100)
    fecha_lanzamiento = models.DateField()
    descripcion = models.TextField(blank=True)
    stock = models.PositiveSmallIntegerField()
    oferta = models.BooleanField()

    def __str__(self):
        return self.nombre

class Libro(models.Model):
    nombre = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    fecha_publicacion = models.DateField()
    descripcion = models.TextField(blank=True)
    stock = models.PositiveSmallIntegerField()
    oferta = models.BooleanField()

    def __str__(self):
        return self.nombre

class Musica(models.Model):
    nombre = models.CharField(max_length=100)
    artista = models.CharField(max_length=100)
    fecha_lanzamiento = models.DateField()
    descripcion = models.TextField(blank=True)
    stock = models.PositiveSmallIntegerField()
    oferta = models.BooleanField()

    def __str__(self):
        return self.nombre
