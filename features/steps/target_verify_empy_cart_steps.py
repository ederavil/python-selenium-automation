from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given('Open Target Main Page')
def open_target(context):
    context.app.main_page.open()


@when('Click on cart icon')
def click_cart_icon(context):
    context.driver.find_element(By.CSS_SELECTOR, "use[href*='/icons/Cart']").click()


@then('Verify empty cart message shown is shown')
def verify_empty_cart_message(context):
    expected_text = 'Your cart is empty'
    actual_text = context.driver.find_element(By.XPATH, "//h1[contains(text(),'Your cart')]").text
    assert expected_text in actual_text, f'Expected text {expected_text} is not actual text {actual_text}.'



