from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.serializers import ValidationError

from apps.warehouse.models import OutputInvoice, OutputInvoiceItem
from apps.warehouse.serializers.output_item_add import OutputInvoiceItemAddSerializer
from apps.warehouse.serializers.output_item_get import OutputInvoiceItemGetSerializer
from apps.warehouse.serializers.output_item_update import OutputInvoiceItemUpdateSerializer
from utils.permissions import IsWarehouseman, IsAuthenticatedAndReadOnly


class OutputInvoiceItemListAddView(GenericAPIView):
    permission_classes = (IsWarehouseman | IsAuthenticatedAndReadOnly,)
    filterset_fields = ("product", "invoice")

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        serializer = self.get_serializer(page, many=True)
        return self.get_paginated_response(serializer.data)

    def get_queryset(self):
        return OutputInvoiceItem.objects.select_related("product")

    def get_serializer_class(self):
        match self.request.method:
            case "POST":
                return OutputInvoiceItemAddSerializer
            case "GET":
                return OutputInvoiceItemGetSerializer


class OutputInvoiceItemUpdateDestroyView(GenericAPIView):
    queryset = OutputInvoiceItem.objects.all()
    permission_classes = (IsWarehouseman | IsAuthenticatedAndReadOnly,)
    serializer_class = OutputInvoiceItemUpdateSerializer

    def put(self, request, pk):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk):
        instance = self.get_object()
        if instance.status == OutputInvoice.Statuses.CONFIRMED:
            raise ValidationError(
                {
                    "keys": "invoice_is_confirmed",
                    "error": "cannot delele item of confirmed invoice"
                }
            )
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
