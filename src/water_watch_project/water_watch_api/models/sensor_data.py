
from django.db import models
from . import Sensor


class SensorData(models.Model):

    class Meta:
        db_table = 'sensor_data'
        ordering = ['id', 'sensor_data_dateTime', 'sensor__station_id', 'sensor__sensor_type_id']
        verbose_name_plural = "sensor data"
        unique_together = (('sensor', 'sensor_data_dateTime'),)
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    sensor_data_dateTime = models.DateTimeField()
    sensor_data_value = models.DecimalField(max_digits=20, decimal_places=3)

    def __str__(self):
        return str(self.sensor) + '-' + str(self.sensor_data_value) + '-' + str(self.sensor_data_dateTime)
