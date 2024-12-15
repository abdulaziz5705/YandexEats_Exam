from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import  status
from rest_framework.response import Response
from rest_framework.views import APIView

from restaurants.models import  CategoryMenuModel, MenuModel
from restaurants.serializers.serializersMenu.Menu import CategoryMenuSerializer, MenuSerializer
from admin_app.permissions import IsRestaurantManager
from users.models import UserModel
from restaurants.serializers.serializersRestaurant.adminCreate import ManagerSerializer

#<<<Profile>>>>

class ManagerProfile(APIView):

    queryset = UserModel.objects.filter(role='manager')
    serializer_class = ManagerSerializer
    permission_classes = [IsRestaurantManager]

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
        return Response(serializer.validated_data, status=status.HTTP_200_OK)

    def delete(self, request):
        user = request.user
        user.delete()
        response = {
            "status": True,
            "message": "Your account has been deleted",
        }
        return Response(response, status=status.HTTP_204_NO_CONTENT)


## <<<<<<<<<<<<<<CATEGORY>>>>>>>>>>>>>>>>


@method_decorator(csrf_exempt, name='dispatch')
class CategoryMenuView(APIView):
    permission_classes = [IsRestaurantManager]
    def get(self, request):
        category = CategoryMenuModel.objects.all()
        serializer = CategoryMenuSerializer(category, many=True).data
        return Response(serializer, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CategoryMenuSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@method_decorator(csrf_exempt, name='dispatch')
class CategoryMenuCRUDView(APIView):
        permission_classes = [IsRestaurantManager]
        def get(self, request, pk):
            try:
                r = CategoryMenuModel.objects.get(pk=pk)
            except CategoryMenuModel.DoesNotExist:
                return Response({"detail": "Restaurant not found."}, status=status.HTTP_404_NOT_FOUND)

            serializer = CategoryMenuSerializer(r)
            return Response(serializer.data, status=status.HTTP_200_OK)

        def put(self, request, pk):
            category = get_object_or_404(CategoryMenuModel,pk=pk)
            serializer = CategoryMenuSerializer(instance=category,data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        def patch(self, request, pk):
            category = get_object_or_404(CategoryMenuModel,pk=pk)
            serializer = CategoryMenuSerializer(instance=category,data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        def delete(self, request, pk):
            category = get_object_or_404(CategoryMenuModel,pk=pk)
            category.delete()
            response = {
                "status": "success",
                "message": "Category deleted successfully"
            }
            return Response(response,status=status.HTTP_204_NO_CONTENT)



## <<<<<<<<<<<<<<<MENU>>>>>>>>>>>>>>>>>>>>>>

class CreateMenuView(APIView):
    permission_classes = [IsRestaurantManager]
    serializer_class = MenuSerializer

    def get(self, request):
        menu = MenuModel.objects.all()
        serializer = MenuSerializer(menu, many=True).data
        return Response(serializer, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = MenuSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = {
            "status": True,
            "message": "Menu created",
        }
        return Response(response, status=status.HTTP_201_CREATED)

class MenuCRUDView(APIView):
    permission_classes = [IsRestaurantManager]

    def get(self, request, pk):
        try:
            r = MenuModel.objects.get(pk=pk)
        except MenuModel.DoesNotExist:
            return Response({"detail": "Menu not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = MenuSerializer(r)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        menu = get_object_or_404(MenuModel, pk=pk)
        serializer = MenuSerializer(instance=menu, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, pk):
        menu = get_object_or_404(MenuModel, pk=pk)
        serializer = MenuSerializer(instance=menu, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        menu = get_object_or_404(MenuModel, pk=pk)
        menu.delete()
        response = {
            "status": True,
            "message": "Menu deleted successfully"
        }
        return Response(response, status=status.HTTP_204_NO_CONTENT)