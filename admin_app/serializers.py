from django.contrib.auth import authenticate
from rest_framework import serializers

from admin_app.models import  ManagerandCourierModel


class RestaurantManagerSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=8,write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = ManagerandCourierModel
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
        manager = ManagerandCourierModel.objects.create(**validated_data)
        manager.set_password(validated_data['password'])
        manager.save()
        return manager


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=200)
    email = serializers.EmailField(max_length=200)
    password = serializers.CharField(max_length=100,write_only=True)
    errors = 'Email\ username or password errors'
    def validate(self, attrs):
        username = attrs.get('username')
        email = attrs.get('email')
        password = attrs.get('password')
        errors = attrs.get('errors')
        try:
            if email.endswith('@gmail.com'):
                user = ManagerandCourierModel.objects.get(email=email)
                print(user)
            else:
                user = ManagerandCourierModel.objects.get(username=username)
                print(user)
        except ManagerandCourierModel.DoesNotExist:
            raise serializers.ValidationError(errors)
        print(user)

        authenticated = authenticate(username=user.username, password=password)
        if not authenticated:
            raise serializers.ValidationError(errors)
        attrs['user'] = authenticated
        return attrs

