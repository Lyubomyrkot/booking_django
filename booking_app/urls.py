from django.contrib import admin
from django.urls import path

from booking_app import views

urlpatterns = [
    path('', views.home, name='home'),
    path('apartments/<int:apartment_id>/', views.apartments_page, name='apartments_page'),
    path('booking/<int:apartment_id>/', views.booking_page, name='booking_page'),
]
