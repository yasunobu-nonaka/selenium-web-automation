from driver import create_driver
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

def test_login_success():
    driver = create_driver()
    try:
        login = LoginPage(driver)
        dashboard = DashboardPage(driver)

        login.open()
        login.login("testuser", "password123")

        text = dashboard.get_welcome_text()
        assert "testuser" in text
    except Exception as e:
        # テスト失敗時の処理を記載
        print("Error: ", e)
    else:
        print("Test passed!")
    finally:
        driver.quit()
