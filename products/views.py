# -*- coding: utf-8 -*-
""" """
from decouple import config
from django.shortcuts import render
from django.views.generic import TemplateView
from meli import ApiClient
from meli.api.rest_client_api import RestClientApi

from products.libs.wrappers import MeliWrapper


class HomeView(TemplateView):
    template_name = "products/home.html"


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
            access_token = config("TOKEN")
            rest_client_api = RestClientApi(api_client)
            query_string = {
                "category": "MLA352679",
                "sort": "price_desc",
                "attributes": "id,permalink,pictures.url",
                "limit": 5,
                "offset": 0,
            }
            search_url = "/sites/MLA/search?{}"

            meli_wrapper = MeliWrapper(
                rest_client_api, query_string, access_token, search_url
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
            access_token = config("TOKEN")
            rest_client_api = RestClientApi(api_client)
            query_string = {
                "category": "MLA352679",
                "sort": "sold_quantity_asc",
                "limit": 5,
                "offset": 0,
            }
            search_url = "/sites/MLA/search?{}"

            meli_wrapper = MeliWrapper(
                rest_client_api, query_string, access_token, search_url
            )
            response = meli_wrapper.get_transactions_completed()

            context["sellers"] = response
            return context


def handler404(request, *args, **argv):
    response = render("404.html", {})
    response.status_code = 404
    return response


def handler500(request, *args, **argv):
    response = render("500.html", {})
    response.status_code = 500
    return response
