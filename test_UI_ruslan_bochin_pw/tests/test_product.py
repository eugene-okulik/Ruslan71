import allure


@allure.feature('Product page')
def test_product_title(product_page):
    product_page.open()
    product_page.check_product_title('Office Design Software')


@allure.feature('Product page')
def test_product_price(product_page):
    product_page.open()
    product_page.check_product_price('280.00')


@allure.feature('Product page')
def test_add_to_cart_button_and_quantity(product_page):
    product_page.open()
    product_page.check_add_to_cart_button_is_visible()
    product_page.check_quantity_value('1')
