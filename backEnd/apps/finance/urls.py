from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apps.finance.views.expense import ExpenseListAddView
from apps.finance.views.income import IncomeListAddView


router = DefaultRouter()

urlpatterns = [
    path("", include(router.urls)),
    path("income/", IncomeListAddView.as_view()),
    path("expense/", ExpenseListAddView.as_view()),
]
