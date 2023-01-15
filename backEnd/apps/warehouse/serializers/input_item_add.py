from rest_framework import serializers

from apps.warehouse.models import InputInvoiceItem, InputInvoice


class InputInvoiceItemAddSerializer(serializers.ModelSerializer):

    class Meta:
        model = InputInvoiceItem
        fields = (
            "product",
            "invoice",
            "quantity",
            "price"
        )

    def validate_invoice(self, value):
        if value.status == InputInvoice.Statuses.CONFIRMED:
            raise serializers.ValidationError(
                {
                    "keys": "invoice",
                    "error": "cannot add invoice item to confirmed invoice"
                }
            )
        return value
