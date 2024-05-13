from rest_framework import serializers

from tripbuddy.flights.models import Flight, Booking, Place


class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = '__all_'


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = '__all__'