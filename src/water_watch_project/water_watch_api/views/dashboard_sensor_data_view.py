# from ..models import SensorData
# from rest_framework.renderers import TemplateHTMLRenderer
# from django_filters.views import FilterView
# from django import forms
# import django_filters as filters


# class StationMapFilter(filters.FilterSet):
#     # current_status = django_filters.MultipleChoiceFilter(choices=STATUS_CHOICES, widget=forms.CheckboxSelectMultiple)
#
#     min_value = filters.NumberFilter(name="sensor_data_value", lookup_expr='gte', widget=forms.NumberInput)
#     max_value = filters.NumberFilter(name="sensor_data_value", lookup_expr='lte', widget=forms.NumberInput)
#     sensor_id = filters.NumberFilter(name="sensor_id", widget=forms.NumberInput)
#     start_date = filters.DateTimeFilter(name="sensor_data_dateTime", lookup_expr='gte')
#     end_date = filters.DateTimeFilter(name="sensor_data_dateTime", lookup_expr='lte')
#
#     class Meta:
#         model = SensorData
#         fields = ['min_value', 'max_value','sensor_id','start_date','end_date']
#
#     class Meta:
#         model = SensorData
#         fields = ['current_status', 'longitude', 'latitude']
