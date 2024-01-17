from decimal import Decimal
from .models import Passenger, Location, Flight, Ticket, Booking, Timetable
from rest_framework import serializers


class FlightSerializer(serializers.ModelSerializer):
    passengers = serializers.PrimaryKeyRelatedField(many=True, queryset=Passenger.objects.all())
    tickets = serializers.PrimaryKeyRelatedField(many=True, queryset=Ticket.objects.all())

    class Meta:
        model = Flight
        fields = '__all__'


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'


class PassengerSerializer(serializers.ModelSerializer):
    tickets = TicketSerializer(many=True, read_only=True)

    class Meta:
        model = Passenger
        fields = '__all__'


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"


class TimetableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timetable
        fields = '__all__'
