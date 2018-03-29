from rest_framework import generics

from ..models import SensorType
from ..serializers import SensorTypeSerializer


class SensorTypeListCreateView(generics.ListCreateAPIView):
    queryset = SensorType.objects.all()
    serializer_class = SensorTypeSerializer


class SensorTypeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SensorType.objects.all()
    serializer_class = SensorTypeSerializer

    #We do not have the need to BATCH INSERT sensor type objects, hence, no need to override create method

