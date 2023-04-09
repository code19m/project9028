from django.db.models import Sum, F
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

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

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def get_queryset(self):
        queryset = Supplier.objects.filter(is_deleted=False).annotate(
            credit=Sum(
                F("invoices__items__quantity") * F("invoices__items__price"),
                default=0
            ) - Sum(F("invoices__expenses__amount"), default=0)
        )
        return queryset.order_by("id")

    def get_serializer_class(self):
        match self.request.method:
            case "POST":
                return SupplierSerializer
            case "PUT":
                return SupplierSerializer
            case _:
                return SupplierGetSerializer
