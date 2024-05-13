from django.db import models
from tripbuddy.users.models import User

GENDER = (('male','MALE'), ('female', 'FEMALE'))
SEAT_CLASS = (('first','FIRST'), ('business','BUSINESS'),('economy','ECONOMY'))
TICKET_STATUS = (('confirmed','CONFIRMED'), ('cancelled','CANCELLED'), ('pending','PENDING'))


class Place(models.Model):
    airport_name = models.CharField(max_length=100)
    airport_code = models.CharField(max_length=3, unique=True)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.airport_name + "(" + self.airport_code + ")"

    def __eq__(self, other):
        return self.airport_code == other.airport_code


class Flight(models.Model):
    origin = models.CharField(max_length=3)
    destination = models.CharField(max_length=3)
    departure_time = models.TimeField()
    arrival_time = models.TimeField()
    duration = models.DurationField()
    airline = models.CharField(max_length=20)
    economy_fare = models.FloatField()
    first_fare = models.FloatField()
    business_fare = models.FloatField()

    def __str__(self):
        return self.origin + " TO " + self.destination

    
class Passenger(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    gender = models.CharField(max_length=20, choices=GENDER, blank=True)



class Booking(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="bookings")
    ref_no = models.CharField(max_length=6, unique=True)
    passengers = models.ManyToManyField(Passenger, related_name="flight_tickets")
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE, related_name="tickets")
    flight_dep_date = models.DateField()
    flight_arr_date = models.DateField()
    flight_fare = models.FloatField()
    other_charges = models.FloatField()
    coupon_used = models.CharField(max_length=15, blank=True)
    coupon_discount = models.FloatField(default=0.0)
    total_fare = models.FloatField()
    seat_class = models.CharField(max_length=20, choices=SEAT_CLASS)
    booking_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=45, choices=TICKET_STATUS)

    def __str__(self):
        return self.ref_no


