from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DashboardPage:
    def __init__(self, driver):
        self.driver = driver

    def get_welcome_text(self):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(
            EC.presence_of_element_located((By.TAG_NAME, "h2"))
        ).text
