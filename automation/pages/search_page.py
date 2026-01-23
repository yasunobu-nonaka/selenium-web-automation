from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from automation.pages.base_page import BasePage

class SearchPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "http://127.0.0.1:5000/search"

    def wait_until_opened(self, timeout=10):
        self.wait_for_url("/search")

    def search(self, location, checkin, checkout, guests, timeout=10):
        self.wait_for_element((By.ID, "location")).send_keys(location)
        self.driver.find_element(By.ID, "checkin").send_keys(checkin)
        self.driver.find_element(By.ID, "checkout").send_keys(checkout)
        self.driver.find_element(By.ID, "guests").send_keys(str(guests))
        self.driver.find_element(By.ID, "search-btn").click()

        try:
            self.wait_for_url("/search-results")
        except TimeoutException:
            raise AssertionError("検索後の画面遷移が確認できませんでした")
