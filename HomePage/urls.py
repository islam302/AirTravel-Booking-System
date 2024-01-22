from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers
from django.conf import settings
from django.conf.urls.static import static
from . import views

router = routers.DefaultRouter()
router.register('locations', views.LocationViewSet, basename='locations')
router.register('flights', views.FlightViewSet, basename='flights')
router.register('tickets', views.TicketViewSet, basename='tickets')
router.register('passengers', views.PassengerViewSet, basename='passengers')
router.register('flight-search', views.FlightsSearchViewSet, basename='flight-search')

urlpatterns = router.urls
