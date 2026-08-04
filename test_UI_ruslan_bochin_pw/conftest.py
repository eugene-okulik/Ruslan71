from playwright.sync_api import BrowserContext
import pytest

from test_UI_ruslan_bochin_pw.pages.cart_page import CartPage
from test_UI_ruslan_bochin_pw.pages.desks_page import DesksPage
from test_UI_ruslan_bochin_pw.pages.product_page import ProductPage


@pytest.fixture()
def page(context: BrowserContext, playwright):
    playwright.selectors.set_test_id_attribute("id")
    page = context.new_page()
    page.set_viewport_size({'width': 1920, 'height': 1080})
    return page


@pytest.fixture()
def cart_page(page):
    return CartPage(page)


@pytest.fixture()
def desks_page(page):
    return DesksPage(page)


@pytest.fixture()
def product_page(page):
    return ProductPage(page)
