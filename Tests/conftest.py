import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--baseurl",
                     action="store",
                     default="https://www.saucedemo.com/",
                     help="base URL for the application under test")
    parser.addoption("--browser",
                     action="store",
                     default="chrome",
                     help="the name is the browser u want to run with")


@pytest.fixture(scope="class")
#@pytest.fixture(scope="session") #u use it when without class, and it will open browser once with all test
def test_setup(request):
    from selenium import webdriver
    browser = request.config.getoption("--browser")
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.FireFox()

    driver.implicitly_wait(5)
    driver.maximize_window()
    request.cls.driver = driver #request all class's driver =driver
    yield
    driver.close()
    driver.quit()
    print("Test Completed")