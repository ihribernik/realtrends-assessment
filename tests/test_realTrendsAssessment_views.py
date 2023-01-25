from django.test import SimpleTestCase
from django.urls import reverse


class TestHomeView(SimpleTestCase):
    def setUp(self) -> None:
        self.home_url = reverse("home")
        # self.best_sellers_url = reverse("top-best-sellers")
        self.template = "realTrendsAssessment/index.html"

    def setup_databases(self, **kwargs):
        """Override the database creation defined in parent class"""

    pass

    def teardown_databases(self, old_config, **kwargs):
        """Override the database teardown defined in parent class"""
        pass

    def test_home(self):
        response = self.client.get(self.home_url)
        self.assertTemplateUsed(response, self.template)
