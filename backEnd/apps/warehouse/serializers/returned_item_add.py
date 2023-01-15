from rest_framework import serializers

from apps.warehouse.models import ReturnedInvoice, ReturnedInvoiceItem


class ReturnedInvoiceItemAddSerializer(serializers.ModelSerializer):

    class Meta:
        model = ReturnedInvoiceItem
        fields = (
            "product",
            "invoice",
            "quantity",
            "price"
        )

    def validate_invoice(self, value):
        if value.status == ReturnedInvoice.Statuses.CONFIRMED:
            raise serializers.ValidationError(
                {
                    "keys": "invoice",
                    "error": "cannot add invoice item to confirmed invoice"
                }
            )
        return value
