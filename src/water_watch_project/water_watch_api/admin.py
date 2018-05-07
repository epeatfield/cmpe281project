from django.contrib import admin
from rangefilter.filter import DateRangeFilter, DateTimeRangeFilter


from . import models

# Register your models here.


class StationAdmin(admin.ModelAdmin):

    actions = ['download_csv']
    list_filter = ['us_state_cd']
    list_display = ('id', 'station_name', 'us_state_cd', 'longitude', 'latitude', 'current_status')

    def download_csv(self, request, queryset):
        import csv
        from django.http import HttpResponse
        import io

        f = io.StringIO()
        writer = csv.writer(f)
        writer.writerow(["id", "station", "state", "longitude", "latitude", "current_status"])

        for s in queryset:
            writer.writerow([s.usgs_site_code, s.station_name, s.us_state_cd, s.longitude, s.latitude])

        f.seek(0)
        response = HttpResponse(f, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=station-type.csv'
        return response

    download_csv.short_description = "Download CSV file for selected stats."
    search_fields = ('id', 'station_name', 'us_state_cd',)
    list_per_page = 10


class SensorAdmin(admin.ModelAdmin):

    actions = ['download_csv']
    list_filter = ('current_status', 'station__station_name', 'sensor_type__sensor_type_name')
    list_display = ('id', 'station', 'sensor_type', 'current_status')

    def download_csv(self, request, queryset):
        import csv
        from django.http import HttpResponse
        import io

        f = io.StringIO()
        writer = csv.writer(f)
        writer.writerow(["id","station","sensor","status"])

        for s in queryset:
            writer.writerow([s.id, s.station, s.sensor_type, s.current_status])

        f.seek(0)
        response = HttpResponse(f, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=sensor.csv'
        return response

    download_csv.short_description = "Download CSV file for selected stats."
    search_fields = ('station__station_name', 'sensor_type__sensor_type_name','current_status',)
    list_per_page = 25

class SensorTypeAdmin(admin.ModelAdmin):

    actions = ['download_csv']
    list_display = ('id', 'sensor_type_name', 'description', 'unit')

    def download_csv(self, request, queryset):
        import csv
        from django.http import HttpResponse
        import io

        f = io.StringIO()
        writer = csv.writer(f)
        writer.writerow(["id","sensor","description","unit"])

        for s in queryset:
            writer.writerow([s.id, s.sensor_type_name, s.description, s.unit])

        f.seek(0)
        response = HttpResponse(f, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=sensor-type.csv'
        return response

    download_csv.short_description = "Download CSV file for selected stats."
    search_fields = ('sensor_type_name',)
    list_per_page = 20


class SensorDataAdmin(admin.ModelAdmin):

    actions = ['download_csv']
    list_display = ('id', 'sensor', 'sensor_data_dateTime', 'sensor_data_value')

    def download_csv(self, request, queryset):
        import csv
        from django.http import HttpResponse
        import io

        f = io.StringIO()
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
    list_per_page = 20


class SensorMaintenanceHistoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'sensor', 'dateTime', 'status')


admin.site.register(models.Station, StationAdmin)
admin.site.register(models.SensorType, SensorTypeAdmin)
admin.site.register(models.Sensor, SensorAdmin)
admin.site.register(models.SensorData, SensorDataAdmin)
admin.site.register(models.SensorMaintenanceHistory, SensorMaintenanceHistoryAdmin)
