from django.db.models import Sum, F, Subquery, OuterRef
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.serializers import ValidationError

from apps.warehouse.models import ReturnedInvoice
from apps.warehouse.serializers.returned_invoice_add import ReturnedInvoiceAddSerializer
from apps.warehouse.serializers.returned_invoice_get import ReturnedInvoiceGetSerializer
from apps.warehouse.serializers.returned_invoice_update import ReturnedInvoiceUpdateSerializer
from utils.permissions import IsWarehouseman, IsAuthenticatedAndReadOnly


class ReturnedInvoiceListAddView(GenericAPIView):
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
        return ReturnedInvoice.objects.annotate(
            total_sum=Sum(F("items__quantity") * F("items__price"), default=0),
            paid_sum=Subquery(
                ReturnedInvoice.objects.filter(id=OuterRef("id")) \
                    .annotate(paid_sum=Sum("expenses__amount", default=0)) \
                    .values("paid_sum")[:1]
            ),
        ).select_related(
            "client"
        ).order_by("-id")

    def get_serializer_class(self):
        match self.request.method:
            case "POST":
                return ReturnedInvoiceAddSerializer
            case "GET":
                return ReturnedInvoiceGetSerializer


class ReturnedInvoiceRetrieveUpdateDestroyView(GenericAPIView):
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
        if instance.status == ReturnedInvoice.Statuses.CONFIRMED:
            raise ValidationError(
                {
                    "keys": "invoice_is_confirmed",
                    "error": "cannot delele confirmed invoice"
                }
            )
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_queryset(self):
        return ReturnedInvoice.objects.annotate(
            total_sum=Sum(F("items__quantity") * F("items__price"), default=0),
            paid_sum=Subquery(
                ReturnedInvoice.objects.filter(id=OuterRef("id")) \
                    .annotate(paid_sum=Sum("expenses__amount", default=0)) \
                    .values("paid_sum")[:1]
            ),
        ).select_related(
            "client"
        ).order_by("-id")

    def get_serializer_class(self):
        match self.request.method:
            case "GET":
                return ReturnedInvoiceGetSerializer
            case "PUT":
                return ReturnedInvoiceUpdateSerializer
