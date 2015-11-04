from django.db import models
from django.contrib.postgres.fields import ArrayField


class Ticket(models.Model):
    description = models.TextField()
    assigned_users = ArrayField(models.IntegerField())
