from rest_framework import serializers
from ..models import Sensor
from ..models import SensorType
from ..models import Station

class SensorSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        many = kwargs.pop('many', True)
        super(SensorSerializer, self).__init__(many=many, *args, **kwargs)

    class Meta:
        model = Sensor
        fields = '__all__'
        depth = 2

class SensorCreateSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        many = kwargs.pop('many', True)
        super(SensorCreateSerializer, self).__init__(many=many, *args, **kwargs)

    class Meta:
        model = Sensor
        fields = '__all__'


class SensorRetrieveUpdateDestroySerializer(serializers.ModelSerializer):

    class Meta:
        model = Sensor
        fields = '__all__'
