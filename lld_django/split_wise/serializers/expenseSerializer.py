from rest_framework.serializers import ModelSerializer
from ..services.createExpense import CreateExpense
from .userSerializer import UserNameSerializer
from ..models.expense import Expense
from ..models.transfer import Transfer

class ExpenseCreateSerializer(ModelSerializer):
    def create(self, validated_data):
        create_expense = CreateExpense()
        return create_expense.process(validated_data)

    class Meta:
        model = Expense
        fields = '__all__'

class TransferViewSerializer(ModelSerializer):
    from_user = UserNameSerializer()
    to_user = UserNameSerializer()
    class Meta:
        model = Transfer
        exclude = ('created_at', 'updated_at', )