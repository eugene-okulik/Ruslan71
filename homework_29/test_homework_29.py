from playwright.sync_api import Page, expect, BrowserContext, Dialog


def test_alert_confirm(page: Page):
    def accept_alert(alert: Dialog):
        alert.accept()

    page.on('dialog', accept_alert)
    page.goto('https://www.qa-practice.com/elements/alert/confirm')
    page.get_by_role('link', name='Click').click()
    expect(page.locator('#result-text')).to_have_text('Ok')


def test_new_tab_button(page: Page, context: BrowserContext):
    page.goto('https://www.qa-practice.com/elements/new_tab/button')
    button = page.locator('#new-page-button')
    with context.expect_page() as new_page_event:
        button.click()
    new_page = new_page_event.value
    expect(new_page.locator('#result-text')).to_have_text('I am a new page in a new tab')
    new_page.close()
    expect(button).to_be_enabled()


def test_color_change(page: Page):
    page.goto('https://demoqa.com/dynamic-properties')
    button = page.locator('#colorChange')
    expect(button).to_have_class('mt-4 text-danger btn btn-primary', timeout=10000)
    button.click()
