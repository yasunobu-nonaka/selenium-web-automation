from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SearchResultsPage:
    def __init__(self, driver):
        self.driver = driver

    def wait_until_opened(self, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.url_contains("/search-results")
        )
        WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((By.TAG_NAME, "h2"))
        )

    def has_results(self):
        return len(self.driver.find_elements(By.CLASS_NAME, "hotel")) > 0

    def select_first_hotel(self):
        self.driver.find_element(By.CLASS_NAME, "select-btn").click()

    def get_no_results_message(self):
        return self.driver.find_element(By.ID, "no-results").text
