from decouple import config
from django.views.generic import TemplateView
from meli import ApiClient
from meli.api.rest_client_api import RestClientApi

from utils.wrappers import MeliWrapper

from utils.constants import (
    SEARCH_URL,
    SEARCH_CATEGORY,
    LIMIT_PRICE_DESC,
    SORT_BY_PRICE_DESC,
    LIMIT_SOLD_QUANTITY,
    SORT_BY_SOLD_QUANTITY_ASC,
)


class MostExpensiveProducts(TemplateView):
    """
    Una página que muestre el listado con los apodos de
    los cinco usuarios con mayor
    cantidad de unidades vendidas en la categoría “Smartwatch”
    """

    template_name = "products/most_expensive_products.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        with ApiClient() as api_client:
            access_token = config("APP_SECRET")
            rest_client_api = RestClientApi(api_client)
            query_string = {
                "category": SEARCH_CATEGORY,
                "sort": SORT_BY_PRICE_DESC,
                "limit": LIMIT_PRICE_DESC,
            }

            meli_wrapper = MeliWrapper(
                rest_client_api, query_string, access_token, SEARCH_URL
            )
            response = meli_wrapper.get_result_sorted_by_price()

            context["products"] = response
            return context


class BestSellersUserNickNames(TemplateView):
    """
    Una página que muestre el listado con los apodos
    de los cinco usuarios con mayor
    cantidad de unidades vendidas en la categoría “Smartwatch”
    """

    template_name = "products/best_sellers_user_nicknames.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        with ApiClient() as api_client:
            access_token = config("APP_SECRET")
            rest_client_api = RestClientApi(api_client)
            query_string = {
                "category": SEARCH_CATEGORY,
                "sort": SORT_BY_SOLD_QUANTITY_ASC,
                "limit": LIMIT_SOLD_QUANTITY,
            }

            meli_wrapper = MeliWrapper(
                rest_client_api, query_string, access_token, SEARCH_URL
            )
            response = meli_wrapper.get_transactions_completed()

            context["sellers"] = response
            return context
