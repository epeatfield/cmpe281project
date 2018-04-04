from django.db import models
from . import Station
from . import SensorType


class SensorManager(models.Manager):
    def get_by_natural_key(self, station, sensor_type):
        return self.get(staion=Station.objects.get_by_natural_key(station), sensor_type=SensorType.objects.get_by_natural_key(sensor_type))


class Sensor(models.Model):
    class Meta:
        db_table = 'sensor'
        unique_together = (('station', 'sensor_type'),)

    objects = SensorManager()
    ACTIVE = 'ACTIVE'
    INACTIVE = 'INACTIVE'
    MAINTENANCE = 'MAINTENANCE'
    STATUS_CHOICES = (
        (ACTIVE, 'active'),
        (INACTIVE, 'inactive'),
        (MAINTENANCE, 'maintenance'),
    )
    station = models.ForeignKey(Station, on_delete=models.CASCADE)
    sensor_type = models.ForeignKey(SensorType, on_delete=models.CASCADE)
    current_status = models.CharField(max_length=15, choices=STATUS_CHOICES, default=ACTIVE)

    def __str__(self):

        return self.station.natural_key() + '-' + self.sensor_type.natural_key()


    def natural_key(self):

        return [self.station.natural_key(), self.sensor_type.natural_key()]

    natural_key.dependencies = ['water_watch_api.station', 'water_watch_api.sensor_type']
