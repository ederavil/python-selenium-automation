from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@then('Verify product image displays for each')
def product_images(context):
    context.driver.find_elements(By.CSS_SELECTOR, "[data-test='@web/ProductCard/ProductCardImage/primary']")


@then('Verify product name displays for each')
def product_names(context):
    context.driver.find_elements(By.CSS_SELECTOR, "[data-test='product-title']")