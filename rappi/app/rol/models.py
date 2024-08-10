from django.db import models

# Create your models here.

class Rol (models.Model):

    class Meta:
        verbose_name = "Rol"
        verbose_name_plural = "Rol"
        
    name = models.CharField('Nombre', max_length=100)
    state = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name}'