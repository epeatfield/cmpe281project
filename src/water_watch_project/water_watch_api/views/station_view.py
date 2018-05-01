from rest_framework import generics
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
