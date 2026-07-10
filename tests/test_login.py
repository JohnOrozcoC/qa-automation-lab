
from playwright.sync_api import Page
from data.users import VALID_USER
from pages.login_page import LoginPage
from pages.inventory_page import inventoryPage

def test_successful_login(page: Page):
    login_page = LoginPage(page)
    inventorypage = inventoryPage(page)

    login_page.open()
    
    login_page.login(
        VALID_USER["username"],
        VALID_USER["password"]
    )

    inventorypage.verify_title()

