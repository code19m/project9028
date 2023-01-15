from rest_framework import serializers

from apps.warehouse.models import OutputInvoice, OutputInvoiceItem


class OutputInvoiceItemUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = OutputInvoiceItem
        fields = (
            "quantity",
            "price",
        )

    def validate(self, attrs):
        invoice = self.instance.invoice
        if invoice.status == OutputInvoice.Statuses.CONFIRMED:
            raise serializers.ValidationError(
                {
                    "keys": "invoice_is_confirmed",
                    "error": "cannot update item of confirmed invoice"
                }
            )
        return attrs
