import pytest
from _pytest.monkeypatch import MonkeyPatch
from django.test import SimpleTestCase
from utils.wrappers import MeliWrapper
from meli.api_client import ApiClient
from meli.api.rest_client_api import RestClientApi
from decouple import config


@pytest.mark.usefixtures("get_sorted_by_price_data_fixture")
@pytest.mark.usefixtures("get_result_sorted_by_price_fixture")
class TestMelliWrapper(SimpleTestCase):
    def setUp(self) -> None:
        self.search_url = "/sites/MLA/search?{}"
        self.api_client = ApiClient()
        self.rest_client_api = RestClientApi(self.api_client)
        self.query_string = {
            "category": "MLA352679",
            "sort": "price_desc",
            "attributes": "id,permalink,pictures.url",
            "limit": 5,
            "offset": 0,
        }
        self.access_token = config("TOKEN")

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
