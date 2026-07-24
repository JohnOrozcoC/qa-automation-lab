import pytest
from data.users import VALID_USER

@pytest.mark.smoke
@pytest.mark.critical
@pytest.mark.login

def test_successful_login(login_page, inventory_page):

    login_page.open()
    login_page.login(
        VALID_USER["username"],
        VALID_USER["password"]
    )

    inventory_page.wait_until_loaded()





 