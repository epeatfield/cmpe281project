from rest_framework import generics
from rest_framework import permissions as rest_framework_permissions
from .. import permissions as custom_permissions
from ..models import Sensor

from ..serializers import SensorSerializer, SensorDataRetrieveUpdateDestroySerializer


class SensorListCreateView(generics.ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
    permission_classes = (rest_framework_permissions.IsAuthenticated, custom_permissions.IsAdminOrReadOnly)


class SensorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDataRetrieveUpdateDestroySerializer
    permission_classes = (rest_framework_permissions.IsAuthenticated, custom_permissions.IsAdminOrReadOnly)

