<<<<<<< HEAD
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse


class PassengerViewSetTestCase(APITestCase):
    def view_passengers(self):
        client = APIClient()
        response = self.client.get(reverse('Home/passengers/'))
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
=======
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from model_bakery import baker
from HomePage.models import Passenger
import pytest

@pytest.mark.django_db
class TestPassenger:
    def test_create_passenger(self, api_client, authenticated_user):
        client = api_client
        client.force_authenticate(user=authenticated_user)
        passenger_data = baker.make(Passenger)
        response = client.post('/Home/passengers/', data={'passenger_data_key': passenger_data.id})

        assert response.status_code == status.HTTP_200_OK



from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from model_bakery import baker
from HomePage.models import Passenger
import pytest

@pytest.mark.django_db
class TestPassenger:
    def test_create_passenger(self, api_client, authenticated_user):
        client = api_client
        client.force_authenticate(user=authenticated_user)
        passenger_data = baker.make(Passenger)
        response = client.post('/Home/passengers/', data={'passenger_data_key': passenger_data.id})

        assert response.status_code == status.HTTP_200_OK
>>>>>>> d912c379733bdcc70af27c86e773847a1a52134b
