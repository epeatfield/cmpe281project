from rest_framework import generics
from rest_framework import permissions as rest_framework_permissions
from django_filters import rest_framework as filters
from .. import permissions as custom_permissions
from ..models import Sensor

from ..serializers import SensorSerializer, SensorDataRetrieveUpdateDestroySerializer


class SensorFilter(filters.FilterSet):
    station_id = filters.NumberFilter(name="station__id",)
    sensor_type_id = filters.NumberFilter(name="sensor_type__id")

    class Meta:
        model = Sensor
        fields = ['station_id', 'sensor_type_id']

class SensorListCreateView(generics.ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
    permission_classes = (rest_framework_permissions.IsAuthenticated, custom_permissions.IsAdminOrReadOnly)
    filter_class = SensorFilter
    filter_backends = (filters.DjangoFilterBackend,)


class SensorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDataRetrieveUpdateDestroySerializer
    permission_classes = (rest_framework_permissions.IsAuthenticated, custom_permissions.IsAdminOrReadOnly)

