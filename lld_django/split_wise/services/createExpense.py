from ..models.expense import Expense
from ..models.userExpensePaidBy import UserExpensePaidBy
from ..models.userExpenseOwedBy import UserExpenseOwedBy
from ..models.userExpense import UserExpense

class CreateExpense:

    def process(self, validated_data):
        money = validated_data['amount']
        paid_by = validated_data['created_by']
        parties = validated_data['participants']
        count = len(parties)
        avg = money//count
        
        expense = Expense.objects.create(amount=validated_data['amount'],
                                        name=validated_data['name'],
                                        created_by=validated_data['created_by'],
                                        group_in=validated_data['group_in'])
        # set many to many field separately
        expense.participants.set(validated_data['participants'])

        user_expense = UserExpense.objects.create(amount=(money-avg), 
                                                    ue_expense=expense,
                                                    ue_user=paid_by)
        UserExpensePaidBy.objects.create(expense_paid=expense, 
                                        user_expense_paid=user_expense)
        
        # Owed by
        owed_by = [party for party in parties if party != paid_by]
        for ower in owed_by:
            user_expense = UserExpense.objects.create(amount=avg, 
                                                    ue_expense=expense,
                                                    ue_user=ower)
            UserExpenseOwedBy.objects.create(expense_owed=expense, 
                                        user_expense_owed=user_expense)
        return expense