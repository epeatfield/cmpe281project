from django.contrib import admin
from . import models
# Register your models here.


class StationAdmin(admin.ModelAdmin):
    list_filter = ['us_state_cd']
    list_display = ('station_name','us_state_cd','longitute','latitute')
class SensorAdmin(admin.ModelAdmin):
    list_filter = ('current_status', 'station__station_name', 'sensor_type__sensor_type_name')
    list_display = ('station', 'sensor_type', 'current_status')
class SensorTypeAdmin(admin.ModelAdmin):
    list_display = ('sensor_type_name', 'description', 'unit')

admin.site.register(models.Station, StationAdmin)
admin.site.register(models.SensorType, SensorTypeAdmin)
admin.site.register(models.Sensor, SensorAdmin)
