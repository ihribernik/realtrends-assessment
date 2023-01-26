from django.test import SimpleTestCase
from django.test.client import RequestFactory
from http import HTTPStatus


class TestErrorUrlsView(SimpleTestCase):
    def setUp(self) -> None:
        self.client.raise_request_exception = False
        self.request = RequestFactory()

    def setup_databases(self, **kwargs):
        """Override the database creation defined in parent class"""

    pass

    def teardown_databases(self, old_config, **kwargs):
        """Override the database teardown defined in parent class"""
        pass

    def test_404(self):
        response = self.client.get("/superPrueba")
        self.assertEqual(response.status_code, HTTPStatus.NOT_FOUND)
        self.assertTemplateUsed(response, "404.html")
