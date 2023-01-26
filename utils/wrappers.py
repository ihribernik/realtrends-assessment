from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from meli import OAuth20Api
from meli.api.rest_client_api import RestClientApi
from typing import Dict, List
from urllib.parse import urlencode
from utils.constants import MELI_BASE_URL


class MeliWrapper:
    def __init__(
        self,
        rest_client_api: RestClientApi,
        query_string: Dict = None,
        access_token: str = '',
        search_url: str = '',
        auth_api: OAuth20Api = None,
        grant_type: str = '',
        client_id: str = '',
        client_secret: str = '',
        redirect_uri: str = '',
    ) -> None:
        self.rest_client_api = rest_client_api
        self.query_string = query_string
        self.access_token = access_token
        self.search_url = search_url
        self.auth_api = auth_api
        self.grant_type = grant_type
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri

    def get_auth(self) -> HttpResponseRedirect:
        url = MELI_BASE_URL.format(self.client_id, self.redirect_uri)
        return redirect(url)

    def get_token(self, code) -> object:

        response = self.auth_api.get_token(
            grant_type=self.grant_type,
            client_id=self.client_id,
            client_secret=self.client_secret,
            redirect_uri=self.redirect_uri,
            code=code
        )
        return response

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
