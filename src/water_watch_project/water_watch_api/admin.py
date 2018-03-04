from django.contrib import admin
from . import models
# Register your models here.


class StationAdmin(admin.ModelAdmin):
    list_filter = ['us_state_cd']
    list_display = ('station_name','us_state_cd','longitute','latitute')

admin.site.register(models.Station, StationAdmin)
