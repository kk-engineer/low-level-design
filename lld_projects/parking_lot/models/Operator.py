from django.db import models


class Operator(models.Model):
    name = models.TextField()
    email = models.EmailField()
    phone_number = models.TextField()

    def __str__(self):
        return self.name
