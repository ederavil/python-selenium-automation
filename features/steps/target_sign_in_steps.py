from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


side_sign_in_btn = (By.XPATH, "//span[contains(@class, 'sc-859e7637-0') and text()='Sign in']")
@when('Click on Sign in')
def click_sign_in(context):
    context.driver.find_element(By.XPATH, "//span[contains(@class, 'sc-58ad44c0-3')]").click()



@when('Click on Sign in from side menu')
def click_sign_in_on_side(context):
    context.driver.wait.until(EC.element_to_be_clickable(side_sign_in_btn))
    context.driver.find_element(By.XPATH, "//span[contains(@class, 'sc-859e7637-0') and text()='Sign in']").click()



@then('Verify sign in form opens')
def sign_in_shown(context):
    context.driver.find_element(By.XPATH, "//span[text()='Sign into your Target account']")
