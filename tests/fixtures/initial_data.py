import json

from pytest import fixture


def get_file_data(name):
    with open(f"tests/data/{name}", "r") as f:
        return json.load(f)


def get_sorted_by_price_data(self):
    return get_file_data("sorted_by_price_data.json")


def get_best_sellers_data(self):
    return get_file_data("sorted_by_sellers_data.json")


def get_result_sorted_by_price(self):
    return get_file_data("result_sorted_by_price_data.json")


@fixture
def get_sorted_by_price_data_fixture(request):
    request.cls.get_sorted_by_price_data = get_sorted_by_price_data


@fixture
def get_sorted_by_best_sellers_fixture(request):
    request.cls.get_sellers_data = get_best_sellers_data


@fixture
def get_result_sorted_by_price_fixture(request):
    request.cls.get_result_sorted_by_price = get_result_sorted_by_price
