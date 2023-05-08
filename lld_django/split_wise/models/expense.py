from django.db import models
from django.conf import settings
from .base import Base
from .group import Group

class Expense(Base):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=10, default='INR')
    name = models.CharField(max_length=50)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,\
                                     related_name='expense')
    group_in = models.ForeignKey(Group, on_delete=models.CASCADE, null=True, 
                                    related_name='group_expense')
    participants = models.ManyToManyField(settings.AUTH_USER_MODEL, 
                                            related_name="shared_expense")

    class Meta:
        unique_together = ['name', 'created_by', ]

    def __str__(self):
        return self.name