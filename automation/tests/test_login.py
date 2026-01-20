import time
from automation.pages.login_page import LoginPage
from automation.pages.dashboard_page import DashboardPage

def test_login_success(driver):
    login = LoginPage(driver)
    dashboard = DashboardPage(driver)

    login.open()
    result = login.login("testuser", "password123")
    # login.wait_for_redirect()

    # welcome_text = dashboard.get_welcome_text()

    assert result == "success"
    assert "testuser" in dashboard.get_welcome_text()

def test_login_failure(driver):
    login = LoginPage(driver)

    login.open()
    result = login.login("testuser", "wrongpassword")

    # error_text = login.wait_for_login_error()

    assert result == "failure"
    assert "Invalid credentials" in login.get_error_text()
