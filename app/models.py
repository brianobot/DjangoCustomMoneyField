from django.db import models
from .fields import AssetField


class Money(models.Model):
    title = models.CharField(max_length=255, blank=True, default="default-title")
    descr = models.CharField(max_length=255, blank=True, default="default-descr")
    money = AssetField()
    # asset can be passed in as :
    # tuple of 2 item
    # list of 2 item
    