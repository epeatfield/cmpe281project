from rest_framework import status, generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from django_filters import rest_framework as filters
from rest_framework import permissions as rest_framework_permissions
from .. import permissions as custom_permissions

from ..models import SensorData
from ..serializers import SensorDataSerializer, SensorDataCreateSerializer


class SensorDataFilter(filters.FilterSet):
    #TODO add more filter we need for searching a list of sensor data
    min_value = filters.NumberFilter(name="sensor_data_value", lookup_expr='gte')
    max_value = filters.NumberFilter(name="sensor_data_value", lookup_expr='lte')

    class Meta:
        model = SensorData
        fields = ['min_value', 'max_value']


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000


class SensorDataListCreateView(generics.ListCreateAPIView):
    queryset = SensorData.objects.all()
    serializer_class = SensorDataSerializer
    filter_class = SensorDataFilter
    filter_backends = (filters.DjangoFilterBackend,)
    pagination_class = StandardResultsSetPagination
    permission_classes = (rest_framework_permissions.IsAuthenticated, custom_permissions.IsAdminOrReadOnly)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return SensorDataCreateSerializer
        return SensorDataSerializer

    def create(self, request, *args, **kwargs):
        '''This method is overriden the create method to
        implement a POST request to BATCH INSERT multiple sensor data objects.'''

        list_of_sensor_data = request.data
        serializer = SensorDataCreateSerializer(data=list_of_sensor_data, many=True)
        many = isinstance(list_of_sensor_data, list)
        print (list_of_sensor_data, many)
        if serializer.is_valid():
            serializer.save()
            headers = self.get_success_headers(serializer.data)
            return Response(dict(enumerate(serializer.data)), status=status.HTTP_201_CREATED,
                            headers=headers)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




    # #TODO Emma - add functons to update or partial-update by pk, destroy by pk => please create new simple serializer
    # TODO list (search),this is an example of how we filter sensor data by value range
    #  MOST IMPORTANT FOR NEXT STEPS: TODO list (search) filtered by time range, by station and by sensor type with pagination






