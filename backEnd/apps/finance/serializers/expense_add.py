from rest_framework import serializers

from apps.finance.models import Expense


class ExpenseAddSerializer(serializers.ModelSerializer):

    class Meta:
        model = Expense
        fields = (
            "invoice",
            "returned_invoice",
            "amount",
            "description"
        )

    def validate(self, attrs):
        invoice = attrs.get("invoice")
        returned_invoice = attrs.get("returned_invoice")
        amount = attrs.get("amount")

        if invoice and returned_invoice:
            raise serializers.ValidationError({
                "keys": "(invoice, returned_invoice)",
                "error": "invoice or returned_invoice must be null"
            })

        if not amount:
            raise serializers.ValidationError({
                "keys": "amount",
                "error": "amount must be greater than 0"
            })

        return attrs
