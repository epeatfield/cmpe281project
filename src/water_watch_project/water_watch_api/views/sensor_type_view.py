from rest_framework import generics
from rest_framework import permissions as rest_framework_permissions
from .. import permissions as custom_permissions
from ..models import SensorType
from ..serializers import SensorTypeSerializer


class SensorTypeListCreateView(generics.ListCreateAPIView):
    queryset = SensorType.objects.all()
    serializer_class = SensorTypeSerializer
    permission_classes = (rest_framework_permissions.IsAuthenticated, custom_permissions.IsAdminOrReadOnly)


class SensorTypeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SensorType.objects.all()
    serializer_class = SensorTypeSerializer
    permission_classes = (rest_framework_permissions.IsAuthenticated, custom_permissions.IsAdminOrReadOnly)

    #We do not have the need to BATCH INSERT sensor type objects, hence, no need to override create method
