from rest_framework.viewsets import ModelViewSet

from apps.finance.models import CostType
from apps.finance.serializers.cost_type import CostTypeSerializer
from utils.permissions import IsFinancier, IsAuthenticatedAndReadOnly


class CostTypeViewSet(ModelViewSet):
    queryset = CostType.objects.filter(is_deleted=False)
    serializer_class = CostTypeSerializer
    permission_classes = (IsFinancier | IsAuthenticatedAndReadOnly,)
    search_fields = ("title",)

    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.save()
