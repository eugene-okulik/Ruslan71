import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    yield chrome_driver
    chrome_driver.quit()


def test_input_simple(driver):
    input_text = 'homework_25_test'
    driver.get('https://www.qa-practice.com/elements/input/simple')
    text_field = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.NAME, 'text_string'))
    )
    text_field.send_keys(input_text)
    text_field.send_keys(Keys.ENTER)
    result = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.ID, 'result-text'))
    )
    print(result.text)
    assert result.text == input_text


def test_practice_form(driver):
    driver.get('https://demoqa.com/automation-practice-form')
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'firstName'))
    )
    driver.find_element(By.ID, 'firstName').send_keys('Ruslan')
    driver.find_element(By.ID, 'lastName').send_keys('Bochin')
    driver.find_element(By.ID, 'userEmail').send_keys('ruslan.test@mail.com')
    driver.find_element(By.XPATH, '//label[text()="Male"]').click()
    driver.find_element(By.ID, 'userNumber').send_keys('9998887766')

    driver.find_element(By.ID, 'dateOfBirthInput').click()
    Select(driver.find_element(By.CLASS_NAME, 'react-datepicker__month-select')).select_by_value('0')
    Select(driver.find_element(By.CLASS_NAME, 'react-datepicker__year-select')).select_by_value('1995')
    driver.find_element(By.XPATH, '//div[contains(@class, "react-datepicker__day") and text()="15"]').click()

    subjects = driver.find_element(By.ID, 'subjectsInput')
    subjects.send_keys('Maths')
    subjects.send_keys(Keys.ENTER)
    driver.find_element(By.ID, 'hobbies-checkbox-1').click()
    driver.find_element(By.ID, 'currentAddress').send_keys('Moscow')

    driver.find_element(By.ID, 'state').click()
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//div[text()="NCR"]'))).click()
    driver.find_element(By.ID, 'city').click()
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//div[text()="Delhi"]'))).click()

    driver.find_element(By.ID, 'submit').click()
    modal = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, 'modal-content'))
    )
    print(modal.text)
    assert 'Ruslan' in modal.text
    assert 'Bochin' in modal.text


def test_single_select(driver):
    selected_language = 'Python'
    driver.get('https://www.qa-practice.com/elements/select/single_select')
    select_element = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.ID, 'id_choose_language'))
    )
    Select(select_element).select_by_visible_text(selected_language)
    driver.find_element(By.NAME, 'submit').click()
    result = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.ID, 'result-text'))
    )
    print(result.text)
    assert selected_language in result.text


def test_dynamic_loading(driver):
    driver.get('https://the-internet.herokuapp.com/dynamic_loading/2')
    start_button = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '#start button'))
    )
    start_button.click()
    hello_text = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, 'finish'))
    )
    print(hello_text.text)
    assert hello_text.text == 'Hello World!'
