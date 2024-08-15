from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


cheetos_in_cart = (By.CSS_SELECTOR, "[aria-label*='1 in cart for Cheetos Jumbo']")


@then('Add {product} to cart')
def add_chips_to_cart(context, product):
    context.driver.execute_script("window.scrollBy(0,2000)", "")
    context.app.search_results_page.add_to_cart()


@then('Verify {product} is in cart')
def verify_in_cart(context, product):
    context.app.search_results_page.verify_product_in_cart()

