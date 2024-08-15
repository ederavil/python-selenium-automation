from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep


class Header(Page):
    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
    SIGN_IN_BTN = (By.XPATH, "//span[contains(@class, 'sc-58ad44c0-3')]")
    SIGN_SIGN_IN_BTN = (By.XPATH, "//span[contains(@class, 'sc-859e7637-0') and text()='Sign in']")

    def search_product(self, product):
        print('POM layer:', product)
        self.input_text(product, *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BTN)
        sleep(6)

    def user_sign_in(self):
        self.click(*self.SIGN_IN_BTN)

    def side_sign_in(self):
        self.wait_and_click(*self.SIGN_SIGN_IN_BTN)


