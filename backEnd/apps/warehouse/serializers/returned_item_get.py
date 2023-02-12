from rest_framework import serializers

from apps.warehouse.models import ReturnedInvoiceItem
from apps.warehouse.serializers.product_get import ProductNestedSerializer


class ReturnedInvoiceItemGetSerializer(serializers.ModelSerializer):
    product = ProductNestedSerializer()

    class Meta:
        model = ReturnedInvoiceItem
        fields = (
            "id",
            "product",
            "invoice",
            "quantity",
            "price",
        )
