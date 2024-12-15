from rest_framework import serializers
from users.models import *


class RestaurantManagerSerializer(serializers.ModelSerializer):
    """Registrator serializer yani admin tomonidan restaurant manager va
    courierga username va password yaratish """
    password = serializers.CharField(max_length=8,write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = UserModel
        fields = '__all__'

    def validate(self, attrs):
        password = attrs.get('password')
        confirm_password = attrs.get('confirm_password')
        if password != confirm_password:
            raise serializers.ValidationError('Passwords must match')
        return attrs

    def validate_email(self, email):
        if not email.endswith('@gmail.com') or  email.endswith('@mail.com'):
            raise serializers.ValidationError('Email must end with @gmail.com')
        return email

    def create(self, validated_data):
        validated_data.pop('confirm_password')
        manager = UserModel.objects.create(**validated_data)
        manager.set_password(validated_data['password'])
        manager.save()
        return manager



class LoginManagerSerializer(serializers.Serializer):
    """Berilgan username bilan login qilish """
    username = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=100, write_only=True)

    def validate(self, attrs):
        username = attrs.get('username')


        if not username:
            raise serializers.ValidationError('Username is required')


        try:
            user = UserModel.objects.get(username=username)
        except UserModel.DoesNotExist:
            raise serializers.ValidationError('User with this username does not exist')

        attrs['user'] = user
        return attrs