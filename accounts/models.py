from django.db import models

from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    
    class Role(models.TextChoices):
        MEMBER = "MEMBER", 'Member'
        ADMIN = "ADMIN", 'Admin'
        SUPERADMIN = 'SUPERADMIN', 'Super Admin'
    
    base_role = Role.MEMBER

    username = models.CharField(max_length=150, unique=True, blank=True, null=True)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=15, choices=Role.choices, default=base_role)
    avatar = models.ImageField(default="profile_pics/profileDefault.png",upload_to='profile_pics/')
        
class Session(models.Model):
    id = models.CharField(primary_key=True)
    quota = models.IntegerField(default=3)