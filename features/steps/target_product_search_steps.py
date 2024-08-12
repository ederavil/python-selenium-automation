from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC


@when('Search for {product}')
def search_chips(context, product):
    context.app.header.search_product()


@then('Verify search results show {product}')
def verify_chips_in_search(context, product):
    context.app.search_results_page.verify_text()


@then('Verify intended URL is shown with {product} within')
def product_url(context, product):
    context.app.search_results_page.verify_url()

