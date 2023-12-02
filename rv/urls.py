from django.urls import path
from .views import home, dashboard

urlpatterns = [
    path('',home, name='index'),
    path('dashboard/',dashboard, name='dashboard'),
]
