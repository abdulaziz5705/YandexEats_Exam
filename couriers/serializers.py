from rest_framework import serializers
from users.models import UserModel

class CourierSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = '__all__'

    def __str__(self):
        return f"{self.name}, {self.role} "