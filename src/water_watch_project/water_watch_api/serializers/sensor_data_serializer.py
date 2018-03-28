from rest_framework import serializers
from ..models import SensorData


class SensorDataListSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        many = kwargs.pop('many', True)
        super(SensorDataListSerializer, self).__init__(many=many, *args, **kwargs)

    class Meta:
        model = SensorData
        fields = '__all__'
