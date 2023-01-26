import json

import pytest
from _pytest.monkeypatch import MonkeyPatch
from decouple import config
from django.test import SimpleTestCase
from meli.api.rest_client_api import RestClientApi
from meli.api_client import ApiClient
from meli import OAuth20Api

from utils.constants import (
    SEARCH_URL,
    SEARCH_CATEGORY,
    SORT_BY_SOLD_QUANTITY_ASC,
    LIMIT_SOLD_QUANTITY,
    GRANT_TYPE,
    REDIRECT_LOCAL_URL,
)
from utils.wrappers import MeliWrapper


@pytest.mark.usefixtures("get_sorted_by_price_data_fixture")
@pytest.mark.usefixtures("get_result_sorted_by_price_fixture")
@pytest.mark.usefixtures("get_sorted_by_best_sellers_fixture")
@pytest.mark.usefixtures("get_result_sorted_by_best_sellers_fixture")
class TestMelliWrapper(SimpleTestCase):
    def setUp(self) -> None:
        self.search_url = SEARCH_URL
        self.api_client = ApiClient()
        self.rest_client_api = RestClientApi(self.api_client)
        self.access_token = config("APP_SECRET")
        self.query_string = {
            "category": SEARCH_CATEGORY,
            "sort": SORT_BY_SOLD_QUANTITY_ASC,
            "limit": LIMIT_SOLD_QUANTITY,
        }

        self.monkeypatch = MonkeyPatch()

    def setup_databases(self, **kwargs) -> None:
        """Override the database creation defined in parent class"""
        pass

    def teardown_databases(self, old_config, **kwargs) -> None:
        """Override the database teardown defined in parent class"""
        pass

    def test_get_result_sorted_by_price(self) -> None:
        meli_wrapper = MeliWrapper(
            self.rest_client_api, self.query_string, self.access_token, self.search_url
        )
        self.monkeypatch.setattr(
            target=meli_wrapper, name="get_info", value=self.get_sorted_by_price_data
        )
        response = meli_wrapper.get_result_sorted_by_price()
        mock_data = self.get_result_sorted_by_price()
        self.assertEqual(mock_data, response)

    def test_get_transactions_completed(self) -> None:
        meli_wrapper = MeliWrapper(
            self.rest_client_api, self.query_string, self.access_token, self.search_url
        )
        self.monkeypatch.setattr(
            target=meli_wrapper, name="get_info", value=self.get_sellers_data
        )
        response = meli_wrapper.get_transactions_completed()
        mock_data = self.get_result_sorted_by_best_sellers()
        self.assertEqual(mock_data, response)

    # TODO: falta terminar este test
    # def test_get_token(self) -> None:
    #     auth_api = OAuth20Api(self.api_client)
    #     meli_wrapper = MeliWrapper(
    #         auth_api=auth_api,
    #         grant_type=GRANT_TYPE,
    #         client_id=config('APP_ID'),
    #         client_secret=config('APP_SECRET'),
    #         redirect_uri=REDIRECT_LOCAL_URL,
    #     )
    #
    #     refesh_toke = meli_wrapper.get_auth()
    #     mock_data = ''
    #     response = meli_wrapper.get_token(refesh_toke)
    #
    #     self.assertEqual(mock_data, response)
