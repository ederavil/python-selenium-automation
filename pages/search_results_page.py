from selenium.webdriver.common.by import By
from pages.base_page import Page


class SearchResultsPage(Page):
    SEARCH_RESULTS_TEXT = (By.XPATH, "//div[@data-test='resultsHeading']")
    PRODUCT_SEARCH_RESULTS = (By.CSS_SELECTOR, "[data-test='@web/ProductCard/ProductCardImage/primary']")
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[data-test='orderPickupButton']")
    SIDE_CLOSE_BTN = (By.CSS_SELECTOR, "[aria-label='close']")
    ITEM_QUANTITY = (By.CSS_SELECTOR, "[data-test='cartItem-qty']")

    def verify_text(self):
        actual_text = self.driver.find_element(*self.SEARCH_RESULTS_TEXT).text
        assert 'chips' in actual_text, f'Expected text to be chips and it is {actual_text}'

    def verify_url(self):
        url = self.driver.current_url
        assert 'chips' in url, f'Expected "chips" not in {url}'

    def add_to_cart(self):
        self.wait_and_click(*self.PRODUCT_SEARCH_RESULTS)
        self.wait_and_click(*self.ADD_TO_CART_BTN)

    def verify_product_in_cart(self):
        self.click(*self.SIDE_CLOSE_BTN)
        self.click_cart()
        self.wait_until_clickable(*self.ITEM_QUANTITY)

