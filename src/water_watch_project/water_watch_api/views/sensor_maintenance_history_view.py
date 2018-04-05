from rest_framework import generics
from rest_framework import permissions as rest_framework_permissions
from .. import permissions as custom_permissions
from ..models import SensorMaintenanceHistory
from ..serializers import SensorMaintenanceHistorySerializer


class SensorMaintenanceHistoryListCreateView(generics.ListCreateAPIView):
    queryset = SensorMaintenanceHistory.objects.all()
    serializer_class = SensorMaintenanceHistorySerializer
    permission_classes = (rest_framework_permissions.IsAuthenticated, custom_permissions.IsAdminOrReadOnly)


class SensorMaintenanceHistoryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SensorMaintenanceHistory.objects.all()
    serializer_class = SensorMaintenanceHistorySerializer
    permission_classes = (rest_framework_permissions.IsAuthenticated, custom_permissions.IsAdminOrReadOnly)