from automation.pages.login_page import LoginPage
from automation.pages.search_page import SearchPage
from automation.pages.search_results_page import SearchResultsPage
from automation.pages.dashboard_page import DashboardPage

def test_login_search_and_select(driver):
    login = LoginPage(driver)
    search = SearchPage(driver)
    search_results = SearchResultsPage(driver)
    dashboard = DashboardPage(driver)

    # 1. Login
    login.open()
    result = login.login("testuser", "password123")
    assert result == "success"

    # 2. Search
    search.wait_until_opened()
    search.search("Tokyo", "2026-05-01", "2026-05-02", 2)

    # 3. Select from search results
    search_results.wait_until_opened()
    search_results.select_first_hotel()

    # 4. Dashboard
    welcome = dashboard.get_welcome_text()
    assert "testuser" in welcome


def test_search_no_results(driver):
    login = LoginPage(driver)
    search = SearchPage(driver)
    search_results = SearchResultsPage(driver)
    dashboard = DashboardPage(driver)

    login.open()
    result = login.login("testuser", "password123")
    assert result == "success"

    # 2. Search
    search.wait_until_opened()
    search.search("Nowhere", "2026-05-01", "2026-05-02", 1)

    # 3. Search Results
    search_results.wait_until_opened()
    assert not search_results.has_results()
    assert search_results.get_no_results_message()
