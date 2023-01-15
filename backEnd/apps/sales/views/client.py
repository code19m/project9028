from rest_framework.viewsets import ModelViewSet

from apps.sales.models import Client
from apps.sales.serializers.client import ClientSerializer
from utils.permissions import IsSalesman, IsAuthenticatedAndReadOnly


class ClientViewSet(ModelViewSet):
    queryset = Client.objects.filter(is_deleted=False)
    serializer_class = ClientSerializer
    permission_classes = (IsSalesman | IsAuthenticatedAndReadOnly,)
    search_fields = ("title", "phone_number")

    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.save()
