from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.serializers import ValidationError

from apps.warehouse.models import ReturnedInvoice, ReturnedInvoiceItem
from apps.warehouse.serializers.returned_item_add import ReturnedInvoiceItemAddSerializer
from apps.warehouse.serializers.returned_item_get import ReturnedInvoiceItemGetSerializer
from apps.warehouse.serializers.returned_item_update import ReturnedInvoiceItemUpdateSerializer
from utils.permissions import IsWarehouseman, IsAuthenticatedAndReadOnly


class ReturnedInvoiceItemListAddView(GenericAPIView):
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
        return ReturnedInvoiceItem.objects.select_related("product")

    def get_serializer_class(self):
        match self.request.method:
            case "POST":
                return ReturnedInvoiceItemAddSerializer
            case "GET":
                return ReturnedInvoiceItemGetSerializer


class ReturnedInvoiceItemUpdateDestroyView(GenericAPIView):
    queryset = ReturnedInvoiceItem.objects.all()
    permission_classes = (IsWarehouseman | IsAuthenticatedAndReadOnly,)
    serializer_class = ReturnedInvoiceItemUpdateSerializer

    def put(self, request, pk):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk):
        instance = self.get_object()
        if instance.invoice.status == ReturnedInvoice.Statuses.CONFIRMED:
            raise ValidationError(
                {
                    "keys": "invoice_is_confirmed",
                    "error": "cannot delele item of confirmed invoice"
                }
            )
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
