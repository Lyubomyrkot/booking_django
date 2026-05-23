from django.shortcuts import render
from .models import Apartment, Booking

def home(request):
    appartments = Apartment.objects.all()
    return render(request, 'home.html', {'appartments': appartments})