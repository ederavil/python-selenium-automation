from pages.base_page import Page
from selenium.webdriver.common.by import By


class TermsPage(Page):
    def verify_tc_url(self):
        self.verify_partial_url('/terms-conditions')