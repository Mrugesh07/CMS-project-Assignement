
# cms_app/views.py
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import ContentItem
from .serializers import ContentItemSerializer
# cms_app/tests.py
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User
from django.urls import reverse
from .models import ContentItem



class ContentItemViewSet(viewsets.ModelViewSet):
    queryset = ContentItem.objects.all()
    serializer_class = ContentItemSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
