from rest_framework import serializers

from apps.warehouse.models.product import Product


class ProductUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = (
            "id",
            "title",
            "code",
            "shelf_life",
            "current_price",
            "product_type",
            "group",
            "description"
        )

    def validate_title(self, value):
        instance = self.instance
        exists = Product.objects.filter(
            is_deleted=False, title=value
        ).exclude(
            id=instance.id
        ).exists()
        if exists:
            raise serializers.ValidationError(
                {
                    "key": "title",
                    "error": "already exists"
                }
            )
        return value

    def validate_code(self, value):
        instance = self.instance
        exists = Product.objects.filter(
            is_deleted=False, code=value
        ).exclude(
            id=instance.id
        ).exists()
        if exists:
            raise serializers.ValidationError(
                {
                    "key": "code",
                    "error": "already exists"
                }
            )
        return value
