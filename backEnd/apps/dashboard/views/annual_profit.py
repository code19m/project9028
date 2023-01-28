from django.db.models import Sum
from django.utils import timezone
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from apps.finance.models import Income, Expense


MONTHS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]


class AnnualProfitView(GenericAPIView):

    def get(self, request):
        year = request.GET.get("year") or timezone.now().year

        response = {}
        for month in MONTHS:
            total_income = Income.objects.filter(
                income_type=Income.Types.FROM_SALES,
                added_time__year=year, added_time__month=month
            ).aggregate(total=Sum("amount", default=0))["total"]

            total_expense = Expense.objects.filter(
                added_time__year=year, added_time__month=month
            ).aggregate(total=Sum("amount", default=0))["total"]

            response[str(month)] = {
                "total_income": total_income,
                "total_expense": total_expense,
                "profit": total_income - total_expense,
            }

        return Response(response)
