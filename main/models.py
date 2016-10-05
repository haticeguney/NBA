from __future__ import unicode_literals

from django.db import models


class Player(models.Model):
    name = models.CharField(max_length=255)
    game = models.CharField(max_length=255)
    date = models.DateField()

    def __str__(self):
        return self.name
