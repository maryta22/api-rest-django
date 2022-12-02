from django.db import models
from django_countries.fields import CountryField

class Cuenta(models.Model):
    saldo = models.DecimalField(max_digits = 2, decimal_places = 2)

    def __str__(self):
        return self.saldo


class Cliente(models.Model):

    MASCULINO = 'M'
    FEMENINO = 'F'

    GENERO_OPCIONES = (
        (MASCULINO, 'Masculino'),
        (FEMENINO, 'Femenino')
    )

    nombre = models.CharField(max_length=50)   
    apellido = models.CharField(max_length=50)
    correo = models.EmailField()
    genero = models.CharField(max_length=2, choices=GENERO_OPCIONES, default=FEMENINO)
    cuenta = models.ForeignKey(Cuenta, on_delete=models.CASCADE)
    pais =  CountryField()

    def __str__(self):
        return self.nombre

