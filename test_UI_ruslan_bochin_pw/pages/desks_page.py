from playwright.sync_api import expect
import allure

from test_UI_ruslan_bochin_pw.pages.base_page import BasePage
from test_UI_ruslan_bochin_pw.pages.locators.shop import DesksLocators as Loc


class DesksPage(BasePage):
    page_url = '/shop/category/desks-1'

    @allure.step('Check desks breadcrumb')
    def check_desks_in_breadcrumb(self):
        expect(self.find(Loc.BREADCRUMB)).to_contain_text('Desks')

    @allure.step('Check products are displayed')
    def check_products_are_displayed(self):
        expect(self.find(Loc.PRODUCT_NAME).first).to_be_visible()
        assert self.find(Loc.PRODUCT_NAME).count() > 0

    @allure.step('Check customizable desk product')
    def check_customizable_desk_is_visible(self):
        expect(self.page.get_by_text('Customizable Desk').first).to_be_visible()

    @allure.step('Check sort by is visible')
    def check_sort_by_is_visible(self):
        expect(self.find(Loc.SORT_BY).first).to_be_visible()
