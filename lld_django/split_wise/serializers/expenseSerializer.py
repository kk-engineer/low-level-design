from rest_framework.serializers import ModelSerializer
from ..models.expense import Expense
from ..models.userExpensePaidBy import UserExpensePaidBy
from ..models.userExpenseOwedBy import UserExpenseOwedBy
from ..models.userExpense import UserExpense
from ..models.group import Group

class ExpenseCreateSerializer(ModelSerializer):
    #group = GroupViewSerializer()
    def create(self, validated_data):
        print("################")
        money = validated_data['amount']
        paid_by = validated_data['created_by']
        group = Group.objects.get(name=validated_data['group_id'])
        members = group.members.all()
        count = len(members)
        avg = money//count
        print(money, paid_by, avg, count)
        print(members)
        expense = Expense.objects.create(**validated_data)
        user_expense = UserExpense.objects.create(amount=(money-avg), 
                                                    ue_expense=expense,
                                                    ue_user=paid_by)
        UserExpensePaidBy.objects.create(expense_paid=expense, 
                                        user_expense_paid=user_expense)
        
        # Owed by
        owed_by = [m for m in members if m != paid_by]
        for ower in owed_by:
            user_expense = UserExpense.objects.create(amount=avg, 
                                                    ue_expense=expense,
                                                    ue_user=ower)
            UserExpenseOwedBy.objects.create(expense_owed=expense, 
                                        user_expense_owed=user_expense)
        return expense

    class Meta:
        model = Expense
        fields = '__all__'