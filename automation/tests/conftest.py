import pytest
from automation.driver import create_driver

@pytest.fixture
def driver():
    driver = create_driver()
    yield driver
    driver.quit()
