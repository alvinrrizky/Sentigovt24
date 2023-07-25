from django.db import models

# Create your models here.
class Bacapres(models.Model):
    name = models.CharField(default=None, max_length=50, unique=True)
    desc = models.CharField(default=None, null=True)
    keyword = models.CharField(default=None,max_length=250)
    avatar = models.ImageField(default="profile_pics/profileDefault.png",upload_to='bacapres_pics/')