from django.db import models
from django.contrib.auth.models import User

class Apartment(models.Model):
    TYPE_ROOM_CHOICES = [
        ('single', 'Single Room'),
        ('double', 'Double Room'),
        ('suite', 'Suite'),
        ('studio', 'Studio'),
        ('penthouse', 'Penthouse'),
        ('loft', 'Loft'),
        ('villa', 'Villa'),
    ]

    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    image = models.ImageField(upload_to='apartment_images/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    capacity = models.IntegerField(default=1)

    type_room = models.CharField(max_length=50, blank=True, null=True, choices=TYPE_ROOM_CHOICES)

    def __str__(self):
        return f"{self.name} - {self.location} - ${self.price}"
    
    class Meta:
        verbose_name = "Apartment"
        verbose_name_plural = "Apartments"
        ordering = ['name']


class Booking(models.Model):
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE, related_name='bookings')
    guest_name = models.CharField(max_length=100)
    guest_surname = models.CharField(max_length=100)
    guest_email = models.EmailField()
    guest_phone = models.CharField(max_length=20)
    check_in_date = models.DateTimeField()
    check_out_date = models.DateTimeField()
    price_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking for {self.guest_name} {self.guest_surname} at {self.apartment.name} from {self.check_in_date} to {self.check_out_date}"
    
    class Meta:
        verbose_name = "Booking"
        verbose_name_plural = "Bookings"
        ordering = ['-created_at']