from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Passenger, Location, Flight, Ticket, Timetable
from .serializers import PassengerSerializer, LocationSerializer, FlightSerializer, TimetableSerializer, TicketSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .permissions import IsAdminOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from cacheops import cached_as
from .filters import TimetableFilter

class PassengerViewSet(viewsets.ModelViewSet):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['GET'])
    def tickets(self, request, pk=None):
        passenger = self.get_object()
        tickets = Ticket.objects.filter(passenger=passenger)
        serializer = TicketSerializer(tickets, many=True)
        return Response(serializer.data)

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = [IsAdminUser]

class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    permission_classes = [IsAdminOrReadOnly]

class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [IsAdminUser]

    @action(detail=False, methods=['GET'])
    def seats(self, request):
        flights = Flight.objects.all()
        seats_available = {}
        for flight in flights:
            seats_available[flight.id] = flight.seats.count() > 0
        return Response(seats_available)

class FlightsSearchViewSet(viewsets.ModelViewSet):
    queryset = Timetable.objects.all()
    serializer_class = TimetableSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = TimetableFilter

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

