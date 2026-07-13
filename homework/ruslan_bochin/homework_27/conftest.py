import pytest
from selenium import webdriver

from pages.cart_page import CartPage
from pages.category_page import CategoryPage
from pages.product_page import ProductPage


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    yield chrome_driver
    chrome_driver.quit()


@pytest.fixture()
def cart_page(driver):
    return CartPage(driver)


@pytest.fixture()
def category_page(driver):
    return CategoryPage(driver)


@pytest.fixture()
def product_page(driver):
    return ProductPage(driver)
