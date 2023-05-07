from django.db import models
from django.conf import settings
from .base import Base
from .expense import Expense
from .user import User

class UserExpense(Base):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    ue_expense = models.ForeignKey(Expense, on_delete=models.CASCADE, \
                                related_name='expense_user')
    ue_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, \
                            related_name='user_expense')