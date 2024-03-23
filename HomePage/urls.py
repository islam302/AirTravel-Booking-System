from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('locations', views.LocationViewSet, basename='locations')
router.register('flights', views.FlightViewSet, basename='flights')
router.register('tickets', views.TicketViewSet, basename='tickets')
router.register('passengers', views.PassengerViewSet, basename='passengers')
router.register('flight-search', views.FlightsSearchViewSet, basename='flight-search')

urlpatterns = [
    path('', include(router.urls)),
]

