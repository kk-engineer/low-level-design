from django.urls import path
from parking_lot import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.index_page, name='main'),
    path('create_ticket/', views.create_ticket, name='ticket'),
    path('display/', views.get_spots, name='spots_status'),
    #path('display/', TemplateView.as_view(template_name='display.html'))
]