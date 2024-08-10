from django.db import models
from ..rol.models import Rol
# Create your models here.

class Accounts (models.Model):

    name = models.CharField('Nombre', max_length=100)
    last_name = models.CharField('Apellidos', max_length=100)
    phone = models.IntegerField('Teléfono')
    email = models.EmailField('Email', null=True, blank=True)
    
    rol = models.ForeignKey(
        Rol,
        verbose_name="Rol",
        on_delete=models.CASCADE,
        null=True,
        blank=True


    )
    def __str__(self):
        return f'{self.name}  - {self.phone} - {self.rol}'