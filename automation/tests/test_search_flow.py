from automation.pages.login_page import LoginPage
from automation.pages.search_page import SearchPage
from automation.pages.dashboard_page import DashboardPage

def test_login_and_search(driver):
    login = LoginPage(driver)
    search = SearchPage(driver)
    dashboard = DashboardPage(driver)

    # 1. Login
    login.open()
    result = login.login("testuser", "password123")
    assert result == "success"

    # 2. Search
    search.wait_until_opened()
    search.search("Tokyo", "2026-05-01", "2026-05-02", 2)

    # 3. Dashboard
    welcome = dashboard.get_welcome_text()
    assert "testuser" in welcome
