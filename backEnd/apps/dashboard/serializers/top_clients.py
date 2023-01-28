from rest_framework import serializers

from apps.sales.models import Client


class TopClientsSerializer(serializers.ModelSerializer):
    total_sales = serializers.DecimalField(max_digits=20, decimal_places=2, allow_null=False)

    class Meta:
        model = Client
        fields = (
            "id",
            "title",
            "phone_number",
            "total_sales",
        )
