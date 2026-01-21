from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class SearchPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "http://127.0.0.1:5000/search"

    def wait_until_opened(self, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((By.TAG_NAME, "h2"))
        )

    def search(self, location, checkin, checkout, guests, timeout=10):
        wait = WebDriverWait(self.driver, timeout)

        wait.until(EC.presence_of_element_located((By.ID, "location"))).send_keys(location)
        self.driver.find_element(By.ID, "checkin").send_keys(checkin)
        self.driver.find_element(By.ID, "checkout").send_keys(checkout)
        self.driver.find_element(By.ID, "guests").send_keys(str(guests))
        self.driver.find_element(By.ID, "search-btn").click()

        try:
            wait.until(
                # EC.presence_of_element_located((By.TAG_NAME, "h2"))
                lambda d: "/search-results" in d.current_url
            )
        except TimeoutException:
            raise AssertionError("検索後の画面遷移が確認できませんでした")
