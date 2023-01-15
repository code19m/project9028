from django.db.models import Sum, F, DecimalField
from django.db.models.functions import Coalesce
from rest_framework import serializers

from apps.finance.models import Income
from apps.warehouse.models import OutputInvoiceItem


class IncomeAddSerializer(serializers.ModelSerializer):

    class Meta:
        model = Income
        fields = (
            "id",
            "income_type",
            "invoice",
            "amount",
        )

    def validate_invoice(self, value):
        return value

    def validate(self, attrs):
        income_type = attrs["income_type"]
        invoice = attrs.get("invoice")
        amount = attrs["amount"]

        if income_type == Income.Types.FROM_SALES and invoice is None:
            raise serializers.ValidationError(
                {
                    "keys": "invoice",
                    "error": 'invoice cannot be null when income_type is "from_sales"'
                }
            )

        if income_type == Income.Types.FROM_OUTSIDE and invoice is not None:
            raise serializers.ValidationError(
                {
                    "keys": "invoice",
                    "error": 'invoice must be null when income_type is "from_outside"'
                }
            )

        if invoice:
            invoice_total_sum = OutputInvoiceItem.objects.filter(
                invoice=invoice
            ).aggregate(
                total_sum=Sum(
                    F("quantity") * F("price"), 
                    output_field=DecimalField(max_digits=20, decimal_places=2),
                    default=0,
                ),
            )["total_sum"]

            invoice_paid_sum = Income.objects.filter(invoice=invoice).aggregate(
                paid_sum=Sum(
                    "amount", 
                    output_field=DecimalField(max_digits=20, decimal_places=2),
                    default=0,
                ),
            )["paid_sum"]

            rest_amount = invoice_total_sum - invoice_paid_sum

            if amount > rest_amount:
                raise serializers.ValidationError(
                    {
                        "keys": "amount",
                        "error": "amount is bigger than debt of this invoice",
                        "details": f"total_sum: {invoice_total_sum}, paid_sum: {invoice_paid_sum}, amount: {amount}"
                    }
                )

        return attrs
