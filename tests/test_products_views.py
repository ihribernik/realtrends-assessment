from django.test import SimpleTestCase
from django.urls import reverse


class TestHomeView(SimpleTestCase):
    def setUp(self) -> None:
        self.home_url = reverse("home")
        # self.best_sellers_url = reverse("top-best-sellers")
        self.template = "products/index.html"

    def setup_databases(self, **kwargs):
        """Override the database creation defined in parent class"""

    pass

    def teardown_databases(self, old_config, **kwargs):
        """Override the database teardown defined in parent class"""
        pass

    def test_home(self):
        response = self.client.get(self.home_url)
        self.assertTemplateUsed(response, self.template)


class TestBestSellersView(SimpleTestCase):
    def setUp(self) -> None:
        # self.home_url = reverse("home")
        self.best_sellers_url = reverse("top-best-sellers")
        self.template = "products/best_sellers_user_nicknames.html"

    def setup_databases(self, **kwargs):
        """Override the database creation defined in parent class"""

    pass

    def teardown_databases(self, old_config, **kwargs):
        """Override the database teardown defined in parent class"""
        pass

    def test_best_sellers_user_nicknames(self):
        response = self.client.get(self.best_sellers_url)
        self.assertTemplateUsed(response, self.template)


class TestMostExpensiveView(SimpleTestCase):
    def setUp(self) -> None:
        self.most_expensive_url = reverse("most-expensive-products")
        self.template = "products/most_expensive_products.html"

    def setup_databases(self, **kwargs):
        """Override the database creation defined in parent class"""
        pass

    def teardown_databases(self, old_config, **kwargs):
        """Override the database teardown defined in parent class"""
        pass

    def test_most_expensive_products_context(self):
        response = self.client.get(self.most_expensive_url)
        self.assertTemplateUsed(response, self.template)
