from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edicion")

    class Meta:
        verbose_name = "categoria"
        verbose_name_plural = "categorias"
        ordering = ['-created']

    def __str__(self):
        return self.name
    
class Portfolio(models.Model):
    image = models.ImageField(verbose_name="Imagen", upload_to="portfolio", null=True, blank=True)
    categories = models.ManyToManyField(Category, verbose_name="Categorias")
    title = models.CharField(max_length=200, verbose_name="Titulo")
    content = models.TextField(verbose_name="Contenido")
    visit = models.URLField(verbose_name="visitar", null=True, blank=True)
    repository = models.URLField(verbose_name="Repositorio", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edicion")
    
    class Meta:
        verbose_name = "portafolio"
        verbose_name_plural = "portafolio"
        ordering = ['created']
        
    def __str__(self):
        return self.title
    
class Project(models.Model):
    image = models.ImageField(verbose_name="Imagen", upload_to="projects", null=True, blank=True)
    categories = models.ManyToManyField(Category, verbose_name="Categorias")
    title = models.CharField(max_length=200, verbose_name="Titulo")
    content = models.TextField(verbose_name="Contenido")
    visit = models.URLField(verbose_name="visitar", null=True, blank=True)
    repository = models.URLField(verbose_name="Repositorio", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edicion")
    
    class Meta:
        verbose_name = "proyecto"
        verbose_name_plural = "proyectos"
        ordering = ['created']
        
    def __str__(self):
        return self.title
    
    