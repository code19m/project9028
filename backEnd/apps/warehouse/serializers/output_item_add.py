from rest_framework import serializers

from apps.warehouse.models import OutputInvoice, OutputInvoiceItem


class OutputInvoiceItemAddSerializer(serializers.ModelSerializer):

    class Meta:
        model = OutputInvoiceItem
        fields = (
            "product",
            "invoice",
            "quantity",
            "price"
        )

    def validate_invoice(self, value):
        if value.status == OutputInvoice.Statuses.CONFIRMED:
            raise serializers.ValidationError(
                {
                    "keys": "invoice",
                    "error": "cannot add invoice item to confirmed invoice"
                }
            )
        return value
