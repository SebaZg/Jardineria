from django.db import models

# Create your models here.


class Usuario(models.Model):
    idUsuario = models.AutoField(primary_key=True, verbose_name="ID de Usuario")
    nombre = models.CharField(
        max_length=100, null=False, verbose_name="Nombre de Usuario"
    )
    
    correo = models.CharField(
        max_length=100, null=False, verbose_name="Correo de Usuario"
    )
    
    
    Suscrito = models.BooleanField(default=False, verbose_name="suscripcion de Usuario")
    fechaSuscrito = models.DateTimeField(
        auto_now_add=True, null=True, verbose_name="Fecha Suscrito de Usuario"
    )
    Admin = models.BooleanField(default=False, verbose_name="Isadmin de Usuario")