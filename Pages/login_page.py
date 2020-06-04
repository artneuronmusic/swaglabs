from selenium.webdriver.common.by import By
from Pages.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains
import time



class LoginPage(BasePage):

    _website_logo = {"by": By. XPATH, "value": "//div[@class='login_logo']"}
    _username_input = {"by": By.ID, "value": "user-name"}
    _password_input = {"by": By.ID, "value": "password"}
    _login_button = {"by": By.XPATH, "value": "//input[@class='btn_action']"}
    _after_login = {"by": By.XPATH, "value": "//div[@class='product_label']"}
    _delete_button = {"by": By.XPATH, "value":"//button[@class='error-button']"}
    _fail_log_in_message = {"by": By.TAG_NAME, "value": "h3"}

    _drop_down = {"by": By.XPATH, "value": "//button[contains(text(), 'Open Menu')]"}
    _all_items = {"by": By.XPATH, "value": "//nav[@class='bm-item-list']//a[@class='bm-item menu-item']"}

    #
    # def __init__(self, driver):
    #
    #     self.driver = driver
    # self._get_url("https://www.saucedemo.com/")
    # assert self._is_displayed(self._website_logo)


    def login_logo(self):
        self._wait_for_display(self._website_logo, 5)

    #get login info
    def enter_login_info(self, username, password):
        self._send_keys(self._username_input, username)
        self._send_keys(self._password_input, password)
        self._click(self._login_button)

    #evidence after logging in
    def title_after_login(self):

        #return self._wait_for_display(self._after_login, 3)
        return self._is_displayed(self._after_login)

    #response after log in fail
    def failed_message(self):
        self._wait_for_display(self._fail_log_in_message, 3)
        #self.driver.implicitly_wait(3)
        return self._find(self._fail_log_in_message)
        #return self._is_displayed(self._fail_log_in_message)

    #delete action fo
    def delete_button(self):
        self._click(self._delete_button)



















   #def fail_login_message(self):
    #    return self._is_displayed(self._fail_message)
