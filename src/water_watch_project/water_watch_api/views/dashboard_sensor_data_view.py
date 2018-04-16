from ..models import SensorData, Station, Sensor, SensorType
from rest_framework.renderers import TemplateHTMLRenderer
from django_filters.views import FilterView
from django import forms
import django_filters as filters


class DashboardSensorDataFilter(filters.FilterSet):
    station = filters.ModelChoiceFilter(label="Station", name="sensor__station_id", queryset=Station.objects.filter(current_status='ACTIVE'),
                                      widget=forms.Select)
    start_date = filters.DateTimeFilter(label="Start Date", name="sensor_data_dateTime", lookup_expr='gte',
                                        widget=forms.DateTimeInput(attrs={'type': 'date'}))
    end_date = filters.DateTimeFilter(label="End Date", name="sensor_data_dateTime", lookup_expr='lte',
                                      widget=forms.DateTimeInput(attrs={'type': 'date'}))
    sensor_type = filters.ModelChoiceFilter(label="Sensor Type", name="sensor__sensor_type_id", queryset=SensorType.objects.all(),
                                          widget=forms.Select)


    class Meta:
        model = SensorData
        fields = ['start_date', 'end_date', 'station',
                  'sensor_type']


class DashboardSensorDataView(FilterView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'dashboard.html'
    filterset_class = DashboardSensorDataFilter
    context_object_name = 'sensor_data_list'
    paginate_by = 30
    model = SensorData