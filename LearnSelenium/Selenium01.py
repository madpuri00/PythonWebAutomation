# Call Selenium
from selenium import webdriver
import pytest


# browser = webdriver.Chrome()
#
# browser.get("https://youtube.com")
# browser.quit()

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    yield driver
    # return driver # value is stored permanently


def test_open_url_verify_title(driver):
    driver.get("https://youtube.com")
    print(driver.title)

    # verification - actual = expected
    assert "YouTube" in driver.title
