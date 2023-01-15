from rest_framework import serializers

from apps.finance.models import Income


class IncomeGetSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Income
        fields = (
            "id",
            "income_type",
            "invoice",
            "amount",
            "added_time",
        )
