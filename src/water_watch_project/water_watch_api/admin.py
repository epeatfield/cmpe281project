from django.contrib import admin
from django.contrib.admin import DateFieldListFilter

from . import models
# Register your models here.


class StationAdmin(admin.ModelAdmin):

    list_filter = ['us_state_cd']
    list_display = ('id', 'station_name', 'us_state_cd', 'longitude', 'latitude')
    search_fields = ('id', 'station_name', 'us_state_cd',)


class SensorAdmin(admin.ModelAdmin):

    list_filter = ('current_status', 'station__station_name', 'sensor_type__sensor_type_name')
    list_display = ('id', 'station', 'sensor_type', 'current_status')
    search_fields = ('station__station_name', 'sensor_type__sensor_type_name','current_status',)


class SensorTypeAdmin(admin.ModelAdmin):

    list_display = ('id', 'sensor_type_name', 'description', 'unit')
    search_fields = ('sensor_type_name',)


class SensorDataAdmin(admin.ModelAdmin):

    list_display = ('id', 'sensor', 'sensor_data_dateTime', 'sensor_data_value')
    list_filter = ('sensor__station__station_name', 'sensor__sensor_type__sensor_type_name', ('sensor_data_dateTime', DateFieldListFilter),)
    search_fields = ('sensor__station__station_name', 'sensor_data_value','sensor__sensor_type__sensor_type_name')


admin.site.register(models.Station, StationAdmin)
admin.site.register(models.SensorType, SensorTypeAdmin)
admin.site.register(models.Sensor, SensorAdmin)
admin.site.register(models.SensorData, SensorDataAdmin)
