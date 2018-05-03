from django.db import models
from django.contrib.gis.db import models as gis_models
from django.contrib.gis import geos

class StationManager(models.Manager):
    def get_by_natural_key(self, station_name):
        return self.get(station_name=station_name)


class Station(models.Model):

    class Meta:
        db_table = 'station'
        ordering = ['id', 'station_name']
    objects = StationManager()
    ACTIVE = 'ACTIVE'
    INACTIVE = 'INACTIVE'
    MAINTENANCE = 'MAINTENANCE'
    STATUS_CHOICES = (
        (ACTIVE, 'active'),
        (INACTIVE, 'inactive'),
        (MAINTENANCE, 'maintenance'),
    )
    usgs_site_code = models.CharField(max_length=20)
    station_name = models.CharField(max_length=255, unique=True)
    station_short_name = models.CharField(max_length=255, null=True)
    us_state_cd = models.CharField(max_length=2)
    longitude = models.DecimalField(max_digits=15, decimal_places=12)
    latitude = models.DecimalField(max_digits=15, decimal_places=12)
    current_status = models.CharField(max_length=15, choices=STATUS_CHOICES, default=ACTIVE)
    location = gis_models.PointField(u"longitude/latitude",
                                     geography=True, blank=True, null=True)

    gis = gis_models.GeoManager()

    REQUIRED_FIELDS = ('station_name', 'us_state_cd', 'longitude', 'latitude')

    def __str__(self):
        if self.station_short_name:
            return self.station_short_name
        else:
            return self.station_name

    def natural_key(self):
        return self.station_name

    def save(self, **kwargs):
        print('save is called')

        print('update location')
        point = "POINT(%s %s)" % (self.longitude, self.latitude)
        self.location = geos.fromstr(point)
        super(Station, self).save()

    def get_sensor_data_set(self):
        print("Debug");
        print (self.sensor_set.all());
        return self.sensor_set.all();