from rest_framework import serializers

from apps.finance.models import Expense


class ExpenseGetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Expense
        fields = (
            "cost_type",
            "invoice",
            "returned_invoice",
            "amount",
            "description"
        )
