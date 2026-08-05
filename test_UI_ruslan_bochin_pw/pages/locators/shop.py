class CartLocators:
    EMPTY_CART_MESSAGE = '.alert'
    ORDER_OVERVIEW = 'h3'
    REVIEW_ORDER = 'text=Review Order'
    SIGN_IN_LINK = 'a:has-text("Sign in")'


class DesksLocators:
    BREADCRUMB = '.breadcrumb'
    PRODUCT_NAME = 'a[itemprop="name"]'
    SORT_BY = 'small:has-text("Sort By")'
    CUSTOMIZABLE_DESK = 'text=Customizable Desk'


class ProductLocators:
    PRODUCT_TITLE = 'h1'
    PRODUCT_PRICE = '.oe_currency_value'
    ADD_TO_CART_BUTTON = '#add_to_cart'
    QUANTITY_INPUT = 'input[name="add_qty"]'
