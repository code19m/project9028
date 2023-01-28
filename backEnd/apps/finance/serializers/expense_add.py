from rest_framework import serializers

from apps.finance.models import Expense


class ExpenseAddSerializer(serializers.ModelSerializer):

    class Meta:
        model = Expense
        fields = (
            "cost_type",
            "invoice",
            "returned_invoice",
            "amount",
            "description"
        )

    def validate(self, attrs):
        cost_type = attrs.get("cost_type")
        invoice = attrs.get("invoice")
        returned_invoice = attrs.get("returned_invoice")
        amount = attrs.get("amount")

        if cost_type:
            if invoice or returned_invoice:
                raise serializers.ValidationError({
                    "keys": "cost_type",
                    "error": "invoice and returned_invoice must be null when adding cost_type"
                })

        if invoice:
            if cost_type or returned_invoice:
                raise serializers.ValidationError({
                    "keys": "invoice",
                    "error": "cost_type and returned_invoice must be null when adding invoice"
                })
        
        if returned_invoice:
            if invoice or cost_type:
                raise serializers.ValidationError({
                    "keys": "returned_invoice",
                    "error": "cost_type and invoice must be null when adding returned_invoice"
                })
        
        if not cost_type and not invoice and not returned_invoice:
            raise serializers.ValidationError({
                "keys": "cost_type, invoice, returned_invoice",
                "error": "must be provided one of the cost_type, invoice or returned_invoice"
            })

        if not amount:
            raise serializers.ValidationError({
                "keys": "amount",
                "error": "amount must be greater than 0"
            })

        return attrs
