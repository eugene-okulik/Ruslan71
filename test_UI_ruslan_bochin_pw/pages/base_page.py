from playwright.sync_api import Page, Locator
import allure


class BasePage:
    base_url = 'http://testshop.qa-practice.com'
    page_url = None

    def __init__(self, page: Page):
        self.page = page

    @allure.step('Open the page')
    def open(self):
        if self.page_url:
            self.page.goto(
                f'{self.base_url}{self.page_url}',
                wait_until='domcontentloaded',
                timeout=60000
            )
        else:
            raise NotImplementedError('Page can not be opened by URL for this page')

    @allure.step('Find element by locator')
    def find(self, locator) -> Locator:
        return self.page.locator(locator)
