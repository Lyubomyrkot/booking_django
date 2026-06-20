from django.shortcuts import render
from django.contrib import messages
import booking
from .models import Apartment, Booking
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required

def home(request):
    check_in = request.GET.get('check_in')
    check_out = request.GET.get('check_out')
    appartments = Apartment.objects.all()

    if check_in and check_out:
        appartments = Apartment.objects.exclude(
            bookings__check_in_date__lt=check_out,
            bookings__check_out_date__gt=check_in
        )
    
    return render(request, template_name='home.html', context={'appartments': appartments, 'check_in': check_in, 'check_out': check_out})


def apartments_page(request, apartment_id):
    apartment = Apartment.objects.get(id=apartment_id)
    return render(request, template_name='apartment_page.html', context={'apartment': apartment})


def booking_page(request, apartment_id):
    apartment = Apartment.objects.get(id=apartment_id)

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        check_in = request.POST.get('check_in')
        check_out = request.POST.get('check_out')

        # Here you can add validation for the input data if needed
        existing_booking = Booking.objects.filter(
            apartment=apartment, 
            check_in_date__lt=check_out, 
            check_out_date__gt=check_in
        )

        if existing_booking.exists():
            messages.error(request, 'The apartment is already booked for the selected dates.')
        
        else:
            booking = Booking.objects.create(
                apartment=apartment,
                guest_name=first_name,
                guest_surname=last_name,
                guest_email=email,
                guest_phone=phone,
                check_in_date=check_in,
                check_out_date=check_out,

                price_total=apartment.price, # You can calculate the total price based on the check-in and check-out dates if needed
                user=request.user if request.user.is_authenticated else None
            )
            return render(request, 'booking_confirm.html', context={'apartment': apartment, 'booking': booking})

    return render(request, template_name='booking.html', context={'apartment': apartment})

@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, template_name='my_bookings.html', context={'bookings': bookings})
