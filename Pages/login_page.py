from selenium.webdriver.common.by import By
from Pages.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains
import time


class LoginPage(BasePage):
    _username_input = {"by": By.ID, "value": "user-name"}
    _password_input = {"by": By.ID, "value": "password"}
    _login_button = {"by": By.XPATH, "value": "//input[@class='btn_action']"}
    _after_login = {"by": By.XPATH, "value": "//div[@class='product_label']"}
    _delete_button = {"by": By.XPATH, "value":"//button[@class='error-button']"}
    _fail_log_in_message = {"by": By.TAG_NAME, "value": "h3"}

    _drop_down = {"by": By.XPATH, "value": "//button[contains(text(), 'Open Menu')]"}
    _all_items = {"by": By.XPATH, "value": "//nav[@class='bm-item-list']//a[@class='bm-item menu-item']"}


    def __init__(self, driver):
        #super().__init__(driver)
        self.driver = driver

        #super(LoginPage, self).__init__(driver)

        #self.driver=driver

        self._get_url("https://www.saucedemo.com/")
        assert self.driver.current_url == "https://www.saucedemo.com/"

    #get locator for inputting username, password, then login
    def login_info(self, username, password):
        self._send_keys(self._username_input, username)
        self._send_keys(self._password_input, password)
        self._click(self._login_button)

    #the page people will see, after successfully login
    def page_after_login(self):

        #return self._wait_for_display(self._after_login, 3)
        return self._is_displayed(self._after_login)

    #response after log in fail
    def fail_message(self):
        self._wait_for_display(self._fail_log_in_message, 3)
        #self.driver.implicitly_wait(3)
        return self._find(self._fail_log_in_message)
        #return self._is_displayed(self._fail_log_in_message)

    #delete action fo
    def delete_button(self):
        self._click(self._delete_button)



















   #def fail_login_message(self):
    #    return self._is_displayed(self._fail_message)
