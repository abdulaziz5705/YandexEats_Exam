from rest_framework import serializers
from restaurants.models import *


class RestaurantSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False)
    class Meta:
        model = RestaurantModel
        fields = '__all__'
        read_only_fields = ['id']

    def create(self, validated_data):
        return RestaurantModel.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
