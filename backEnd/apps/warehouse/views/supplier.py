from django.db.models import Sum, F
from rest_framework.viewsets import ModelViewSet

from apps.warehouse.models import Supplier
from apps.warehouse.serializers.supplier import SupplierSerializer, SupplierGetSerializer
from utils.permissions import IsWarehouseman, IsAuthenticatedAndReadOnly


class SupplierViewSet(ModelViewSet):
    serializer_class = SupplierSerializer
    permission_classes = (IsWarehouseman | IsAuthenticatedAndReadOnly,)
    search_fields = ("title",)

    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.save()

    def get_queryset(self):
        queryset = Supplier.objects.filter(is_deleted=False).annotate(
            credit=Sum(
                F("invoices__items__quantity") * F("invoices__items__price"),
                default=0
            ) - Sum(F("invoices__expenses__amount"), default=0)
        )
        return queryset

    def get_serializer_class(self):
        match self.request.method:
            case "POST", "PUT":
                return SupplierSerializer
            case _:
                return SupplierGetSerializer
