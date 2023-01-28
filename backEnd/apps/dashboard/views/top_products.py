from django.db.models import Sum, F
from rest_framework.generics import GenericAPIView

from apps.dashboard.serializers.top_products import TopProductsSerializer
from apps.warehouse.models import Product


class TopProductsView(GenericAPIView):
    serializer_class = TopProductsSerializer

    def get(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        serializer = self.get_serializer(page, many=True)
        return self.get_paginated_response(serializer.data)

    def get_queryset(self):
        queryset = Product.objects.annotate(
            total_sales=Sum(F("output_items__quantity") * F("output_items__price"), default=0)
        ).order_by("-total_sales")
        return queryset
