from django.db.models import Sum, F
from rest_framework.generics import GenericAPIView

from apps.dashboard.serializers.supplier_credits import SupplierCreditSerializer
from apps.warehouse.models import Supplier


class SupplierCreditsView(GenericAPIView):
    serializer_class = SupplierCreditSerializer

    def get(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        serializer = self.get_serializer(page, many=True)
        return self.get_paginated_response(serializer.data)

    # Incorrect calculation !!
    def get_queryset(self):
        queryset = Supplier.objects.filter(
            is_deleted=False
        ).annotate(
            total_credit=Sum(
                F("invoices__items__quantity") * F("invoices__items__price"),
                default=0
            ) - Sum(F("invoices__expenses__amount"))
        ).order_by("-total_credit")
        return queryset
