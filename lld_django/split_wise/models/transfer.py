from django.db import models
from django.conf import settings
from .base import Base
from .group import Group

class Transfer(Base):
    from_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, 
                                    related_name='from_user')
    to_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, 
                                    related_name='to_user')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    group_in = models.ForeignKey(Group, on_delete=models.CASCADE, null=True)

    class Meta:
        unique_together = ['from_user', 'to_user', 'group_in', ]