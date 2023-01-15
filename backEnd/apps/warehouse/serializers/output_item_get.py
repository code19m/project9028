from rest_framework import serializers

from apps.warehouse.models import OutputInvoiceItem
from apps.warehouse.serializers.product_get import ProductNestedSerializer


class OutputInvoiceItemGetSerializer(serializers.ModelSerializer):
    product = ProductNestedSerializer()

    class Meta:
        model = OutputInvoiceItem
        fields = (
            "product",
            "invoice",
            "quantity",
            "price"
        )
