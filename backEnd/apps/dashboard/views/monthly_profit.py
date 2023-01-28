from django.db.models import Sum
from django.utils import timezone
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from apps.finance.models import Expense, Income


class MonthlyProfitView(GenericAPIView):

    def get(self, request):
        month = request.GET.get("month") or timezone.now().month

        total_income = Income.objects.filter(
            income_type=Income.Types.FROM_SALES,
            added_time__month=month
        ).aggregate(total=Sum("amount", default=0))["total"]
        
        total_expense = Expense.objects.filter(added_time__month=month) \
            .aggregate(total=Sum("amount", default=0))["total"]
        
        return Response({
            "total_income": total_income,
            "total_expense": total_expense,
            "profit": total_income - total_expense,
        })
