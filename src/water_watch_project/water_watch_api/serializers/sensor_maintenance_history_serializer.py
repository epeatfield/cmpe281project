from rest_framework import serializers
from ..models import SensorMaintenanceHistory


class SensorMaintenanceHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorMaintenanceHistory
        fields = '__all__'