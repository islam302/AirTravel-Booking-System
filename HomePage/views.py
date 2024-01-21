from rest_framework import viewsets
from rest_framework.generics import RetrieveAPIView
from .models import Passenger, Location, Flight, Ticket, Booking, Timetable
from .serializers import PassengerSerializer, LocationSerializer, FlightSerializer, TimetableSerializer, \
    TicketSerializer, BookingSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .permissions import IsAdminOrReadOnly
from rest_framework.decorators import action
from django.shortcuts import render
from django.db.models import Q
from .filters import TimetableFilter
from django_filters.rest_framework import DjangoFilterBackend
from django.core.mail import send_mail
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


class PassengerViewSet(viewsets.ModelViewSet):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        passengers = Passenger.objects.all()
        return render(request, 'passenger.html', {'passengers': passengers})

    @action(detail=True, methods=['GET'])
    def tickets(self):
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


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

    def tickets(self, request, *args, **kwargs):
        booking = self.get_object()
        if booking.ticket_set.count() >= 5:
            raise ValidationError("A user can only book up to 5 tickets in a booking.")
        return super().list(request, *args, **kwargs)


class FlightsSearchViewSet(viewsets.ModelViewSet):
    queryset = Timetable.objects.all()
    serializer_class = TimetableSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = TimetableFilter


class SendEmailsViewSet(APIView):
    def post(self, request, *args, **kwargs):
        try:
            send_mail(
                subject='Subject',
                message='I will find you and I will kill you.',
                from_email='islambadran39@gmail.com',
                recipient_list=['no5510425@gmail.com'])
            return Response({'message': 'Email sent successfully.'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message': 'Internal server error.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def options(self, request, *args, **kwargs):
        return Response(status=status.HTTP_200_OK)
