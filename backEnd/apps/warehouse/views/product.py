from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from apps.warehouse.models import Product
from apps.warehouse.serializers.product_add import ProductAddSerializer
from apps.warehouse.serializers.product_get import ProductGetSerializer
from apps.warehouse.serializers.product_update import ProductUpdateSerializer
from utils.permissions import IsWarehouseman, IsAuthenticatedAndReadOnly


class ProductListAddView(GenericAPIView):
    permission_classes = (IsWarehouseman | IsAuthenticatedAndReadOnly,)
    filterset_fields = ("group", "product_type",)
    search_fields = ("title", "code",)

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
        return Product.objects.filter(is_deleted=False).select_related("group")

    def get_serializer_class(self):
        match self.request.method:
            case "POST":
                return ProductAddSerializer
            case "GET":
                return ProductGetSerializer


class ProductRetrieveUpdateDestroyView(GenericAPIView):
    queryset = Product.objects.filter(is_deleted=False)
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
        instance.is_deleted=True
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_serializer_class(self):
        match self.request.method:
            case "GET":
                return ProductGetSerializer
            case "PUT":
                return ProductUpdateSerializer
