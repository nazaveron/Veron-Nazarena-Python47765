from django.db import models



class usuario(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    edad = models.PositiveIntegerField()

class pulsera1989(models.Model):
    autor = models.CharField(max_length=100, default="Desconocido")
    pais = models.CharField(max_length=50, default="Desconocido")
    edad = models.PositiveIntegerField(default=13)
    color_predominante = models.CharField(max_length=30, default="Blanco")
    def __str__(self):
        return f"{self.autor} - ({self.pais})"

class pulseraReputation(models.Model):
    autor = models.CharField(max_length=100, default="Desconocido")
    pais = models.CharField(max_length=50, default="Desconocido")
    edad = models.PositiveIntegerField(default=13)
    color_predominante = models.CharField(max_length=30, default="Blanco")
    def __str__(self):
        return f"{self.autor} - ({self.pais})"


class pulseraFolklore(models.Model):
    autor = models.CharField(max_length=100, default="Desconocido")
    pais = models.CharField(max_length=50, default="Desconocido")
    edad = models.PositiveIntegerField(default=13)
    color_predominante = models.CharField(max_length=30, default="Blanco")
    def __str__(self):
        return f"{self.autor} - ({self.pais})"


class pulseraLover(models.Model):
    autor = models.CharField(max_length=100, default="Desconocido")
    pais = models.CharField(max_length=50, default="Desconocido")
    edad = models.PositiveIntegerField(default=13)
    color_predominante = models.CharField(max_length=30, default="Blanco")
    def __str__(self):
        return f"{self.autor} - ({self.pais})"


class pulseraSpeakNow(models.Model):
    autor = models.CharField(max_length=100, default="Desconocido")
    pais = models.CharField(max_length=50, default="Desconocido")
    edad = models.PositiveIntegerField(default=13)
    color_predominante = models.CharField(max_length=30, default="Blanco")
    def __str__(self):
        return f"{self.autor} - ({self.pais})"
