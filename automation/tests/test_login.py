import pytest
from automation.driver import create_driver
from automation.pages.login_page import LoginPage
from automation.pages.dashboard_page import DashboardPage

@pytest.fixture
def driver():
    driver = create_driver()
    yield driver
    driver.quit()

def test_login_success(driver):
    login = LoginPage(driver)
    dashboard = DashboardPage(driver)

    login.open()
    login.login("testuser", "password123")

    assert "testuser" in dashboard.get_welcome_text()
