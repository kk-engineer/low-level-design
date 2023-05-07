from django.db import models
from django.conf import settings
from .base import Base

class Group(Base):
    name = models.CharField(max_length=50)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, 
                                    related_name='admin')
    members = models.ManyToManyField(settings.AUTH_USER_MODEL)

    class Meta:
        unique_together = ['name', 'created_by', ]
    
    def __str__(self):
        return self.name