from rest_framework import serializers

from apps.warehouse.models import InputInvoiceItem
from apps.warehouse.serializers.product_get import ProductNestedSerializer


class InputInvoiceItemGetSerializer(serializers.ModelSerializer):
    product = ProductNestedSerializer()

    class Meta:
        model = InputInvoiceItem
        fields = (
            "product",
            "invoice",
            "quantity",
            "price"
        )
