from rest_framework.viewsets import ModelViewSet

from apps.warehouse.models import Group
from apps.warehouse.serializers.group import GroupSerializer
from utils.permissions import IsWarehouseman, IsAuthenticatedAndReadOnly


class GroupViewSet(ModelViewSet):
    queryset = Group.objects.filter(is_deleted=False)
    serializer_class = GroupSerializer
    permission_classes = (IsWarehouseman | IsAuthenticatedAndReadOnly,)
    search_fields = ("title",)

    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.save()
