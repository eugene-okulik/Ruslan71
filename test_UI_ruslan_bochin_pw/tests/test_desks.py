import allure


@allure.feature('Desks category')
def test_desks_breadcrumb(desks_page):
    desks_page.open()
    desks_page.check_desks_in_breadcrumb()


@allure.feature('Desks category')
def test_products_are_displayed(desks_page):
    desks_page.open()
    desks_page.check_products_are_displayed()


@allure.feature('Desks category')
def test_customizable_desk_and_sort(desks_page):
    desks_page.open()
    desks_page.check_customizable_desk_is_visible()
    desks_page.check_sort_by_is_visible()
