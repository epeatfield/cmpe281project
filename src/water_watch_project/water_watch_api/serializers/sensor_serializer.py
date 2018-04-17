from rest_framework import serializers
from ..models import Sensor
from ..models import SensorType
from ..models import Station

class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = '__all__'
        depth = 2

class SensorCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = '__all__'


class SensorRetrieveUpdateDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = '__all__'

class SensorSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = '__all__'
