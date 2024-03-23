from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse


class PassengerViewSetTestCase(APITestCase):
    def view_passengers(self):
        client = APIClient()
        response = self.client.get(reverse('Home/passengers/'))
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
