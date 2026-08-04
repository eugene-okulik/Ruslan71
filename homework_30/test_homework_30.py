from playwright.sync_api import Page, expect, Route
import json


def test_iphone_popup_title(page: Page):
    new_title = 'яблокофон 17 про'

    def handle_route(route: Route):
        response = route.fetch()
        body = response.json()
        body['body']['digitalMat'][0]['familyTypes'][0]['productName'] = new_title
        body = json.dumps(body)
        route.fulfill(
            response=response,
            body=body
        )

    page.route('**/digital-mat**', handle_route)
    page.goto('https://www.apple.com/shop/buy-iphone', wait_until='domcontentloaded')
    page.locator('[data-autom="DigitalMat-1"]').click()
    expect(page.locator('[data-autom="DigitalMat-overlay-header-0-0"]')).to_have_text(new_title)
