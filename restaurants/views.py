from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import  status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from restaurants.models import RestaurantModel, CategoryMenuModel, MenuModel
from restaurants.serializers.serializersMenu.Menu import CategoryMenuSerializer, MenuSerializer
from restaurants.serializers.serializersRestaurant.adminCreate import RestaurantSerializer

## <<<<<<<RESTAURANT>>>>>>>

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


## <<<<<<<<<<<<<<CATEGORY>>>>>>>>>>>>>>>>


@method_decorator(csrf_exempt, name='dispatch')
class CategoryMenuView(APIView):
    permission_classes = [IsAuthenticated]
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
        permission_classes = [IsAuthenticated]
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
    permission_classes = [IsAuthenticated]
    serializer_class = MenuSerializer

    @swagger_auto_schema(
        operation_description="Get example endpoint",
        responses={200: 'Success!'},
    )

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
    permission_classes = [IsAuthenticated]
    serializer_class = MenuSerializer
    def get(self, request, pk):
        menu = get_object_or_404(MenuModel, pk=pk)
        serializer = MenuSerializer(menu, many=True).data
        return Response(serializer, status=status.HTTP_200_OK)

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