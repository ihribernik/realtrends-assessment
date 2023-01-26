from decouple import config
GRANT_TYPE = "authorization_code"
SEARCH_CATEGORY = "MLA352679"
SORT_BY_PRICE_DESC = "price_desc"
SORT_BY_SOLD_QUANTITY_ASC = "sold_quantity_asc"
LIMIT_PRICE_DESC = 21
LIMIT_SOLD_QUANTITY = 6
SEARCH_URL = "/sites/MLA/search?{}"
MELI_BASE_URL = "https://auth.mercadolibre.com.ar/authorization?response_type=code&client_id={}&redirect_uri={}"
REDIRECT_LOCAL_URL = "http://localhost:8000/accounts/oauth/redirect/"
