from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def create_driver():
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")

    return webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )
