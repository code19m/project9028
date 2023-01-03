from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from apps.users.views import (
    CurrentUserViewSet,
    MyTokenObtainPairView,
    ChangeRoleView,
    ChangePasswordView,
)


urlpatterns = [
    path("token/", MyTokenObtainPairView.as_view()),
    path("token/refresh/", TokenRefreshView.as_view()),
    path("me/", CurrentUserViewSet.as_view()),

    path("change-role/", ChangeRoleView.as_view()),
    path("change-password/", ChangePasswordView.as_view()),
]
