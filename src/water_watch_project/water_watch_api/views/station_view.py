#TODO Uttara please add the api to update/add/delete a station, get a single station,
# TODO retrieve a list of staion search by station name and location
#TODO Uttara please add the api to update/add/delete a sensor, get a single sensor, retrieve a list of sensor search by sensor type and staion

from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import permissions as rest_framework_permissions
from .. import permissions as custom_permissions
from ..models import Station
from ..serializers import StationSerializer


class StationListCreateView(generics.ListCreateAPIView):
    serializer_class = StationSerializer
    permission_classes = (rest_framework_permissions.IsAuthenticated, custom_permissions.IsAdminOrReadOnly)

    def get_queryset(self, *args, **kwargs):
        queryset = Station.objects.all()
        pass
        # if self.kwargs:
        #     if self.kwargs['current_status']:
        #         query = Station.objects.filter(category=self.kwargs['current_status'])
        #
        #     if self.kwargs['longitude'] and self.kwargs['latitude']:
        #         longitude = self.kwargs['longitude']
        #         latitude = self.kwargs['longitude']
        #         current_point = geos.fromstr("POINT(%s %s)" % (longitude, latitude))
        #         distance_from_point = {'km': 10}
        #         query = query.gis.filter(location__distance_lte=(current_point, measure.D(**distance_from_point)))
        #         query = query.distance(current_point).order_by('distance')
        # return query



class StationRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Station.objects.all()
    serializer_class = StationSerializer
    permission_classes = (rest_framework_permissions.IsAuthenticated, custom_permissions.IsAdminOrReadOnly)


class StationSearchView(generics.ListCreateAPIView):
    queryset = Station.objects.all()
    serializer_class = StationSerializer
    permission_classes = (rest_framework_permissions.IsAuthenticated, custom_permissions.IsAdminOrReadOnly)
