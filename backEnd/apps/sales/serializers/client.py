from rest_framework import serializers

from apps.sales.models import Client


class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = (
            "id",
            "title",
            "phone_number",
            "address",
        )
