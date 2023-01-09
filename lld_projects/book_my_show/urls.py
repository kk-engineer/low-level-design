from django.urls import path
from book_my_show import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('book_ticket/', views.book_ticket, name='ticket'),
    path('make_payment/', views.make_payment, name='payment')
]
