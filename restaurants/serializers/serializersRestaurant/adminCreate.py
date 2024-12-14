from rest_framework import serializers
from restaurants.models import *
from users.models import UserModel


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



class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = '__all__'

    def __str__(self):
        return f"{self.name}, {self.role} "