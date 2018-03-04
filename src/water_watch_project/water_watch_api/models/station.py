from django.db import models


class Station(models.Model):
    class Meta:
        db_table = 'station'
        ordering = ['station_name']
    usgs_site_code = models.CharField(max_length=20)
    station_name = models.CharField(max_length=255, unique=True)
    us_state_cd = models.CharField(max_length=2)
    longitute = models.DecimalField(max_digits=7, decimal_places=3)
    latitute = models.DecimalField(max_digits=7, decimal_places=3)

    REQUIRED_FIELDS = ('station_name', 'us_state_cd', 'longitute', 'latitute')
    def __str__(self):
        return self.station_name
