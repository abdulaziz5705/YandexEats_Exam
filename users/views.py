import threading

from django.shortcuts import get_object_or_404
from rest_framework import generics,  status
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from restaurants.models import RestaurantModel, CategoryMenuModel
from restaurants.serializers.serializersMenu.Menu import CategoryMenuSerializer
from restaurants.serializers.serializersRestaurant.adminCreate import RestaurantSerializer
from users.models import UserModel
from users.serializers import RegistrationSerializer, VerifyEmailSerializer, LoginSerializer, UserProfileSerializer, \
    ResendCodeSerializer, UserSerializer
from users.signals import sent_verification_email


class RegisterView(generics.CreateAPIView):
    user_model = UserModel.objects.all()
    serializer_class = RegistrationSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        user = serializer.save()
        # user.set_password(serializer.validated_data['password'])
        user.is_active = True
        user.save()
        return user

class VerifyEmailView(APIView):
    permission_classes = [AllowAny]
    serializer_class = VerifyEmailSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_code = serializer.validated_data['user_code']
        user = user_code.user

        user.is_active = True
        user.save()
        user_code.delete()
        response = {
            "status": True,
            "message": "Verification code has been sent.",
        }
        return Response(response, status=status.HTTP_200_OK)

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

class EmailCodeView(APIView):
    permission_classes = [AllowAny]
    serializer_class = ResendCodeSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']
        email_code = threading.Thread(target=sent_verification_email, args=(email,))
        email_code.start()
        response = {
            "status": True,
            "message": "Verification code has been sent for your email",
        }
        return Response(response, status=status.HTTP_200_OK)

class ProfileView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_classes = UserProfileSerializer

    def get(self, request):
        user = request.user
        serializer = self.serializer_classes(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request):
        user = get_object_or_404(UserModel, id=request.user.id)
        serializer = self.serializer_classes(instance=user,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request):
        user = get_object_or_404(UserModel, id=request.user.id)
        serializer = self.serializer_classes(instance=user,data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.validated_data, status=status.HTTP_200_OK)

    def delete(self, request):
        user = request.user
        user.delete()
        response = {
            "status": True,
            "message": "Your account has been deleted",
        }
        return Response(response,status=status.HTTP_204_NO_CONTENT)



class RestaurantView(APIView):
    permission_classes = [AllowAny]
    serializer_class = RestaurantSerializer
    def get(self, request):
        r = RestaurantModel.objects.all()
        serializer = RestaurantSerializer(r, many=True).data
        return Response(serializer, status=status.HTTP_200_OK)


class CategoryView(APIView):
    queryset = CategoryMenuModel.objects.all()
    permission_classes = [AllowAny]
    serializer_class = CategoryMenuSerializer
    def get(self, request):
        category = self.queryset.all()
        serializer = self.serializer_class(category, many=True).data
        return Response(serializer, status=status.HTTP_200_OK)


class AllUsersView(APIView):
    permission_classes = [AllowAny]
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    def get(self, request):
        users = self.queryset.all()
        serializer = self.serializer_class(users, many=True).data
        return Response(serializer, status=status.HTTP_200_OK)