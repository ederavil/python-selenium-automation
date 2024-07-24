from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep



@then('Add Doritos cool ranch to cart')
def add_doritos_to_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, "[aria-label *= 'Add Doritos Cool']").click()
    sleep(3)
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='orderPickupButton']").click()
    sleep(3)



@then('Verify Doritos cool ranch is in cart')
def verify_in_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, "[aria-label*='1 in cart for Doritos Cool']")

