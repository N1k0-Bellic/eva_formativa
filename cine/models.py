import uuid
from django.db import models

class Genero(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.nombre

class Pelicula(models.Model):
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE, related_name='peliculas')
    titulo = models.CharField(max_length=150)
    sinopsis = models.TextField(blank=True)
    afiche = models.ImageField(upload_to='afiches/', blank=True, null=True)
    precio = models.IntegerField()
    en_cartelera = models.BooleanField(default=True)
    def __str__(self):
        return self.titulo

class Ticket(models.Model):
    pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE, related_name='tickets')
    nombre_comprador = models.CharField(max_length=100)
    correo_comprador = models.EmailField()
    cantidad = models.PositiveIntegerField()
    fecha_compra = models.DateTimeField(auto_now_add=True)
    codigo = models.CharField(max_length=50, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.codigo:
            self.codigo = str(uuid.uuid4()).upper()[:8]
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Ticket {self.codigo} - {self.pelicula.titulo}"