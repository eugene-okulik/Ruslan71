from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage
from pages.locators import product_locators as loc

WAIT = 10


class ProductPage(BasePage):
    page_url = '/shop/furn-9999-office-design-software-7?category=9'

    def should_have_product_title(self, title):
        product_title = WebDriverWait(self.driver, WAIT).until(
            EC.visibility_of_element_located(loc.product_title)
        )
        assert product_title.text == title

    def should_have_price(self, price):
        product_price = WebDriverWait(self.driver, WAIT).until(
            EC.visibility_of_element_located(loc.product_price)
        )
        assert product_price.text == price

    def should_have_add_to_cart_button(self):
        button = WebDriverWait(self.driver, WAIT).until(
            EC.element_to_be_clickable(loc.add_to_cart_button)
        )
        assert 'Add to cart' in button.text
