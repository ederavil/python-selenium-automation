from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@when('Click on Target circle icon from top of page')
def click_target_circle(context):
    context.driver.find_element(By.ID, "utilityNav-circle").click()


@then('Verify Target circle page is opened')
def verify_target_circle_page(context):
    expected_text = 'Meet the new Target Circle'
    actual_text = context.driver.find_element(By.XPATH, "//span[contains(text(),'Meet the')]").text
    assert expected_text in actual_text, f'Expected text {expected_text} is not in actual text {actual_text}. '


@then('Verify there is {amount} links on page')
def verify_links_on_page(context, amount):
    amount = int(amount)
    links = context.driver.find_elements(By.CSS_SELECTOR, "[data-test='@web/slingshot-components/CellsComponent/Link']")
    assert len(links) == amount, f'Only {len(links)} present out of {amount}'
