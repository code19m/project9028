from django.urls import path

from apps.dashboard.views.monthly_profit import MonthlyProfitView
from apps.dashboard.views.annual_profit import AnnualProfitView
from apps.dashboard.views.top_products import TopProductsView
from apps.dashboard.views.top_clients import TopClientsView
from apps.dashboard.views.supplier_credits import SupplierCreditsView
from apps.dashboard.views.client_debts import ClientDebtsView


urlpatterns = [
    path("monthly-profit/", MonthlyProfitView.as_view()),
    path("annual-profit/", AnnualProfitView.as_view()),
    path("top-products/", TopProductsView.as_view()),
    path("top-clients/", TopClientsView.as_view()),
    path("supplier-credits/", SupplierCreditsView.as_view()),
    path("client-debts/", ClientDebtsView.as_view()),
]
