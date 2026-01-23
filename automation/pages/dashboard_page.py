from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from automation.pages.base_page import BasePage

class DashboardPage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    def wait_until_opened(self, timeout=10):
        self.wait_for_url("/dashboard")

    def get_welcome_text(self):
        self.wait_until_opened()
        return self.wait_for_element((By.TAG_NAME, "h2")).text

    def get_reserved_hotel(self):
        return self.wait_for_element((By.ID, "hotel-name")).text
    