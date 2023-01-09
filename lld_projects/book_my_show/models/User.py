from django.db import models


class User(models.Model):
    name = models.CharField(max_length=64)
    email = models.EmailField()
    phone = models.CharField(max_length=16)

    def __str__(self):
        return self.name
