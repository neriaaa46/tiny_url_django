from django.db import models
from datetime import datetime


class TinyUrl(models.Model):
    id = models.CharField(primary_key=True, max_length=10)
    url = models.CharField(max_length=1024)


class TinyUrlRequest(models.Model):
    id = models.AutoField(primary_key=True)
    tiny_url = models.ForeignKey(TinyUrl, on_delete=models.CASCADE, max_length=10)
    date = models.DateField(default=datetime.now)


