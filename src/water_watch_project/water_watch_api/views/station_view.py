#TODO Uttara please add the api to update/add/delete a station, get a single station,
# TODO retrieve a list of staion search by station name and location
#TODO Uttara please add the api to update/add/delete a sensor, get a single sensor, retrieve a list of sensor search by sensor type and staion

from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import permissions as rest_framework_permissions
from .. import permissions as custom_permissions
from ..models import Station
from ..serializers import StationSerializer


class StationListCreateView(generics.ListCreateAPIView):
    queryset = Station.objects.all()
    serializer_class = StationSerializer
    permission_classes = (rest_framework_permissions.IsAuthenticated, custom_permissions.IsAdminOrReadOnly)


class StationRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Station.objects.all()
    serializer_class = StationSerializer
    permission_classes = (rest_framework_permissions.IsAuthenticated, custom_permissions.IsAdminOrReadOnly)

class StationSearchView(generics.ListCreateAPIView):
    queryset = Station.objects.all()
    serializer_class = StationSerializer
    permission_classes = (rest_framework_permissions.IsAuthenticated, custom_permissions.IsAdminOrReadOnly)
