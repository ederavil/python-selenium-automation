from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep


class Header(Page):
    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")

    def search_product(self):
        self.input_text('chips', *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BTN)
        sleep(6)
