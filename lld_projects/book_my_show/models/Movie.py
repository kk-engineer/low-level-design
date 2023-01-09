from django.db import models

from book_my_show.models.Language import Language
from book_my_show.models.Visual import Visual


class Movie(models.Model):
    name = models.CharField(max_length=64)
    #duration = models.DurationField()
    languages = models.ManyToManyField(Language)
    visual = models.ManyToManyField(Visual)

    def __str__(self):
        return self.name