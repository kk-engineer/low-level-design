from django.urls import path
from . import views

urlpatterns = [
    path('groups/', views.GroupList.as_view()),
    path('groups/<int:pk>/', views.GroupDetail.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('expenses/', views.ExpenseList.as_view()),
    path('expenses/<int:pk>/', views.ExpenseDetail.as_view()),
    path('get_expenses/', views.GroupExpense.as_view(), name='expenses'),
    path('get_paid_by/', views.GroupExpensePaid.as_view(), name='paid_by'),
    path('get_owed_by/', views.GroupExpenseOwed.as_view(), name='owed_by'),
    path('settleup/', views.SettleUp.as_view(), name='settle_up'),
    path('settleup/<int:pk>/', views.SettleUpDetail.as_view(), name='settle_up_detail'),
]