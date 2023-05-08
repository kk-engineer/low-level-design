from ..models.expense import Expense
from ..models.group import Group
from ..models.transfer import Transfer
from ..models.userExpensePaidBy import UserExpensePaidBy
from ..models.userExpenseOwedBy import UserExpenseOwedBy
from heapq import heapify, heappush, heappop
from django.db.models import Q
from .createExpense import CreateExpense
from collections import defaultdict

class SettleUpTransfer:

    def process(self, group_in):
        print("Settling Up: ", group_in)
        group_exists = Group.objects.filter(base_ptr_id=group_in).exists()
        if not group_exists: return
        group = Group.objects.get(base_ptr_id=group_in)
        queryset = Expense.objects.filter(group_in=group_in)
        paid_by = UserExpensePaidBy.objects.filter(expense_paid__in=queryset)
        owed_by = UserExpenseOwedBy.objects.filter(expense_owed__in=queryset)

        
        user_net_share = defaultdict(int)
        for payer in paid_by:
            amount = payer.user_expense_paid.amount
            user = payer.user_expense_paid.ue_user
            user_net_share[user] += amount
            
        for ower in owed_by:
            amount = ower.user_expense_owed.amount
            user = ower.user_expense_owed.ue_user
            user_net_share[user] -= amount
        
        paid_by_heap, owed_by_heap = [], []
        for user, amount in user_net_share.items():
            if amount > 0:
                # heap compares the elements sequentially, 
                # if 1st elt is same, 2nd is compared and so on ...
                #heappush(paid_by_heap, (-amount, id(user), user)) 
                heappush(paid_by_heap, (-amount, id(user), user))
            elif amount < 0:
                heappush(owed_by_heap, (amount, id(user), user)) 
       
        while owed_by_heap and paid_by_heap:
            curr_owed_amount, paid_id,  curr_owed_user = heappop(owed_by_heap)
            curr_paid_amount, owed_id, curr_paid_user = heappop(paid_by_heap)

            # Should not settle with self
            if curr_owed_user == curr_paid_user: continue

            curr_paid_amount, curr_owed_amount = -curr_paid_amount, -curr_owed_amount
            settled_amount = 0
            if curr_paid_amount > curr_owed_amount:
                # check if already settled
                already_settled = Transfer.objects.filter(Q(from_user=curr_owed_user) & 
                                                            Q(to_user=curr_paid_user) &
                                                            Q(group_in=group_in)
                                                            ).exists()
                if already_settled: continue
                
                settled_amount = curr_owed_amount
                balance = curr_paid_amount - curr_owed_amount
                heappush(paid_by_heap, (-balance, paid_id, curr_paid_user))
            elif curr_owed_amount > curr_paid_amount:
                already_settled = Transfer.objects.filter(Q(from_user=curr_owed_user) & 
                                                            Q(to_user=curr_paid_user) &
                                                            Q(group_in=group_in)
                                                            ).exists()
                if already_settled: continue
                
                settled_amount = curr_paid_amount
                balance = curr_owed_amount - curr_paid_amount 
                heappush(owed_by_heap, (-balance, owed_id, curr_owed_user))
            else:
                already_settled = Transfer.objects.filter(Q(from_user=curr_owed_user) & 
                                                            Q(to_user=curr_paid_user) &
                                                            Q(group_in=group_in)
                                                            ).exists()
                if already_settled: continue
                settled_amount = curr_paid_amount
                
            Transfer.objects.create(from_user=curr_owed_user,
                                    to_user=curr_paid_user,
                                    amount=settled_amount,
                                    group_in=group)
            
            """
            # add the corresponding expense
            expense_name = "Settled_" + curr_owed_user.username + "_" + \
                                         curr_paid_user.username
            data = {
                'amount': settled_amount,
                'name': expense_name, 
                'created_by': curr_owed_user,
                'group_in': group,
                'participants': [curr_paid_user, curr_owed_user],
            }
            create_expense = CreateExpense()
            create_expense.process(data)
            """
	