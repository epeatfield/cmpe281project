#TODO Uttara please add the api to update/add/delete a sensor, get a single sensor, retrieve a list of sensor search by sensor type and staion

from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions as rest_framework_permissions
from .. import permissions as custom_permissions
from ..models import Sensor
from ..models import Station
from ..models import SensorType
from ..serializers import SensorSerializer
from ..serializers import StationSerializer
from ..serializers import SensorTypeSerializer


class SensorListCreateView(generics.ListCreateAPIView):
    queryset=[{'queryset': Sensor.objects.all(), 'serializer_class': SensorSerializer},{'queryset': SensorType.objects.all(), 'serializer_class': SensorTypeSerializer},{'queryset': Station.objects.all(), 'serializer_class': StationSerializer}]
    serializer_class = SensorSerializer
    permission_classes = (rest_framework_permissions.IsAuthenticated, custom_permissions.IsAdminOrReadOnly)


class SensorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset=[{'queryset': Sensor.objects.all(), 'serializer_class': SensorSerializer},{'queryset': SensorType.objects.all(), 'serializer_class': SensorTypeSerializer},{'queryset': Station.objects.all(), 'serializer_class': StationSerializer}]
    serializer_class = SensorSerializer
    permission_classes = (rest_framework_permissions.IsAuthenticated, custom_permissions.IsAdminOrReadOnly)
