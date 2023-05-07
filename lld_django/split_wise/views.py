from django.shortcuts import render
from rest_framework import generics, viewsets
from .serializers.groupSerializer import GroupCreateSerializer
from .serializers.expenseSerializer import ExpenseCreateSerializer
from .serializers.userSerializer import UserCreateSerializer, UserViewSerializer
from .models.group import Group
from .models.expense import Expense
from .models.user import User


# Create your views here.
class GroupList(generics.ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupCreateSerializer

class GroupDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupCreateSerializer

class ExpenseList(generics.ListCreateAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseCreateSerializer

class ExpenseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseCreateSerializer

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
        

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserViewSerializer


