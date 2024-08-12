from selenium.webdriver.common.by import By
from pages.base_page import Page


class SearchResultsPage(Page):
    SEARCH_RESULTS_TEXT = (By.XPATH, "//div[@data-test='resultsHeading']")

    def verify_text(self):
        actual_text = self.driver.find_element(*self.SEARCH_RESULTS_TEXT).text
        assert 'chips' in actual_text, f'Expected text to be chips and it is {actual_text}'

    def verify_url(self):
        url = self.driver.current_url
        assert 'chips' in url, f'Expected "chips" not in {url}'

