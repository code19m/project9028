from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apps.warehouse.views.input_invoice import InputInvoiceListAddView
from apps.warehouse.views.group import GroupViewSet
from apps.warehouse.views.product import ProductListAddView, ProductRetrieveUpdateDestroyView


router = DefaultRouter()
router.register("group", GroupViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("product/", ProductListAddView.as_view()),
    path("product/<int:pk>/", ProductRetrieveUpdateDestroyView.as_view()),
    
    path("input-invoice/", InputInvoiceListAddView.as_view()),
]
