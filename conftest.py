import pytest

from data.users import VALID_USER
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage   


@pytest.fixture
def login_page(page):
    return LoginPage(page)

@pytest.fixture
def inventory_page(page):
    return InventoryPage(page)

@pytest.fixture
def authenticated_inventory_page (login_page, inventory_page):
    login_page.open()

    login_page.login(
        VALID_USER["username"],
        VALID_USER["password"]
    )
    
    inventory_page.wait_until_loaded()
    return inventory_page