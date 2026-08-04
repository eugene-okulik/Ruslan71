from playwright.sync_api import expect
import allure

from test_UI_ruslan_bochin_pw.pages.base_page import BasePage
from test_UI_ruslan_bochin_pw.pages.locators.shop import CartLocators as Loc


class CartPage(BasePage):
    page_url = '/shop/cart'

    @allure.step('Check empty cart message')
    def check_empty_cart_message(self):
        expect(self.find(Loc.EMPTY_CART_MESSAGE)).to_have_text('Your cart is empty!')

    @allure.step('Check order overview title')
    def check_order_overview_title(self):
        expect(self.find(Loc.ORDER_OVERVIEW)).to_have_text('Order overview')

    @allure.step('Check review order step is visible')
    def check_review_order_step_is_visible(self):
        expect(self.page.get_by_text('Review Order').first).to_be_visible()

    @allure.step('Check sign in link is visible')
    def check_sign_in_link_is_visible(self):
        expect(self.page.get_by_role('link', name='Sign in').first).to_be_visible()
