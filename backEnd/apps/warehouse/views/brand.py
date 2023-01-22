from rest_framework.viewsets import ModelViewSet

from apps.warehouse.models import Brand
from apps.warehouse.serializers.brand import BrandSerializer
from utils.permissions import IsWarehouseman, IsAuthenticatedAndReadOnly


class BrandViewSet(ModelViewSet):
    queryset = Brand.objects.filter(is_deleted=False)
    serializer_class = BrandSerializer
    permission_classes = (IsWarehouseman | IsAuthenticatedAndReadOnly,)
    search_fields = ("title",)

    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.save()
