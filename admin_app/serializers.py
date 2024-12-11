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



