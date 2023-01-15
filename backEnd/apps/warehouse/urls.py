from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apps.warehouse.views.input_invoice import (
    InputInvoiceListAddView,
    InputInvoiceRetrieveUpdateDestroyView,
)
from apps.warehouse.views.input_items import (
    InputInvoiceItemListAddView,
    InputInvoiceItemUpdateDestroyView,
)
from apps.warehouse.views.group import GroupViewSet
from apps.warehouse.views.output_invoice import (
    OutputInvoiceListAddView,
    OutputInvoiceRetrieveUpdateDestroyView,
)
from apps.warehouse.views.output_items import (
    OutputInvoiceItemListAddView,
    OutputInvoiceItemUpdateDestroyView,
)
from apps.warehouse.views.product import (
    ProductListAddView,
    ProductRetrieveUpdateDestroyView,
)
from apps.warehouse.views.supplier import SupplierViewSet


router = DefaultRouter()
router.register("group", GroupViewSet)
router.register("supplier", SupplierViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("product/", ProductListAddView.as_view()),
    path("product/<int:pk>/", ProductRetrieveUpdateDestroyView.as_view()),

    path("input-invoice/", InputInvoiceListAddView.as_view()),
    path("input-invoice/<int:pk>/", InputInvoiceRetrieveUpdateDestroyView.as_view()),

    path("input-invoice-item/", InputInvoiceItemListAddView.as_view()),
    path("input-invoice-item/<int:pk>/", InputInvoiceItemUpdateDestroyView.as_view()),

    path("output-invoice/", OutputInvoiceListAddView.as_view()),
    path("output-invoice/<int:pk>/", OutputInvoiceRetrieveUpdateDestroyView.as_view()),

    path("output-invoice-item/", OutputInvoiceItemListAddView.as_view()),
    path("output-invoice-item/<int:pk>/", OutputInvoiceItemUpdateDestroyView.as_view()),
]
