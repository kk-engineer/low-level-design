from django.db import models
from .base import Base
from .expense import Expense
from .userExpense import UserExpense

class UserExpenseOwedBy(Base):
    expense_owed = models.ForeignKey(Expense, on_delete=models.CASCADE, \
                                related_name='ue_owed_by')
    user_expense_owed = models.ForeignKey(UserExpense, on_delete=models.CASCADE, \
                                    related_name='owed_by')
    