from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken


from .models import ManagerandCourierModel
from .permissions import IsCourier, IsRestaurantManager
from .serializers import RestaurantManagerSerializer, LoginSerializer


class RestaurantManagerView(APIView):
    permission_classes = [IsRestaurantManager]
    def get(self, request):
        return Response({"message": "Restaurant Manager"})

class CourierView(APIView):
    permission_classes = [IsCourier]

    def get(self, request):
        return Response({"message": "Hello, Courier!"})


class UsersView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    manager = ManagerandCourierModel.objects.all()
    serializer_class = RestaurantManagerSerializer
    def perform_create(self, serializer):
        manager = serializer.save()
        manager.set_password(serializer.validated_data['password'])
        manager.save()
        return manager




class LoginView(APIView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        refresh = RefreshToken.for_user(serializer.validated_data['user'])
        response = {
            "access_token": str(refresh.access_token),
            "refresh_token": str(refresh)
        }
        return Response(response, status=status.HTTP_200_OK)
