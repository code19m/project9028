from rest_framework.viewsets import ModelViewSet

from apps.warehouse.models import Supplier
from apps.warehouse.serializers.supplier import SupplierSerializer
from utils.permissions import IsWarehouseman, IsAuthenticatedAndReadOnly


class SupplierViewSet(ModelViewSet):
    queryset = Supplier.objects.filter(is_deleted=False)
    serializer_class = SupplierSerializer
    permission_classes = (IsWarehouseman | IsAuthenticatedAndReadOnly,)
    search_fields = ("title",)

    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.save()
