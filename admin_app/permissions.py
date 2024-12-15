from rest_framework.permissions import BasePermission
from users.models import UserRoleChoice

class IsRestaurantManager(BasePermission):
    """Permission restaurant yani restaurant manager ga tegishli bulgan api larni kura oladi oladi """
    def has_permission(self, request, view):
        return  request.user.role == UserRoleChoice.MANAGER


class IsCourier(BasePermission):
    """Courier permission uziga tegishli bulgan api larga ruxsat etish"""
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == UserRoleChoice.COURIER


