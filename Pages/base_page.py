from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from Functionality_Tests import config
from selenium.webdriver.support.ui import Select



class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def _get_url(self, url):


        if url.startswith == "https":
            self.driver.get(url)

        else:
            self.driver.get(config.baseurl + url)


    def _find(self, locator):
        return self.driver.find_element(locator["by"], locator["value"])


    def _find_elements(self, locator):
        return self.driver.find_elements(locator["by"], locator["value"])
    #def _find_plural(self, locator):
     #   return self.driver.find_elements(locator["by"], locator["value"])


    def _clear(self, locator):
        self.driver.find_element(locator["by"], locator["value"]).clear()



    def _click(self, locator):
        self._find(locator).click()

    def _is_displayed(self, locator):
        try:
            self._find(locator).is_displayed()
            return True

        except NoSuchElementException:
            return False




    def _send_keys(self, locator, input_info):
        self._find(locator).send_keys(input_info)

    def _select(self, locator):
        return Select(self._find(locator))

    def _wait_for_display(self, locator, timeout):
        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(
                expected_conditions.visibility_of_element_located((locator['by'], locator['value'])))

        except TimeoutException:
            return False

        return True


    def _wait_for_not_display(self, locator, timeout):
        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(expected_conditions.invisibility_of_element_located((locator['by'], locator['value'])))

        except TimeoutException:
            return False

        return True


    def _wait_for_click(self, locator, timeout):
        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(
                expected_conditions.element_to_be_clickable((locator['by'], locator['value'])))

        except TimeoutException:
            return False

        return True


