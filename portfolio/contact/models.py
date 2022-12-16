from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre y Apellido")
    email = models.EmailField(verbose_name="Direccion de correo electronico")
    phone = models.CharField(max_length=20, verbose_name="Telefono")
    content = models.TextField(verbose_name="Mensaje")
    
    class Meta:
        verbose_name = "contacto"
        verbose_name_plural = "contactos"
    
    def __str__(self):
        return self.name
    