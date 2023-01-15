from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apps.warehouse.views.input_invoice import (
    InputInvoiceListAddView,
    InputInvoiceRetrieveUpdateDestroyView,
)
from apps.warehouse.views.input_item import (
    InputInvoiceItemListAddView,
    InputInvoiceItemUpdateDestroyView,
)
from apps.warehouse.views.group import GroupViewSet
from apps.warehouse.views.output_invoice import (
    OutputInvoiceListAddView,
    OutputInvoiceRetrieveUpdateDestroyView,
)
from apps.warehouse.views.output_item import (
    OutputInvoiceItemListAddView,
    OutputInvoiceItemUpdateDestroyView,
)
from apps.warehouse.views.product import (
    ProductListAddView,
    ProductRetrieveUpdateDestroyView,
)
from apps.warehouse.views.returned_invoice import (
    ReturnedInvoiceListAddView,
    ReturnedInvoiceRetrieveUpdateDestroyView,
)
from apps.warehouse.views.returned_item import (
    ReturnedInvoiceItemListAddView,
    ReturnedInvoiceItemUpdateDestroyView,
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

    path("returned-invoice/", ReturnedInvoiceListAddView.as_view()),
    path("returned-invoice/<int:pk>/", ReturnedInvoiceRetrieveUpdateDestroyView.as_view()),

    path("returned-invoice-item/", ReturnedInvoiceItemListAddView.as_view()),
    path("returned-invoice-item/<int:pk>/", ReturnedInvoiceItemUpdateDestroyView.as_view()),
]
