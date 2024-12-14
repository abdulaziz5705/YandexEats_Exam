
from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from admin_app.permissions import IsCourier
from couriers.serializers import *
from users.models import UserModel


class ProfileView(APIView):
    queryset = UserModel.objects.filter(role='courier')
    serializer_class = CourierSerializer
    permission_classes = [IsCourier]

    def get(self, request):
        user = request.user
        serializer = self.serializer_class(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request):
        user = get_object_or_404(UserModel, id=request.user.id)
        serializer = self.serializer_class(instance=user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        responce = {
            "status": True,
            "message": "success patch",
        }
        return Response( serializer.validated_data, status=status.HTTP_200_OK)

    def delete(self, request):
        user = request.user
        user.delete()
        response = {
            "status": True,
            "message": "Your account has been deleted",
        }
        return Response(response, status=status.HTTP_204_NO_CONTENT)




