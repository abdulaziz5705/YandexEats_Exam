from datetime import timezone, timedelta
from django.utils import timezone
from rest_framework import serializers
from users.models import UserModel, VerificationModel


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['id','first_name','email',]
        username_field = 'email'
        extra_kwargs = {
            'password': {'write_only': True},
            'first_name': {'write_only': True},
            'last_name': {'write_only': True},
            'username': {'write_only': True},

                }


    def validate_email(self, email):
        if not email.endswith('@gmail.com') or  email.endswith('@mail.com') or email.count('@') != 1:
            raise serializers.ValidationError('Email must end with @gmail.com')
        return email


    def create(self, validated_data):
        validated_data['username']  = validated_data.pop('first_name')
        user = UserModel.objects.create_user(**validated_data)
        user.save()
        return user

class VerifyEmailSerializer(serializers.Serializer):
    email = serializers.EmailField()
    code = serializers.CharField(write_only=True)
    class Meta:
        model = UserModel
        fields = ['email', 'code']

    def validate(self, attrs):
        try:
            user = UserModel.objects.get(email=attrs['email'])
            user_code = VerificationModel.objects.get(code=attrs['code'])
        except VerificationModel.DoesNotExist:
            raise serializers.ValidationError('Verification code does not exist')

        current_time = timezone.now()
        if user_code.created_at +timedelta(minutes=2) < current_time:
            user_code.delete()
            raise serializers.ValidationError('Gmail or code errors try again')

        attrs['user_code'] = user_code
        return attrs


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate(self, attrs):
        email = attrs.get('email')


        if not email:
            raise serializers.ValidationError('Email is required')


        try:
            user = UserModel.objects.get(email=email)
        except UserModel.DoesNotExist:
            raise serializers.ValidationError('User with this email does not exist')

        attrs['user'] = user
        return attrs


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['id', 'username', 'email', 'first_name', 'last_name']
        extra_kwargs = {
            'password': {'write_only': True},
        }

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        exclude = ['password']
        extra_kwargs = {
            'last_login': {'read_only': True},
            'date_joined': {'read_only': True},
            'is_active': {'read_only': True},
            'is_staff': {'read_only': True},
        }


class ResendCodeSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate(self, attrs):
        email = attrs.get('email')
        try:
            user = UserModel.objects.get(email=email, is_active=True)
        except UserModel.DoesNotExist:
            raise serializers.ValidationError('Email is error')

        user_code = VerificationModel.objects.filter(user__email=email)
        if user_code:
            current_time = timezone.now()
            if user_code.created_at + timedelta(minutes=2) > current_time:
                raise serializers.ValidationError('You have already active code')
        attrs['user'] = user
        return attrs