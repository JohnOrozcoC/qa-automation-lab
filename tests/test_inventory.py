import pytest
from data.products import BACKPACK 

@pytest.mark.smoke
@pytest.mark.cart

def test_add_product_to_cart(authenticated_inventory_page):
    authenticated_inventory_page.add_product_to_cart(BACKPACK)
    authenticated_inventory_page.validate_cart_quantity(1)
   # page.pause()
