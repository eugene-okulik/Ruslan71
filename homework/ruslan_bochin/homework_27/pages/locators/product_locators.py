from selenium.webdriver.common.by import By

product_title = (By.TAG_NAME, 'h1')
product_price = (By.CSS_SELECTOR, '.oe_price .oe_currency_value')
add_to_cart_button = (By.ID, 'add_to_cart')
breadcrumb = (By.CSS_SELECTOR, '.breadcrumb')
