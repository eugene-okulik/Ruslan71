from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage
from pages.locators import cart_locators as loc

WAIT = 10


class CartPage(BasePage):
    page_url = '/shop/cart'

    def should_have_page_title(self, title):
        WebDriverWait(self.driver, WAIT).until(lambda d: d.title == title)
        assert self.driver.title == title

    def should_show_empty_cart_message(self):
        alert = WebDriverWait(self.driver, WAIT).until(
            EC.visibility_of_element_located(loc.empty_cart_alert)
        )
        assert 'Your cart is empty!' in alert.text

    def should_have_order_overview(self):
        overview = WebDriverWait(self.driver, WAIT).until(
            EC.visibility_of_element_located(loc.order_overview)
        )
        assert overview.text == 'Order overview'
