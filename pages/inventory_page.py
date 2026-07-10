from playwright.sync_api import Page, expect

class inventoryPage:

    def __init__(self, page : Page):
        self.page = page
        self.title = page.get_by_text("Products")
        self.products = page.locator(".inventory_item")
        self.add_to_cart_buttons = page.get_by_role("button", name="Add to cart")
        self.cart_icon = page.locator(".shopping_cart_link")

    def wait_until_loaded(self):
        expect(self.title).to_be_visible()
        expect(self.products.first).to_be_visible()
        expect(self.add_to_cart_buttons.first).to_be_visible()

    def add_product_to_cart(self,product_name: str):
        product = self.page.get_by_text(product_name)
        expect(product).to_be_visible()

        add_button = self.page.locator(
            f"xpath=//div[text()='{product_name}']/ancestor::div[@class='inventory_item']//button"
        )

        add_button.click()

    def open_cart(self):
        self.cart_icon.click()





    
        

