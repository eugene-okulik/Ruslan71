from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage
from pages.locators import category_locators as loc

WAIT = 10


class CategoryPage(BasePage):
    page_url = '/shop/category/desks-1'

    def should_have_desks_in_breadcrumb(self):
        breadcrumb = WebDriverWait(self.driver, WAIT).until(
            EC.visibility_of_element_located(loc.breadcrumb)
        )
        assert 'Desks' in breadcrumb.text

    def should_have_products(self, min_count=1):
        products = WebDriverWait(self.driver, WAIT).until(
            lambda d: d.find_elements(*loc.product_card)
        )
        assert len(products) >= min_count

    def should_contain_product(self, product_name):
        titles = WebDriverWait(self.driver, WAIT).until(
            lambda d: d.find_elements(*loc.product_title)
        )
        product_names = [title.text for title in titles]
        assert product_name in product_names
