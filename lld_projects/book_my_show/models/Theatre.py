from django.db import models

from book_my_show.models.City import City


class Theatre(models.Model):
    name = models.CharField(max_length=64)
    address = models.CharField(max_length=64)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
