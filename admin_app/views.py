from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from restaurants.models import RestaurantModel
from restaurants.serializers.serializersRestaurant.adminCreate import RestaurantSerializer
from users.models import *
from rest_framework import generics, status
from rest_framework.permissions import AllowAny,  IsAdminUser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import RestaurantManagerSerializer,  LoginManagerSerializer


class RestaurantManagerView(APIView):
    queryset = UserModel.objects.filter(role='manager')
    serializer_class = RestaurantManagerSerializer
    permission_classes = [IsAdminUser]
    def get(self, request):
        r = self.queryset.all()
        serializer = RestaurantManagerSerializer(r, many=True)
        return Response(serializer.data)




class CourierView(APIView):
    queryset = UserModel.objects.filter(role='courier')
    serializer_class = RestaurantManagerSerializer
    permission_classes = [IsAdminUser]

    def get(self, request):
        c  = self.queryset.all()
        serializer = self.serializer_class(c, many=True)
        return Response(serializer.data)



class UsersView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    manager = UserModel.objects.filter(role='manager, courier' )
    serializer_class = RestaurantManagerSerializer
    def perform_create(self, serializer):
        manager = serializer.save()
        manager.set_password(serializer.validated_data['password'])
        manager.save()
        return manager




class LoginView(APIView):
    serializer_class = LoginManagerSerializer
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




#<<<<<<<<<<<<<<<<Restaurant>>>>>>>>>>>>>>>>>

## <<<<<<<RESTAURANT>>>>>>>

@method_decorator(csrf_exempt, name='dispatch')
class CreateRestaurantView(APIView):
    serializer_class = RestaurantSerializer
    permission_classes = [IsAdminUser]

    def get(self, request):
        r = RestaurantModel.objects.all()
        serializer = RestaurantSerializer(r, many=True).data
        return Response(serializer, status=status.HTTP_200_OK)


    def post(self, request):
        serializer = RestaurantSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = {
            "status": True,
            "message": "Restaurant created",
            "data": serializer.data
        }
        return Response(response, status=status.HTTP_201_CREATED)


@method_decorator(csrf_exempt, name='dispatch')
class CRUDRestaurantView(APIView):
    serializer_class = RestaurantSerializer
    permission_classes = [IsAdminUser]

    def get(self, request, pk):
        try:
            r = RestaurantModel.objects.get(pk=pk)
        except RestaurantModel.DoesNotExist:
            return Response({"detail": "Restaurant not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = RestaurantSerializer(r)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        r = get_object_or_404(RestaurantModel, pk=pk)
        serializer = RestaurantSerializer(instance=r,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = {
            "status": True,
            "message": "Restaurant updated",
            "data": serializer.data
        }
        return Response(response, status=status.HTTP_200_OK)

    def patch(self, request, pk):
        r = get_object_or_404(RestaurantModel, pk=pk)
        serializer = RestaurantSerializer(instance=r,data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = {
            "status": True,
            "message": "Restaurant updated",
            "data": serializer.data
        }
        return Response(response, status=status.HTTP_200_OK)

    def delete(self, request, pk=None):
        r = get_object_or_404(RestaurantModel, pk=pk)
        r.delete()
        response = {
            "status": True,
            "message": "Restaurant deleted",
        }
        return Response(response, status=status.HTTP_200_OK)
