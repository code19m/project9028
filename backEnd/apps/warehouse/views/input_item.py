from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.serializers import ValidationError

from apps.warehouse.models import InputInvoiceItem, InputInvoice
from apps.warehouse.serializers.input_item_add import InputInvoiceItemAddSerializer
from apps.warehouse.serializers.input_item_get import InputInvoiceItemGetSerializer
from apps.warehouse.serializers.input_item_update import InputInvoiceItemUpdateSerializer
from utils.permissions import IsWarehouseman, IsAuthenticatedAndReadOnly


class InputInvoiceItemListAddView(GenericAPIView):
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
        return InputInvoiceItem.objects.select_related("product")

    def get_serializer_class(self):
        match self.request.method:
            case "POST":
                return InputInvoiceItemAddSerializer
            case "GET":
                return InputInvoiceItemGetSerializer


class InputInvoiceItemUpdateDestroyView(GenericAPIView):
    queryset = InputInvoiceItem.objects.all()
    permission_classes = (IsWarehouseman | IsAuthenticatedAndReadOnly,)
    serializer_class = InputInvoiceItemUpdateSerializer

    def put(self, request, pk):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk):
        instance = self.get_object()
        if instance.invoice.status == InputInvoice.Statuses.CONFIRMED:
            raise ValidationError(
                {
                    "keys": "invoice_is_confirmed",
                    "error": "cannot delele item of confirmed invoice"
                }
            )
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
