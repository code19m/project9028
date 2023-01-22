from rest_framework import serializers

from apps.warehouse.models import Brand


class BrandSerializer(serializers.ModelSerializer):

    class Meta:
        model = Brand
        fields = (
            "id",
            "title",
        )
