from django.db import models
from django.db import models as m
from django.db.models import Model as M, DecimalField as DF, IntegerField as IF, CharField as CF
from django.db.models import ForeignKey as FK, DateField as DateF


# Create your models here.

class Predio(M):
    ancho = DF(max_digits=13, decimal_places=3) # en metros
    largo = DF(max_digits=13, decimal_places=3)
class Especie(M):
    nombre = CF(max_length=20)
class Plantacion(M):
    especie = FK('Especie',on_delete=m.CASCADE)
    fecha = DateF()
    distancia = DF(max_digits=6, decimal_places=3)
    ancho_del_borde = DF(max_digits=6, decimal_places=3)
    
    class Meta:
        verbose_name_plural = 'Plantaciones'
