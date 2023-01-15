from rest_framework import serializers

from apps.warehouse.models import Supplier


class SupplierSerializer(serializers.ModelSerializer):

    class Meta:
        model = Supplier
        fields = (
            "id",
            "title",
            "address",
        )
