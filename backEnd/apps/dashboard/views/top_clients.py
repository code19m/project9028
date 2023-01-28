from django.db.models import Sum, F
from rest_framework.generics import GenericAPIView

from apps.dashboard.serializers.top_clients import TopClientsSerializer
from apps.sales.models import Client


class TopClientsView(GenericAPIView):
    serializer_class = TopClientsSerializer

    def get(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        serializer = self.get_serializer(page, many=True)
        return self.get_paginated_response(serializer.data)

    def get_queryset(self):
        queryset = Client.objects.filter(
            is_deleted=False
        ).annotate(
            total_sales=Sum(
                F("invoices__items__quantity") * F("invoices__items__price"),
                default=0
            )
        ).order_by("-total_sales")
        return queryset
