from django.db import models
from bacapres.models import Bacapres
from django.conf import settings

class Tweet(models.Model):
    tweet_id = models.TextField(default=None)
    text = models.TextField(default=None)
    user_name = models.CharField(default=None)
    created_at = models.DateTimeField(default=None)
    text_preprocessed = models.TextField(default=None)
    sentiment = models.TextField(default=None)
    bacapres = models.ForeignKey(Bacapres, on_delete=models.CASCADE)

class History(models.Model):
    start_date = models.DateTimeField(default=None)
    end_date = models.DateTimeField(default=None)

    tweet = models.ManyToManyField(Tweet)
    bacapres = models.ManyToManyField(Bacapres)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,  on_delete=models.CASCADE, null=True)
