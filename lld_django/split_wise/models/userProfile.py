from django.db import models
from django.conf import settings
from phone_field import PhoneField
from .base import Base
from .user import User

class UserProfile(Base):

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=False,
                                related_name='profile')
    
    phone_number = PhoneField(blank=True, help_text='Contact Phone Number')