
from django.db import models
from . import Sensor


class SensorMaintenanceHistory(models.Model):

    class Meta:
        db_table = 'sensor_maintenance_history'
        ordering = ['id', 'dateTime']
        verbose_name_plural = "sensor maintenance history"

    ACTIVE = 'ACTIVE'
    INACTIVE = 'INACTIVE'
    MAINTENANCE = 'MAINTENANCE'
    STATUS_CHOICES = (
        (ACTIVE, 'active'),
        (INACTIVE, 'inactive'),
        (MAINTENANCE, 'maintenance'),
    )

    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    dateTime = models.DateTimeField()
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default=ACTIVE)

    def __str__(self):
        return str(self.sensor) + '-' + str(self.status) + '-' + str(self.dateTime)
