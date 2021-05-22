from django.db import models

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _

from .managers import CustomUserManager

# Create your models here.


class Lab(models.Model):
    name = models.CharField(max_length=255,null=True,blank=True)
    address = models.CharField(max_length=200,null=True,blank=True)




class User(AbstractUser):
    
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email