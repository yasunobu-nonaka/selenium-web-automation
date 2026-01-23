from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from automation.pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "http://127.0.0.1:5000/"

    def open(self):
        self.driver.get(self.url)

    def login(self, username, password, timeout=10):
        self.wait_for_element((By.ID, "username")).send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-btn").click()

        try:
            WebDriverWait(self.driver, timeout).until(
                lambda d: "/search" in d.current_url
                or self._has_login_error()
            )
        except TimeoutException:
            raise AssertionError("ログイン結果が確定しませんでした")
        
        if "/search" in self.driver.current_url:
            return "success"
        else:
            return "failure"
        
    def _has_login_error(self):
        return len(self.driver.find_elements(By.CSS_SELECTOR, "p")) > 0
    
    def get_error_text(self):
        return self.driver.find_element(By.CSS_SELECTOR, "p").text
