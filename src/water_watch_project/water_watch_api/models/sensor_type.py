from django.db import models


class SensorTypeManager(models.Manager):

    def get_by_natural_key(self, sensor_type_name):

        return self.get(sensor_type_name=sensor_type_name)


class SensorType(models.Model):

    class Meta:
        db_table = 'sensor_type'
        ordering = ['sensor_type_name']
    objects = SensorTypeManager()
    usgs_sensor_type_code = models.CharField(max_length=20, default="00000000")
    sensor_type_name = models.CharField(max_length=255, unique=True)
    description = models.CharField(max_length=255)
    unit = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.sensor_type_name

    def natural_key(self):
        return self.sensor_type_name
