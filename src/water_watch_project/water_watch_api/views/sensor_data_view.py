from rest_framework import mixins, viewsets, status
from rest_framework.response import Response

from ..models import SensorData
from ..serializers import SensorDataListSerializer


class SensorDataViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):


    queryset = SensorData.objects.all()
    serializer_class = SensorDataListSerializer

    def create(self, request, *args, **kwargs):
        listOfSensorData = request.data

        serializer = self.get_serializer(data=listOfSensorData, many=True)
        if serializer.is_valid():
            serializer.save()
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED,
                            headers=headers)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)