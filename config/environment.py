import os

ENVIRONMENT = os.getenv("ENVIRONMENT", "QA")

BASE_URLS = {
    "DEV": "https://www.saucedemo.com/",
    "QA": "https://www.saucedemo.com/",
    "STAGING": "https://www.saucedemo.com/",
}

BASE_URL = BASE_URLS[ENVIRONMENT]