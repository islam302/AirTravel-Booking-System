from decimal import Decimal
from .models import Passenger, Location, Flight, Ticket, Timetable
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

    def validate(self, data):
        flight = data.get('flight')
        booked_seats = Ticket.objects.filter(flight=flight).count()
        total_seats = flight.seats
        seat_number = data.get('seat_number')

        # CHECK IF THERE ARE SEATS OR NOT
        if booked_seats >= total_seats:
            raise serializers.ValidationError("No more seats available for this flight")
        # CHECK IF SEAT IS AVAILABLE
        elif seat_number <= 0 or seat_number > total_seats:
            raise serializers.ValidationError("This seat not available for this flight")
        # CHECK IF THE SEAT BOOKED
        elif Ticket.objects.filter(flight=flight, seat_number=seat_number).exists():
            raise serializers.ValidationError("This seat is already booked")

        return data


class PassengerSerializer(serializers.ModelSerializer):
    tickets = TicketSerializer(many=True, read_only=True)

    class Meta:
        model = Passenger
        fields = '__all__'


class TimetableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timetable
        fields = '__all__'
