from playwright.sync_api import Page

from data.users import VALID_USER
from data.products import BACKPACK 
from pages.login_page import LoginPage
from pages.inventory_page import inventoryPage

def test_add_product_to_cart(page: Page):
    login_page = LoginPage(page)
    inventorypage = inventoryPage(page)

    login_page.open()
    
    login_page.login(
        VALID_USER["username"],
        VALID_USER["password"]
    )

    inventorypage.wait_until_loaded()

    inventorypage.add_product_to_cart(BACKPACK)

    # page.pause()
