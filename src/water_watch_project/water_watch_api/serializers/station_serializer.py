from rest_framework import serializers
from ..models import Station


class StationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = '__all__'
        depth = 2

class StationCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = '__all__'

class StationRetrieveUpdateDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = '__all__'


class StationSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = '__all__'
