from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers.groupSerializer import GroupCreateSerializer
from .serializers.expenseSerializer import ExpenseCreateSerializer, \
                                    TransferViewSerializer
from .serializers.userExpenseSerializer import UserExpenseViewSerializer, \
                    UserExpensePaidBySerializer, UserExpenseOwedBySerializer
from .serializers.userSerializer import UserCreateSerializer, UserViewSerializer
from .models.group import Group
from .models.expense import Expense
from .models.userExpense import UserExpense
from .models.userExpensePaidBy import UserExpensePaidBy
from .models.userExpenseOwedBy import UserExpenseOwedBy
from .models.user import User
from .models.transfer import Transfer
from .services.settleUpTransfer import SettleUpTransfer


# Create your views here.
class GroupList(generics.ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupCreateSerializer

class GroupDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupCreateSerializer

class ExpenseList(generics.ListCreateAPIView):
    serializer_class = ExpenseCreateSerializer

    def get_queryset(self):
        group_in = self.request.query_params.get('group_in')
        queryset = Expense.objects.filter(group_in=group_in)
        return queryset

class ExpenseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseCreateSerializer

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
        

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = ExpenseCreateSerializer

class GroupExpense(generics.ListAPIView):
    serializer_class = ExpenseCreateSerializer

    def get_queryset(self):
        group_in = self.request.query_params.get('group_in')
        queryset = Expense.objects.filter(group_in=group_in)
        return queryset

class GroupExpensePaid(generics.ListAPIView):
    serializer_class = UserExpensePaidBySerializer

    def get_queryset(self):
        group_in = self.request.query_params.get('group_in')
        queryset = Expense.objects.filter(group_in=group_in)
        paid_by = UserExpensePaidBy.objects.filter(expense_paid__in=queryset)
        return paid_by

class GroupExpenseOwed(generics.ListAPIView):
    serializer_class = UserExpenseOwedBySerializer

    def get_queryset(self):
        group_in = self.request.query_params.get('group_in')
        queryset = Expense.objects.filter(group_in=group_in)
        owed_by = UserExpenseOwedBy.objects.filter(expense_owed__in=queryset)
        return owed_by

class SettleUp(generics.ListAPIView):

    def get_serializer_class(self):
        group_in = self.request.query_params.get('group_in')
        settle_up = SettleUpTransfer()
        settle_up.process(group_in)
        return TransferViewSerializer

    def get_queryset(self):
        group_in = self.request.query_params.get('group_in')
        queryset = Transfer.objects.filter(group_in=group_in)
        return queryset

class SettleUpDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transfer.objects.all()
    serializer_class = TransferViewSerializer