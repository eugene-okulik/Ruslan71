import pytest


@pytest.mark.cart
def test_cart_page_title(cart_page):
    cart_page.open_page()
    cart_page.should_have_page_title('Shopping Cart | My Website')


@pytest.mark.cart
def test_empty_cart_message(cart_page):
    cart_page.open_page()
    cart_page.should_show_empty_cart_message()


@pytest.mark.cart
def test_cart_order_overview(cart_page):
    cart_page.open_page()
    cart_page.should_have_order_overview()


@pytest.mark.category
def test_category_breadcrumb(category_page):
    category_page.open_page()
    category_page.should_have_desks_in_breadcrumb()


@pytest.mark.category
def test_category_has_products(category_page):
    category_page.open_page()
    category_page.should_have_products(min_count=5)


@pytest.mark.category
def test_category_contains_customizable_desk(category_page):
    category_page.open_page()
    category_page.should_contain_product('Customizable Desk')


@pytest.mark.product
def test_product_title(product_page):
    product_page.open_page()
    product_page.should_have_product_title('Office Design Software')


@pytest.mark.product
def test_product_price(product_page):
    product_page.open_page()
    product_page.should_have_price('280.00')


@pytest.mark.product
def test_product_add_to_cart_button(product_page):
    product_page.open_page()
    product_page.should_have_add_to_cart_button()
