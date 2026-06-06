from django.shortcuts import render
from .models import Apartment, Booking
from django.http import HttpResponse

def home(request):
    appartments = Apartment.objects.all()

    return render(request, template_name='home.html', context={'appartments': appartments})

def apartments_page(request, apartment_id):
    apartment = Apartment.objects.get(id=apartment_id)
    return render(request, template_name='apartment_page.html', context={'apartment': apartment})

def booking_page(request, apartment_id):
    apartment = Apartment.objects.get(id=apartment_id)
    
    return render(request, template_name='booking.html', context={'apartment': apartment})