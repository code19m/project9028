from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from apps.finance.models import Expense
from apps.finance.serializers.expense_add import ExpenseAddSerializer
from apps.finance.serializers.expense_get import ExpenseGetSerializer
from utils.permissions import IsFinancier, IsAuthenticatedAndReadOnly


class ExpenseListAddView(GenericAPIView):
    queryset = Expense.objects.all()
    permission_classes = (IsFinancier | IsAuthenticatedAndReadOnly,)
    filterset_fields = ("cost_type__title",)

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

    def get_serializer_class(self):
        match self.request.method:
            case "POST":
                return ExpenseAddSerializer
            case "GET":
                return ExpenseGetSerializer
