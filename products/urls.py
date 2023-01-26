from django.urls import path
from . import views

urlpatterns = [
    path(
        "top-best-sellers", views.BestSellersUserNickNames.as_view(), name="top-best-sellers"
    ),
    path(
        "most-expensive-products",
        views.MostExpensiveProducts.as_view(),
        name="most-expensive-products",
    ),
]
