from django.db import transaction
from django.db.models import Sum, F, Subquery, OuterRef
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.serializers import ValidationError

from apps.warehouse.models import InputInvoice
from apps.finance.models import Expense
from apps.warehouse.serializers.input_invoice_add import InputInvoiceAddSerializer
from apps.warehouse.serializers.input_invoice_get import InputInvoiceGetSerializer
from apps.warehouse.serializers.input_invoice_update import InputInvoiceUpdateSerializer
from utils.permissions import IsWarehouseman, IsAuthenticatedAndReadOnly


class InputInvoiceListAddView(GenericAPIView):
    permission_classes = (IsWarehouseman | IsAuthenticatedAndReadOnly,)

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
        return InputInvoice.objects.annotate(
            total_sum=Sum(F("items__quantity") * F("items__price"), default=0),
            paid_sum=Subquery(
                InputInvoice.objects.filter(id=OuterRef("id")) \
                    .annotate(paid_sum=Sum("expenses__amount", default=0)) \
                    .values("paid_sum")[:1]
            )
        ).select_related(
            "supplier"
        ).order_by("-id")

    def get_serializer_class(self):
        match self.request.method:
            case "POST":
                return InputInvoiceAddSerializer
            case "GET":
                return InputInvoiceGetSerializer


class InputInvoiceRetrieveUpdateDestroyView(GenericAPIView):
    permission_classes = (IsWarehouseman | IsAuthenticatedAndReadOnly,)

    def get(self, request, pk):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def put(self, request, pk):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk):
        instance = self.get_object()
        if instance.status == InputInvoice.Statuses.CONFIRMED:
            raise ValidationError(
                {
                    "keys": "invoice_is_confirmed",
                    "error": "cannot delele confirmed invoice"
                }
            )
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_queryset(self):
        return InputInvoice.objects.annotate(
            total_sum=Sum(F("items__quantity") * F("items__price"), default=0),
            paid_sum=Subquery(
                InputInvoice.objects.filter(id=OuterRef("id")) \
                    .annotate(paid_sum=Sum("expenses__amount", default=0)) \
                    .values("paid_sum")[:1]
            )
        ).select_related(
            "supplier"
        ).order_by("-id")

    def get_serializer_class(self):
        match self.request.method:
            case "GET":
                return InputInvoiceGetSerializer
            case "PUT":
                return InputInvoiceUpdateSerializer


class InputInvoiceConfirmView(GenericAPIView):
    permission_classes = (IsWarehouseman | IsAuthenticatedAndReadOnly,)

    @transaction.atomic
    def post(self, request, pk):
        invoice = self.get_object()
        invoice.set_confirmed_status()
        invoice.update_products_quantity()
        return Response(status=status.HTTP_200_OK)

    def get_queryset(self):
        return InputInvoice.objects.filter(status=InputInvoice.Statuses.NEW)
