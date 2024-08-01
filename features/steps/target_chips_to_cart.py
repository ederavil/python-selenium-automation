from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


cheetos_in_cart = (By.CSS_SELECTOR, "[aria-label*='1 in cart for Cheetos Jumbo']")
@then('Add Cheetos to cart')
def add_cheetos_to_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, "[aria-label *= 'Add Cheetos Jumbo']").click()
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='orderPickupButton']").click()


@then('Verify Cheetos Jumbo is in cart')
def verify_in_cart(context):
    context.driver.wait.until(EC.visibility_of_element_located(cheetos_in_cart))
    context.driver.find_element(By.CSS_SELECTOR, "[aria-label*='1 in cart for Cheetos Jumbo']")

