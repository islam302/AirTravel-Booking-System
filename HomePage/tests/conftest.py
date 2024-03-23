from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from rest_framework import status
from model_bakery import baker
from rest_framework.test import APIClient
import pytest


UserModel = get_user_model()
@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def authenticated_user(api_client):
    user = UserModel.objects.create()
    refresh = RefreshToken.for_user(user)
    access_token = str(refresh.access_token)
    user.access_token = access_token
    return user

@pytest.fixture
def test_authenticated_user(api_client, authenticated_user):
    client = api_client
    client.force_authenticate(user=authenticated_user)
    response = client.post('auth/jwt/create/')

    assert response.status_code == status.HTTP_200_OK

