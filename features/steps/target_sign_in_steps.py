from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@when('Click on Sign in')
def click_sign_in(context):
    context.driver.find_element(By.XPATH, "//span[contains(@class, 'sc-58ad44c0-3')]").click()
    sleep(2)


@when('Click on Sign in from side menu')
def click_sign_in_on_side(context):
    context.driver.find_element(By.XPATH, "//span[contains(@class, 'sc-859e7637-0') and text()='Sign in']").click()
    sleep(3)


@then('Verify sign in form opens')
def sign_in_shown(context):
    context.driver.find_element(By.XPATH, "//span[text()='Sign into your Target account']")
