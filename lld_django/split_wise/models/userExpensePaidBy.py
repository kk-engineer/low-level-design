from django.db import models
from .base import Base
from .expense import Expense
from .userExpense import UserExpense

class UserExpensePaidBy(Base):
    expense_paid = models.ForeignKey(Expense, on_delete=models.CASCADE, \
                                related_name='ue_paid_by')
    user_expense_paid = models.ForeignKey(UserExpense, on_delete=models.CASCADE, \
                                    related_name='paid_by')