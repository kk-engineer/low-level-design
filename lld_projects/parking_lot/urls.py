from django.urls import path
from parking_lot import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.index_page),
    path('display/', TemplateView.as_view(template_name='display.html'))
]