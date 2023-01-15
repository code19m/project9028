from rest_framework import serializers

from apps.warehouse.models import InputInvoiceItem, InputInvoice


class InputInvoiceItemUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = InputInvoiceItem
        fields = (
            "quantity",
            "price",
        )

    def validate(self, attrs):
        invoice = self.instance.invoice
        if invoice.status == InputInvoice.Statuses.CONFIRMED:
            raise serializers.ValidationError(
                {
                    "keys": "invoice_is_confirmed",
                    "error": "cannot update item of confirmed invoice"
                }
            )
        return attrs
