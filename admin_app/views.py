from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import ManagerandCourierModel
from .permissions import IsRestaurantManager, IsCourier
from .serializers import RestaurantManagerSerializer


class RestaurantManagerView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    manager = ManagerandCourierModel.objects.all()
    serializer_class = RestaurantManagerSerializer
    def perform_create(self, serializer):
        manager = serializer.save()
        manager.set_password(serializer.validated_data['password'])
        manager.save()
        return manager

class CourierView(APIView):
    permission_classes = [IsCourier]

    def get(self, request):
        return Response({"message": "Hello, Courier!"})
