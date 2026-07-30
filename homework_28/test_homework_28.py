from playwright.sync_api import Page, expect


def test_get_by_role(page: Page):
    page.goto('https://the-internet.herokuapp.com/')
    page.get_by_role('link', name='Form Authentication').click()
    page.get_by_role('textbox', name='Username').fill('tomsmith')
    page.get_by_role('textbox', name='Password').fill('SuperSecretPassword!')
    page.get_by_role('button', name='Login').click()
    expect(page.get_by_role('heading', name='Secure Area', exact=True)).to_be_visible()


def test_practice_form(page: Page):
    page.goto('https://demoqa.com/automation-practice-form')
    page.get_by_placeholder('First Name').fill('Ruslan')
    page.get_by_placeholder('Last Name').fill('Bochin')
    page.get_by_placeholder('name@example.com').fill('ruslan@test.com')
    page.locator('label[for="gender-radio-1"]').click()
    page.get_by_placeholder('Mobile Number').fill('1234567890')
    page.locator('#dateOfBirthInput').click()
    page.locator('.react-datepicker__month-select').select_option('June')
    page.locator('.react-datepicker__year-select').select_option('1999')
    page.locator('.react-datepicker__day--015:not(.react-datepicker__day--outside-month)').click()
    page.locator('#subjectsInput').fill('Maths')
    page.keyboard.press('Enter')
    page.locator('label[for="hobbies-checkbox-1"]').click()
    page.get_by_placeholder('Current Address').fill('Moscow')
    page.locator('#state').click()
    page.get_by_text('NCR', exact=True).click()
    page.locator('#city').click()
    page.get_by_text('Delhi', exact=True).click()
    page.locator('#submit').click()
    expect(page.locator('#example-modal-sizes-title-lg')).to_have_text('Thanks for submitting the form')
