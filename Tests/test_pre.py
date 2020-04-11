

from selenium import webdriver
import pytest

@pytest.fixture()
def test_setup():
    global driver
    driver = webdriver.Chrome()
    driver.get("https://www.google.com/")
    driver.implicitly_wait(5)
    driver.maximize_window()

    yield
    driver.close()
    driver.quit()
    print("Test Completed")

def test_fill_in(test_setup):
    driver.find_element_by_xpath("//input[@name='q']")
    assert driver.title == "Google"

