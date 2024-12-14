from rest_framework import serializers
from restaurants.models import MenuModel,CategoryMenuModel


class CategoryMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryMenuModel
        fields = '__all__'

    def create(self, validated_data):
        return CategoryMenuModel.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance





class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuModel
        fields = '__all__'


    def create(self, validated_data):
        return MenuModel.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance