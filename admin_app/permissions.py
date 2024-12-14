# from rest_framework.permissions import BasePermission
#
# class IsRestaurantManager(BasePermission):
#     def has_permission(self, request, view):
#         return request.user.is_authenticated and request.user.role == 'manager'
#
#
# class IsCourier(BasePermission):
#     def has_permission(self, request, view):
#         return request.user  and request.user.is_staff
#
#
