from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets, permissions
from .models import Itinerary
from . import serializers
from .permissions import ReadOnly

class UserViewSet(viewsets.ModelViewSet):
    """
    Provides basic CRUD functions for the User model
    """
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = (ReadOnly, )

class ItineraryViewSet(viewsets.ModelViewSet):
    """
    Provides basic CRUD functions for the Itinerary model
    """
    queryset = Itinerary.objects.all()
    serializer_class = serializers.ItinerarySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
