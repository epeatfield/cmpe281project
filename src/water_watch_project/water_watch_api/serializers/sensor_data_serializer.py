from rest_framework import serializers
from ..models import SensorData


class SensorDataSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        many = kwargs.pop('many', True)
        super(SensorDataSerializer, self).__init__(many=many, *args, **kwargs)

    class Meta:
        model = SensorData
        fields = '__all__'
