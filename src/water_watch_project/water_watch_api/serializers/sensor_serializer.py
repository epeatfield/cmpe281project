from rest_framework import serializers
from ..models import Sensor


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = '__all__'
        depth = 1


class SensorRetrieveUpdateDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = '__all__'
