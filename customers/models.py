from django.db import models

from django.contrib.postgres.fields import HStoreField


class Customer(models.Model):
    name = models.CharField(max_length=254)
    email = models.EmailField()

    preferences = HStoreField()

