from automation.pages.login_page import LoginPage
from automation.pages.search_page import SearchPage

def test_login_success(driver):
    login = LoginPage(driver)
    search = SearchPage(driver)

    login.open()
    result = login.login("testuser", "password123")

    assert result == "success"
    search.wait_until_opened()

def test_login_failure(driver):
    login = LoginPage(driver)

    login.open()
    result = login.login("testuser", "wrongpassword")

    assert result == "failure"
    assert "Invalid credentials" in login.get_error_text()
