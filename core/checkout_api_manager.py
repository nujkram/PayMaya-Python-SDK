import base64
from typing import Dict

from core.constants import PRODUCTION, CHECKOUT_PRODUCTION_URL, CHECKOUT_SANDBOX_URL
from paymaya_sdk import PayMayaSDK


class CheckoutAPIManager:
    public_api_key: str = None
    secret_api_key: str = None
    environment: str = None
    base_url: str = None
    http_headers: Dict = None

    def __init__(self):
        instance = PayMayaSDK.get_instance()
        self.public_api_key = instance.checkout_public_api_key
        self.secret_api_key = instance.checkout_secret_api_key
        self.environment = instance.checkout_environment
        self.base_url = self.get_base_url()
        self.http_headers = {"Content-Type": "application/json"}

    def get_base_url(self) -> str:
        if self.environment == PRODUCTION:
            url = CHECKOUT_PRODUCTION_URL
        else:
            url = CHECKOUT_SANDBOX_URL

        return url

    def use_basic_auth_with_api_key(self, api_key: str = None):
        if not api_key:
            raise ValueError("API Key is required")

        token = base64.b64encode(api_key.encode("utf-8"))
        self.http_headers["Authorization"] = f"Basic {token.decode()}:"