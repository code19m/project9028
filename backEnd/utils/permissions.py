from rest_framework.permissions import BasePermission, SAFE_METHODS

from apps.users.models.user import User


class IsAuthenticatedAndReadOnly(BasePermission):

    def has_permission(self, request, view):
        user = request.user
        return user.is_authenticated and request.method in SAFE_METHODS 


class IsDirector(BasePermission):

    def has_permission(self, request, view):
        user = request.user
        return user.is_authenticated and user.current_role == User.Roles.DIRECTOR


class IsWarehouseman(BasePermission):

    def has_permission(self, request, view):
        user = request.user
        return user.is_authenticated and user.current_role == User.Roles.WAREHOUSEMAN


class IsSalesman(BasePermission):

    def has_permission(self, request, view):
        user = request.user
        return user.is_authenticated and user.current_role == User.Roles.SALESMAN


class IsFinancier(BasePermission):

    def has_permission(self, request, view):
        user = request.user
        return user.is_authenticated and user.current_role == User.Roles.FINANCIER
