from django.db import models


class StationManager(models.Manager):
    def get_by_natural_key(self, station_name):
        return self.get(station_name=station_name)


class Station(models.Model):

    class Meta:
        db_table = 'station'
        ordering = ['id', 'station_name']
    objects = StationManager()
    usgs_site_code = models.CharField(max_length=20)
    station_name = models.CharField(max_length=255, unique=True)
    us_state_cd = models.CharField(max_length=2)
    longitude = models.DecimalField(max_digits=7, decimal_places=3)
    latitude = models.DecimalField(max_digits=7, decimal_places=3)

    REQUIRED_FIELDS = ('station_name', 'us_state_cd', 'longitude', 'latitude')

    def __str__(self):
        return self.station_name
    def natural_key(self):
        return self.station_name
