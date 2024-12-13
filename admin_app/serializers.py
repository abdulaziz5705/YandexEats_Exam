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


# class LoginSerializer(serializers.Serializer):
#     email_or_username = serializers.CharField(max_length=255)
#     password = serializers.CharField(max_length=100,write_only=True)
#     errors = 'Email\ username or password errors'
#     def validate(self, attrs):
#         email_or_username = attrs.get('email_or_username')
#         print(email_or_username)
#         password = attrs.get('password')
#         errors = attrs.get('errors')
#         try:
#             if email_or_username.endswith('@gmail.com'):
#                 user = ManagerandCourierModel.objects.get(email=email_or_username)
#                 print("email: ",user)
#             else:
#                 user = ManagerandCourierModel.objects.get(username=email_or_username)
#                 print("username: ",user)
#         except ManagerandCourierModel.DoesNotExist:
#             raise serializers.ValidationError(errors)
#         print(user)
#
#         authenticated = authenticate(username=user.username, password=password)
#         if not authenticated:
#             raise serializers.ValidationError(errors)
#         attrs['user'] = authenticated
#         return attrs


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=100, write_only=True)

    def validate(self, attrs):
        username = attrs.get('username')


        if not username:
            raise serializers.ValidationError('Username is required')


        try:
            user = ManagerandCourierModel.objects.get(username=username)
        except ManagerandCourierModel.DoesNotExist:
            raise serializers.ValidationError('User with this username does not exist')

        attrs['user'] = user
        return attrs