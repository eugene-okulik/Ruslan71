import allure


@allure.feature('Cart page')
def test_empty_cart_message(cart_page):
    cart_page.open()
    cart_page.check_empty_cart_message('Your cart is empty!')


@allure.feature('Cart page')
def test_order_overview_title(cart_page):
    cart_page.open()
    cart_page.check_order_overview_title('Order overview')


@allure.feature('Cart page')
def test_review_order_step(cart_page):
    cart_page.open()
    cart_page.check_review_order_step_is_visible()
    cart_page.check_sign_in_link_is_visible()
