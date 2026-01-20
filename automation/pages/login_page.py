from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "http://127.0.0.1:5000/"

    def open(self):
        self.driver.get(self.url)

    def login(self, username, password):
        wait = WebDriverWait(self.driver, 10)

        wait.until(EC.presence_of_element_located((By.ID, "username"))).send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-btn").click()