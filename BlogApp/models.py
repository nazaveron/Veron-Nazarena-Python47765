from django.db import models

class pulsera1989(models.Model):
    imagen = models.ImageField(upload_to='pulseras_fotos', null=False, blank=False, default="n")
    autor = models.CharField(max_length=100, default="Desconocido")
    pais = models.CharField(max_length=50, default="Desconocido")
    edad = models.PositiveIntegerField(default=13)
    color_predominante = models.CharField(max_length=30, default="Blanco")
    def __str__(self):
        return f"{self.autor} - ({self.pais})"

class pulseraReputation(models.Model):
    imagen = models.ImageField(upload_to='pulseras_fotos', null=False, blank=False, default="n")
    autor = models.CharField(max_length=100, default="Desconocido")
    pais = models.CharField(max_length=50, default="Desconocido")
    edad = models.PositiveIntegerField(default=13)
    color_predominante = models.CharField(max_length=30, default="Blanco")
    def __str__(self):
        return f"{self.autor} - ({self.pais})"


class pulseraFolklore(models.Model):
    imagen = models.ImageField(upload_to='pulseras_fotos', null=False, blank=False, default="n")
    autor = models.CharField(max_length=100, default="Desconocido")
    pais = models.CharField(max_length=50, default="Desconocido")
    edad = models.PositiveIntegerField(default=13)
    color_predominante = models.CharField(max_length=30, default="Blanco")
    def __str__(self):
        return f"{self.autor} - ({self.pais})"


class pulseraLover(models.Model):
    imagen = models.ImageField(upload_to='pulseras_fotos', null=False, blank=False, default="n")
    autor = models.CharField(max_length=100, default="Desconocido")
    pais = models.CharField(max_length=50, default="Desconocido")
    edad = models.PositiveIntegerField(default=13)
    color_predominante = models.CharField(max_length=30, default="Blanco")
    def __str__(self):
        return f"{self.autor} - ({self.pais})"
    

