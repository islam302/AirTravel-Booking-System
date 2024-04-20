from rest_framework import viewsets
from rest_framework.generics import RetrieveAPIView
from .models import Passenger, Location, Flight, Ticket, Timetable
from .serializers import PassengerSerializer, LocationSerializer, FlightSerializer, TimetableSerializer, TicketSerializer
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
from . import models
import requests


class StudentProgressViewSet(ViewSet):

    def check_ids(self, data):
        goal_id = data.get('goal_id')
        student_id = data.get('student_id')
        student_goal_id = data.get('student_goal_id')
        levelstep_id = data.get('levelstep_id')

        if not all([goal_id, student_id, student_goal_id, levelstep_id]):
            return False
        return True

    def list(self, request):
        if not self.check_ids(request.query_params):
            return Response(
                {"error": "goal_id, student_id, student_goal_id, levelstep_id are required."},
                status=status.HTTP_400_BAD_REQUEST
            )

        student_process = StudentProgress.objects.all()
        serializer = StudentProgressSerializer(student_process, many=True)
        return Response(serializer.data)

    def update(self, request, pk=None):
        student_progress = get_object_or_404(StudentProgress, pk=pk)

        if not self.check_ids(request.data):
            return Response(
                {"error": "goal_id, student_id, student_goal_id, levelstep_id are required."},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = StudentProgressSerializer(student_progress, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        student_progress = get_object_or_404(StudentProgress, pk=pk)
        student_progress.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class StudentGoalViewSet(ViewSet):

    def check_ids(self, data):
        goal_id = data.get('goal_id')
        studentclass_id = data.get('studentclass_id')
        subscription_id = data.get('subscription_id')
        user_id = data.get('user_id')

        if not all([goal_id, studentclass_id, subscription_id, user_id]):
            return False
        return True

    def create(self, request):
        if not self.check_ids(request.data):
            return Response(
                {"error": "goal_id, studentclass_id, subscription_id, user_id are required."},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = StudentGoalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        if not self.check_ids(request.query_params):
            return Response(
                {"error": "goal_id, studentclass_id, subscription_id, user_id are required."},
                status=status.HTTP_400_BAD_REQUEST
            )

        student_goals = StudentGoal.objects.all()
        serializer = StudentGoalSerializer(student_goals, many=True)
        return Response(serializer.data)

    def update(self, request, pk=None):
        student_goal = get_object_or_404(StudentGoal, pk=pk)

        if not self.check_ids(request.data):
            return Response(
                {"error": "goal_id, studentclass_id, subscription_id, user_id are required."},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = StudentGoalSerializer(student_goal, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        student_goal = get_object_or_404(StudentGoal, pk=pk)
        student_goal.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PassengerViewSet(viewsets.ModelViewSet):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer
    # permission_classes = [IsAuthenticated]



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
    pass


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


