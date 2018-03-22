from django.contrib import admin
#from django.contrib.admin import DateFieldListFilter
from django.contrib.admin import ModelAdmin
from rangefilter.filter import DateRangeFilter, DateTimeRangeFilter


from . import models

# Register your models here.


class StationAdmin(admin.ModelAdmin):

    list_filter = ['us_state_cd']
    list_display = ('id', 'station_name', 'us_state_cd', 'longitude', 'latitude')
    search_fields = ('id', 'station_name', 'us_state_cd',)
    list_per_page = 5

class SensorAdmin(admin.ModelAdmin):

    list_filter = ('current_status', 'station__station_name', 'sensor_type__sensor_type_name')
    list_display = ('id', 'station', 'sensor_type', 'current_status')
    search_fields = ('station__station_name', 'sensor_type__sensor_type_name','current_status',)
    list_per_page = 5

class SensorTypeAdmin(admin.ModelAdmin):

    list_display = ('id', 'sensor_type_name', 'description', 'unit')
    search_fields = ('sensor_type_name',)
    list_per_page = 5

class SensorDataAdmin(admin.ModelAdmin):

    actions = ['download_csv']
    list_display = ('id', 'sensor', 'sensor_data_dateTime', 'sensor_data_value')
    def download_csv(self, request, queryset):
        #None
        import csv
        from django.http import HttpResponse
        import StringIO

        f = StringIO.StringIO()
        writer = csv.writer(f)
        writer.writerow(["id","sensor","sensor date","sensor value"])

        for s in queryset:
            writer.writerow([s.id, s.sensor, s.sensor_data_dateTime, s.sensor_data_value])

        f.seek(0)
        response = HttpResponse(f, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=sensor-data.csv'
        return response

    download_csv.short_description = "Download CSV file for selected stats."
    list_filter = ('sensor__station__station_name', 'sensor__sensor_type__sensor_type_name', ('sensor_data_dateTime', DateTimeRangeFilter),)
    search_fields = ('sensor__station__station_name', 'sensor_data_value','sensor__sensor_type__sensor_type_name')
    list_per_page = 10

admin.site.register(models.Station, StationAdmin)
admin.site.register(models.SensorType, SensorTypeAdmin)
admin.site.register(models.Sensor, SensorAdmin)
admin.site.register(models.SensorData, SensorDataAdmin)
