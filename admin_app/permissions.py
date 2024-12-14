from rest_framework.permissions import BasePermission
from users.models import UserRoleChoice

class IsRestaurantManager(BasePermission):
    def has_permission(self, request, view):
        return  request.user.role == UserRoleChoice.MANAGER


class IsCourier(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == UserRoleChoice.COURIER


