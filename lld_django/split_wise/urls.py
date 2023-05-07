from django.urls import path
from . import views

urlpatterns = [
    path('groups/', views.GroupList.as_view()),
    path('groups/<int:pk>/', views.GroupDetail.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('expenses/', views.ExpenseList.as_view()),
    path('expenses/<int:pk>/', views.ExpenseDetail.as_view()),
]