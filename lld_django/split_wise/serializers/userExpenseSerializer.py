from rest_framework.serializers import ModelSerializer
from ..models.userExpense import UserExpense
from ..models.userExpensePaidBy import UserExpensePaidBy
from ..models.userExpenseOwedBy import UserExpenseOwedBy
from .userSerializer import UserNameSerializer

class UserExpenseViewSerializer(ModelSerializer):
    ue_user = UserNameSerializer()
    class Meta:
        model = UserExpense
        exclude = ('created_at', 'updated_at', )

class UserExpensePaidBySerializer(ModelSerializer):
    user_expense_paid = UserExpenseViewSerializer()

    class Meta:
        model = UserExpensePaidBy
        exclude = ('created_at', 'updated_at', )

class UserExpenseOwedBySerializer(ModelSerializer):
    user_expense_owed = UserExpenseViewSerializer()

    class Meta:
        model = UserExpenseOwedBy
        exclude = ('created_at', 'updated_at', )