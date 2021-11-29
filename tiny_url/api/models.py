from django.db import models


class TinyUrl(models.Model):
    id = models.CharField(primary_key=True, max_length=10)
    url = models.CharField(max_length=1024)
    counter = models.BigIntegerField(default=0)

