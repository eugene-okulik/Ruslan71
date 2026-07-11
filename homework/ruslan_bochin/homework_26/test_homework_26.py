import pytest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

SHOP_URL = 'http://testshop.qa-practice.com/'
PRODUCT_NAME = 'Customizable Desk'
WAIT = 10


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    yield chrome_driver
    chrome_driver.quit()


def test_add_to_cart_in_new_tab(driver):
    driver.get(SHOP_URL)
    main_tab = driver.current_window_handle
    product = WebDriverWait(driver, WAIT).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '[alt="Customizable Desk"]'))
    )
    ActionChains(driver).key_down(Keys.CONTROL).click(product).key_up(Keys.CONTROL).perform()

    WebDriverWait(driver, WAIT).until(lambda d: len(d.window_handles) > 1)
    product_tab = [tab for tab in driver.window_handles if tab != main_tab][0]
    driver.switch_to.window(product_tab)

    add_to_cart = WebDriverWait(driver, WAIT).until(
        EC.element_to_be_clickable((By.ID, 'add_to_cart'))
    )
    add_to_cart.click()
    WebDriverWait(driver, WAIT).until(
        EC.element_to_be_clickable((By.XPATH, '//*[text()="Continue Shopping"]'))
    ).click()
    WebDriverWait(driver, WAIT).until(
        lambda d: d.find_element(By.CSS_SELECTOR, 'sup.my_cart_quantity').text == '1'
    )
    driver.close()
    driver.switch_to.window(main_tab)

    cart_link = WebDriverWait(driver, WAIT).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/shop/cart']"))
    )
    cart_link.click()
    product_in_cart = WebDriverWait(driver, WAIT).until(
        EC.presence_of_element_located(
            (By.XPATH, f"//*[contains(text(), '{PRODUCT_NAME}')]")
        )
    )
    assert PRODUCT_NAME in product_in_cart.text


def test_add_to_cart_on_hover(driver):
    driver.get(SHOP_URL)
    product = WebDriverWait(driver, WAIT).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[alt="Customizable Desk"]'))
    )
    card = product.find_element(By.XPATH, './ancestor::form')
    ActionChains(driver).move_to_element(product).perform()
    cart_button = WebDriverWait(card, WAIT).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'a.a-submit'))
    )
    cart_button.click()

    modal = WebDriverWait(driver, WAIT).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '.modal-content'))
    )
    print(modal.text)
    assert PRODUCT_NAME in modal.text
