from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


@when('Click on Sign in')
def click_sign_in(context):
    context.app.header.user_sign_in()


@when('Click on Sign in from side menu')
def click_sign_in_on_side(context):
    context.app.header.side_sign_in()


@then('Verify sign in form opens')
def sign_in_shown(context):
    context.app.sign_in_page.verify_sign_in_txt()
