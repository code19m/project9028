from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apps.finance.views.income import IncomeListAddView
from apps.finance.views.cost_type import CostTypeViewSet


router = DefaultRouter()
router.register("cost-type", CostTypeViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("income/", IncomeListAddView.as_view()),
]
