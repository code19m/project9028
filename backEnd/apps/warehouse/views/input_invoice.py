from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from apps.warehouse.models import InputInvoice
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
        return InputInvoice.objects.filter(is_deleted=False).select_related("supplier")
