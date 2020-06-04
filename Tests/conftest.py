import pytest
from selenium import webdriver
import config


def pytest_addoption(parser):
    # parser.addoption("--baseurl",
    #                 action="store",
    #                 default="https://www.saucedemo.com/",
    #                 help="base URL for the application under test")
    parser.addoption("--browser",
                     action="store",
                     default="chrome",
                     help="the name is the browser u want to run with")


#@pytest.fixture(scope='function')
#@pytest.fixture(scope='session')
#@pytest.fixture(scope="class")
#@pytest.fixture(scope="session") #u use it when without class, and it will open browser once with all test


@pytest.fixture
def driver(request):
    #url = request.config.getoption("--baseurl")
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



"""
@pytest.fixture
def driver(request):
    config.baseurl = request.config.getoption("--baseurl")
    config.browser = request.config.getoption("--browser")
    if config.browser == "chrome":
        driver_ = webdriver.Chrome()
    elif config.browser == "firefox":
        driver_ = webdriver.FireFox()

    def quit():
        driver_.quit()

    request.addfinalizer(quit)
    return driver_


"""



