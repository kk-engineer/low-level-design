from django.db import models

from book_my_show.models.Theatre import Theatre


class Screen(models.Model):
    name = models.CharField(max_length=32)
    theatre = models.ManyToManyField(Theatre)

    def __str__(self):
        return self.name
