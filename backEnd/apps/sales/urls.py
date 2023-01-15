from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apps.sales.views.client import ClientViewSet


router = DefaultRouter()
router.register("client", ClientViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
