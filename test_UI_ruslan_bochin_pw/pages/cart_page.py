from playwright.sync_api import expect
import allure

from test_UI_ruslan_bochin_pw.pages.base_page import BasePage
from test_UI_ruslan_bochin_pw.pages.locators.shop import CartLocators as Loc


class CartPage(BasePage):
    page_url = '/shop/cart'

    @allure.step('Check empty cart message')
    def check_empty_cart_message(self, message):
        expect(self.find(Loc.EMPTY_CART_MESSAGE)).to_have_text(message)

    @allure.step('Check order overview title')
    def check_order_overview_title(self, title):
        expect(self.find(Loc.ORDER_OVERVIEW)).to_have_text(title)

    @allure.step('Check review order step is visible')
    def check_review_order_step_is_visible(self):
        expect(self.find(Loc.REVIEW_ORDER).first).to_be_visible()

    @allure.step('Check sign in link is visible')
    def check_sign_in_link_is_visible(self):
        expect(self.find(Loc.SIGN_IN_LINK).first).to_be_visible()
