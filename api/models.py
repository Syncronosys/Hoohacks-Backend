from django.db import models
from uuid import uuid4


class Client(models.Model):
    name = models.CharField(max_length=100)
    uuid = models.UUIDField(default=uuid4)

    anger = models.DecimalField(max_digits=6, decimal_places=5, default=0.0)
    contempt = models.DecimalField(
        max_digits=6, decimal_places=5, default=0.0)
    disgust = models.DecimalField(
        max_digits=6, decimal_places=5, default=0.0)
    fear = models.DecimalField(max_digits=6, decimal_places=5, default=0.0)
    happiness = models.DecimalField(
        max_digits=6, decimal_places=5, default=0.0)
    neutral = models.DecimalField(
        max_digits=6, decimal_places=5, default=0.0)
    sadness = models.DecimalField(
        max_digits=6, decimal_places=5, default=0.0)
    surprise = models.DecimalField(
        max_digits=6, decimal_places=5, default=0.0)


def hex_uuid():
    return uuid4().hex[:8]


class Session(models.Model):
    uuid = models.CharField(max_length=8, default=hex_uuid)
    members = models.ManyToManyField(Client)
