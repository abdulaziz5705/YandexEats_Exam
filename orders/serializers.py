from rest_framework import serializers
from orders.models import OrderFromUser, Courier


class CourierSerializer(serializers.ModelSerializer):

    class Meta:
        model = Courier
        fields = ['id', 'user', 'vehicle_type', 'is_active']

    def validate_user(self, value):
        if value.role != 'courier':
            raise serializers.ValidationError("The user must have the role 'courier' to be assigned as a courier.")
        return value



class OrderUserSerializer(serializers.ModelSerializer):
    courier = CourierSerializer(read_only=True)
    class Meta:
        model = OrderFromUser
        fields = ['id', 'user', 'courier', 'product', 'status', 'created_time']
        read_only_fields = ['created_time']

