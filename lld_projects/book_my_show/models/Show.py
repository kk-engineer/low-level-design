from django.db import models
from django.db.models import UniqueConstraint
from django.utils import timezone

from book_my_show.models.Language import Language
from book_my_show.models.Movie import Movie
from book_my_show.models.Screen import Screen
from book_my_show.models.Theatre import Theatre
from book_my_show.models.Visual import Visual


class Show(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    start_time = models.DateTimeField(default=timezone.now)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    visuals = models.ForeignKey(Visual, on_delete=models.CASCADE)
    screen = models.ForeignKey(Screen, on_delete=models.CASCADE)
    theatre = models.ForeignKey(Theatre, on_delete=models.CASCADE, default='PVR Cinemas')

    def __str__(self):
        return str(self.start_time)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['movie', 'start_time', 'language', 'screen', 'theatre'],
                                    name='unique_show')
            ]

    link = 'Edit'
