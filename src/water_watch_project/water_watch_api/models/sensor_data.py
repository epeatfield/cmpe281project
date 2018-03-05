from django.db import models

from . import Sensor

class SensorData(models.Model):
    class Meta:
        db_table = 'sensor_data'
        #ordering = ['station_name']
