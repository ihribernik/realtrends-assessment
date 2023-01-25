from meli.api.rest_client_api import RestClientApi
from typing import Dict, List
from urllib.parse import urlencode


class MeliWrapper:
    def __init__(
        self,
        rest_client_api: RestClientApi,
        query_string: Dict,
        access_token: str,
        search_url,
    ):
        self.rest_client_api = rest_client_api
        self.query_string = query_string
        self.access_token = access_token
        self.search_url = search_url

    def get_info(self) -> Dict:
        response = self.rest_client_api.resource_get(
            self.search_url.format(urlencode(self.query_string)),
            self.access_token,
        )
        return response

    def get_result_sorted_by_price(self) -> List:
        response = self.get_info()
        products = sorted(response["results"], key=lambda x: x["price"], reverse=True)
        return products

    def get_transactions_completed(self) -> List:
        response = self.get_info()
        sellers = [
            {
                "nickname": item["seller"]["nickname"],
                "transactions_completed": item["seller"]["seller_reputation"][
                    "transactions"
                ]["completed"],
            }
            for item in response["results"]
        ]
        sorted_sellers = sorted(
            sellers, key=lambda x: x["transactions_completed"], reverse=True
        )
        return sorted_sellers
