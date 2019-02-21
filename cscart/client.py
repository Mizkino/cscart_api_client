import requests
import json
import base64
from logging import basicConfig, getLogger, DEBUG
from typing import Dict, Any

logger = getLogger(__name__)


class Client:
    def __init__(self, url_base: str, email: str, api_key: str) -> None:
        self.url_base = url_base
        self.authorization = "Basic " + base64.b64encode(
            f"{email}:{api_key}".encode("utf-8")
        ).decode("utf-8")

    def _get_API(self, url: str) -> requests.Response:
        return requests.get(url, headers={"authorization": self.authorization})

    def get_categories(
        self, category_id: int = None, params: Dict[str, Any] = {}
    ) -> requests.Response:
        url = (
            self.url_base
            + "categories"
            + ("" if category_id is None else f"/{category_id}")
        )
        url = url + (
            ""
            if not params
            else "?" + "&".join([f"{k}={v}" for k, v in params.items()])
        )
        return self._get_API(url)

    def get_orders(
        self, order_id: int = None, params: Dict[str, Any] = {}
    ) -> requests.Response:
        url = self.url_base + "orders" + ("" if order_id is None else f"/{order_id}")
        url = url + (
            ""
            if not params
            else "?" + "&".join([f"{k}={v}" for k, v in params.items()])
        )
        return self._get_API(url)

    def get_payment_methods(
        self, payment_id: int = None, params: Dict[str, Any] = {}
    ) -> requests.Response:
        url = (
            self.url_base
            + "payments"
            + ("" if payment_id is None else f"/{payment_id}")
        )
        url = url + (
            ""
            if not params
            else "?" + "&".join([f"{k}={v}" for k, v in params.items()])
        )
        return self._get_API(url)

    def get_product_features(
        self,
        feature_id: int = None,
        product_id: int = None,
        params: Dict[str, Any] = {},
    ) -> requests.Response:
        url = self.url_base + ("" if product_id is None else f"products/{product_id}/")
        url = url + "features" + ("" if feature_id is None else f"/{feature_id}")
        url = url + (
            ""
            if not params
            else "?" + "&".join([f"{k}={v}" for k, v in params.items()])
        )
        return self._get_API(url)

    def get_products(
        self,
        product_id: int = None,
        category_id: int = None,
        params: Dict[str, Any] = {},
    ) -> requests.Response:
        url = self.url_base + (
            "" if category_id is None else f"categories/{category_id}/"
        )
        url = url + "products" + ("" if product_id is None else f"/{product_id}")
        url = url + (
            ""
            if not params
            else "?" + "&".join([f"{k}={v}" for k, v in params.items()])
        )
        return self._get_API(url)

    def get_settings(
        self, setting_id: int = None, params: Dict[str, Any] = {}
    ) -> requests.Response:
        url = (
            self.url_base
            + "settings"
            + ("" if setting_id is None else f"/{setting_id}")
        )
        url = url + (
            ""
            if not params
            else "?" + "&".join([f"{k}={v}" for k, v in params.items()])
        )
        return self._get_API(url)

    def get_shipments(
        self, shipment_id: int = None, params: Dict[str, Any] = {}
    ) -> requests.Response:
        url = (
            self.url_base
            + "shipments"
            + ("" if shipment_id is None else f"/{shipment_id}")
        )
        url = url + (
            ""
            if not params
            else "?" + "&".join([f"{k}={v}" for k, v in params.items()])
        )
        return self._get_API(url)

    def get_shipping_methods(
        self, shipping_id: int = None, params: Dict[str, Any] = {}
    ) -> requests.Response:
        url = (
            self.url_base
            + "shippings"
            + ("" if shipping_id is None else f"/{shipping_id}")
        )
        url = url + (
            ""
            if not params
            else "?" + "&".join([f"{k}={v}" for k, v in params.items()])
        )
        return self._get_API(url)

    def get_statuses(
        self, statuse_id: int = None, params: Dict[str, Any] = {}
    ) -> requests.Response:
        url = (
            self.url_base
            + "statuses"
            + ("" if statuse_id is None else f"/{statuse_id}")
        )
        url = url + (
            ""
            if not params
            else "?" + "&".join([f"{k}={v}" for k, v in params.items()])
        )
        return self._get_API(url)

    def get_stores(
        self, store_id: int = None, params: Dict[str, Any] = {}
    ) -> requests.Response:
        url = self.url_base + "stores" + ("" if store_id is None else f"/{store_id}")
        url = url + (
            ""
            if not params
            else "?" + "&".join([f"{k}={v}" for k, v in params.items()])
        )
        return self._get_API(url)

    def get_taxes(
        self, taxe_id: int = None, params: Dict[str, Any] = {}
    ) -> requests.Response:
        url = self.url_base + "taxes" + ("" if taxe_id is None else f"/{taxe_id}")
        url = url + (
            ""
            if not params
            else "?" + "&".join([f"{k}={v}" for k, v in params.items()])
        )
        return self._get_API(url)

    def get_users(
        self, user_id: int = None, params: Dict[str, Any] = {}
    ) -> requests.Response:
        url = self.url_base + "users" + ("" if user_id is None else f"/{user_id}")
        url = url + (
            ""
            if not params
            else "?" + "&".join([f"{k}={v}" for k, v in params.items()])
        )
        return self._get_API(url)

    def get_usergroups(
        self, usergroup_id: int = None, user_id: int = None, params: Dict[str, Any] = {}
    ) -> requests.Response:
        url = self.url_base + ("" if user_id is None else f"users/{user_id}/")
        url = url + "usergroups" + ("" if usergroup_id is None else f"/{usergroup_id}")
        url = url + (
            ""
            if not params
            else "?" + "&".join([f"{k}={v}" for k, v in params.items()])
        )
        return self._get_API(url)


if __name__ == "__main__":

    basicConfig(format="%(asctime)s : %(threadName)s : %(levelname)s : %(message)s")
    logger.setLevel(DEBUG)

    f = open("config.json", encoding="utf-8")
    config = json.load(f)
    f.close()
    url_base = config["cscart"]["url_base"]
    email = config["cscart"]["email"]
    api_key = config["cscart"]["api_key"]
    c = Client(url_base, email, api_key)
    logger.debug(f"url_base :{url_base}, email :{email}, api_key:{api_key}")

    params = {"page": 1, "items_per_page": 1}
    logger.debug(c.get_categories(params=params).json())
    logger.debug(c.get_orders(params=params).json())
    logger.debug(c.get_payment_methods(params=params).json())
    logger.debug(c.get_product_features(params=params).json())
    logger.debug(c.get_products(params=params).json())
    logger.debug(c.get_settings(params=params).json())
    logger.debug(c.get_shipments(params=params).json())
    logger.debug(c.get_shipping_methods(params=params).json())
    logger.debug(c.get_statuses(params=params).json())
    logger.debug(c.get_stores(params=params).json())
    logger.debug(c.get_taxes(params=params).json())
    logger.debug(c.get_users(params=params).json())
