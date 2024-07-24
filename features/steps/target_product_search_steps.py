from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@when('Search for {product}')
def search_chips(context, product):
    context.driver.find_element(By.ID, 'search').send_keys(product)
    context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
    sleep(9)


@then('Verify search results show {product}')
def verify_chips_in_search(context, product):
    actual_text = context.driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
    assert product in actual_text, f'Expected text {product} is not actual text {actual_text}.'


@then('Verify intended URL is shown with {product} within')
def product_url(context, product):
    url = context.driver.current_url
    assert product in url, f"{product} is not within the current url"