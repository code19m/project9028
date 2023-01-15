from rest_framework import serializers

from apps.warehouse.models import ReturnedInvoice, ReturnedInvoiceItem


class ReturnedInvoiceItemUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = ReturnedInvoiceItem
        fields = (
            "quantity",
            "price",
        )

    def validate(self, attrs):
        invoice = self.instance.invoice
        if invoice.status == ReturnedInvoice.Statuses.CONFIRMED:
            raise serializers.ValidationError(
                {
                    "keys": "invoice_is_confirmed",
                    "error": "cannot update item of confirmed invoice"
                }
            )
        return attrs
