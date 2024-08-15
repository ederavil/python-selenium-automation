from pages.base_page import Page
from selenium.webdriver.common.by import By


class SignInPage(Page):
    SIGN_IN_TEXT = (By.XPATH, "//span[text()='Sign into your Target account']")

    def verify_sign_in_txt(self):
        self.driver.find_element(*self.SIGN_IN_TEXT)