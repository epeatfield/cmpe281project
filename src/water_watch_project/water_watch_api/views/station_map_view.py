from ..models import Station
from rest_framework.renderers import TemplateHTMLRenderer
from django_filters.views import FilterView
from django import forms
import django_filters
from django.contrib.gis import geos
from django.contrib.gis import measure




ACTIVE = 'ACTIVE'
INACTIVE = 'INACTIVE'
MAINTENANCE = 'MAINTENANCE'
STATUS_CHOICES = (
    (ACTIVE, 'active'),
    (INACTIVE, 'inactive'),
    (MAINTENANCE, 'maintenance'),
)





class StationMapFilter(django_filters.FilterSet):
    current_status = django_filters.MultipleChoiceFilter(choices=STATUS_CHOICES, widget=forms.CheckboxSelectMultiple)
    longitude = django_filters.NumberFilter(widget=forms.NumberInput)
    latitude = django_filters.NumberFilter(widget=forms.NumberInput)

    class Meta:
        model = Station
        fields = ['current_status', 'longitude', 'latitude']


class StationMapView(FilterView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'station_map.html'
    filterset_class = StationMapFilter
    context_object_name = 'stations'
    model = Station


    def get_queryset(self, *args, **kwargs):
        query = Station.objects.all()
        if self.kwargs:
            if self.kwargs['current_status']:
                query = Station.objects.filter(category=self.kwargs['current_status'])

            if self.kwargs['longitude'] and self.kwargs['latitude']:
                longitude = self.kwargs['longitude']
                latitude = self.kwargs['longitude']
                current_point = geos.fromstr("POINT(%s %s)" % (longitude, latitude))
                distance_from_point = {'km': 10}
                query = query.gis.filter(location__distance_lte=(current_point, measure.D(**distance_from_point)))
                query = query.distance(current_point).order_by('distance')
        return query
