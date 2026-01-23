from selenium.webdriver.common.by import By
from automation.pages.base_page import BasePage

class SearchResultsPage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    def wait_until_opened(self, timeout=10):
        self.wait_for_url("/search-results")
        self.wait_for_element((By.TAG_NAME, "h2"))

    def has_results(self):
        return len(self.driver.find_elements(By.CLASS_NAME, "hotel")) > 0

    def select_first_hotel(self):
        self.driver.find_element(By.CLASS_NAME, "select-btn").click()

    def get_no_results_message(self):
        return self.driver.find_element(By.ID, "no-results").text
