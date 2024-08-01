from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


color_options = (By.CSS_SELECTOR, "div[aria-label='Carousel'] li")
selected_color = (By.CSS_SELECTOR, "[data-test='@web/VariationComponent'] div")


@given('Open product page for {product_id}')
def open_product_page(context, product_id):
    context.driver.get(f'https://www.target.com/p/{product_id}')
    sleep(8)


@then('Verify the colors can be chosen')
def click_colors(context):
    expected_colors = ['Blush', 'Fresh Mint', 'Lavender', 'Tart Orange']
    actual_colors = []

    colors = context.driver.find_elements(*color_options)
    for color in colors:
        color.click()

        select_color = context.driver.find_element(*selected_color).text
        print('Current color', select_color)

        select_color = select_color.split('\n')[1]
        actual_colors.append(select_color)
        print(actual_colors)

    assert expected_colors == actual_colors, f'Expected colors {expected_colors} is not the actual colors {actual_colors}'
