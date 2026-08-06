from playwright.sync_api import expect
import allure

from test_UI_ruslan_bochin_pw.pages.base_page import BasePage
from test_UI_ruslan_bochin_pw.pages.locators.shop import ProductLocators as Loc


class ProductPage(BasePage):
    page_url = '/shop/furn-9999-office-design-software-7?category=9'

    @allure.step('Check product title')
    def check_product_title(self, title):
        expect(self.find(Loc.PRODUCT_TITLE)).to_have_text(title)

    @allure.step('Check product price')
    def check_product_price(self, price):
        expect(self.find(Loc.PRODUCT_PRICE).first).to_have_text(price)

    @allure.step('Check add to cart button is visible')
    def check_add_to_cart_button_is_visible(self):
        expect(self.find(Loc.ADD_TO_CART_BUTTON)).to_be_visible()

    @allure.step('Check quantity input value')
    def check_quantity_value(self, value):
        expect(self.find(Loc.QUANTITY_INPUT)).to_have_value(value)

    @allure.step('Click add to cart')
    def click_add_to_cart(self):
        self.find(Loc.ADD_TO_CART_BUTTON).click()
