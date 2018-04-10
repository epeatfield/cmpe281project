from rest_framework import serializers
from ..models import Station


class StationSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        many = kwargs.pop('many', True)
        super(StationSerializer, self).__init__(many=many, *args, **kwargs)

    class Meta:
        model = Station
        fields = '__all__'
        depth = 2

class StationCreateSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        many = kwargs.pop('many', True)
        super(StationCreateSerializer, self).__init__(many=many, *args, **kwargs)

    class Meta:
        model = Station
        fields = '__all__'

class StationRetrieveUpdateDestroySerializer(serializers.ModelSerializer):

    class Meta:
        model = Station
        fields = '__all__'
