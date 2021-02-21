from rest_framework import serializers
from cdx.cars.models import Car


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('make', 'model', 'year')
        model = Car
