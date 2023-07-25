from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

# class User(AbstractUser):
#     class Meta:
#         db_table = 'auth_user'
#         app_label = 'auth.User'
    
#     # class Role(models.TextChoices):
#     #     MEMBER = "MEMBER", 'Member'
#     #     ADMIN = "ADMIN", 'Admin'
#     #     SUPERADMIN = 'SUPERADMIN', 'Super Admin'

#     # class Meta:
#     #     app_label = 'auth.User'
    
#     # base_role = Role.MEMBER

#     # role = models.CharField(max_length=50, choices=Role.choices)

#     # def save(self, *arg, **kwargs):
#     #     if not self.pk:
#     #         self.role = self.base_role
#     #         return super().save(*arg, **kwargs)