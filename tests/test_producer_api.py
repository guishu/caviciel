from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APIClient, APITransactionTestCase
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

from core.models import Producer


class TestProducerAPI(APITransactionTestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')

        token = RefreshToken.for_user(self.user).access_token
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")

    def test_create_producer_returns_201_with_proper_arguments(self):
        create_producer_url = reverse("producer-list")

        count = Producer.objects.count()

        response = self.client.post(create_producer_url, {"name": "test_name"}, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.post(create_producer_url, {"domain": "test_domain"}, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.post(create_producer_url, {"name": "test_name", "domain": "test_domain"}, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(Producer.objects.count(), count + 3)

    def test_create_producer_returns_400_without_proper_arguments(self):
        create_producer_url = reverse("producer-list")

        count = Producer.objects.count()

        response = self.client.post(create_producer_url, {"address": "test_address"}, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Producer.objects.count(), count)

    def test_create_producer_returns_409_on_duplicate_producer(self):
        create_producer_url = reverse("producer-list")

        count = Producer.objects.count()

        self.client.post(create_producer_url, {"name": "test_name"}, format="json")
        response = self.client.post(create_producer_url, {"name": "test_name"}, format="json")
        self.assertEqual(response.status_code, status.HTTP_409_CONFLICT)

        self.client.post(create_producer_url, {"domain": "test_domain"}, format="json")
        response = self.client.post(create_producer_url, {"domain": "test_domain"}, format="json")
        self.assertEqual(response.status_code, status.HTTP_409_CONFLICT)

        self.client.post(create_producer_url, {"name": "test_name", "domain": "test_domain"}, format="json")
        response = self.client.post(create_producer_url, {"name": "test_name", "domain": "test_domain"}, format="json")
        self.assertEqual(response.status_code, status.HTTP_409_CONFLICT)

        self.assertEqual(Producer.objects.count(), count + 3)
