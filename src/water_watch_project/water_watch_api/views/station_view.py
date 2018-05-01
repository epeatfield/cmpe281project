from rest_framework import generics
from rest_framework import permissions as rest_framework_permissions
from .. import permissions as custom_permissions
from ..models import Station
from ..serializers import StationSerializer
from django_filters import rest_framework as filters

ACTIVE = 'ACTIVE'
INACTIVE = 'INACTIVE'
MAINTENANCE = 'MAINTENANCE'
STATUS_CHOICES = (
    (ACTIVE, 'active'),
    (INACTIVE, 'inactive'),
    (MAINTENANCE, 'maintenance'),
)


class StationFilter(filters.FilterSet):
    current_status = filters.MultipleChoiceFilter(choices=STATUS_CHOICES)

    class Meta:
        model = Station
        fields = ['current_status']

class StationListCreateView(generics.ListCreateAPIView):
    queryset = Station.objects.all()
    serializer_class = StationSerializer
    permission_classes = (rest_framework_permissions.IsAuthenticated, custom_permissions.IsAdminOrReadOnly)
    filter_class = StationFilter
    filter_backends = (filters.DjangoFilterBackend,)


class StationRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Station.objects.all()
    serializer_class = StationSerializer
    permission_classes = (rest_framework_permissions.IsAuthenticated, custom_permissions.IsAdminOrReadOnly)
