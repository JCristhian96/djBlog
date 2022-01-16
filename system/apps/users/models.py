import email
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """ Modelo para el manejo de los Usuarios"""
    
    email = models.EmailField(unique=True, blank=False, null=False)
    web_site = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"