# cms_app/tests.py
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User
from django.urls import reverse
from .models import ContentItem
from django.urls import reverse

def test_content_item_create_authenticated(self):
    self.client.force_authenticate(user=self.user)
    url = reverse('contentitem-list')  # Assuming 'contentitem-list' is the automatically generated URL for listing content items
    response = self.client.post(url, self.content_item_data, format='json')
    print(response.status_code)
    print(response.data)
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)
