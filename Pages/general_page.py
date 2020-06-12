from selenium.webdriver.common.by import By
from Pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException, TimeoutException, StaleElementReferenceException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.\
    select import Select as WebDriverSelect
from Info.error_control import Error
import time


class GeneralPage(BasePage):
    _drop_down = {"by": By.XPATH, "value": "//button[contains(text(), 'Open Menu')]"}
    _all_items = {"by": By.CLASS_NAME, "value": "bm-item"}
    _all_products = {"by": By.CLASS_NAME, "value": "inventory_item"}
    _reset_app_state = {"by": By.XPATH, "value": "//a[@id='reset_sidebar_link']"}
    _delete_button = {"by": By.XPATH, "value": "//button[contains(text(),'Close Menu')]"}
    _cart_sign = {"by": By.XPATH, "value": "//*[name()='path' and contains( @ fill, 'currentCol')]"}
    _cart_qty = {"by": By.XPATH, "value": "//span[@class='fa-layers-counter shopping_cart_badge']"}


    def cart_sign(self):
        try:
            self._is_displayed(self._cart_sign)
            return self._find(self._cart_sign)

        except Error:
            raise



    # check does the qty exist, if yes, then locate it
    def cart_qty(self):
        if self._is_displayed(self._cart_qty):

            return self._find(self._cart_qty)

        else:
            return None


    def drop_down_menu(self):
        self._click(self._drop_down)


    def selection_menu(self):
        #without using sleep to pause script, but wait unitl the last option show
        self._wait_for_display(self._reset_app_state, 5)

        items = self.driver.find_elements(self._all_items["by"], self._all_items["value"])

        item_list = []

        for i in items:
            if i.is_displayed():
                item_list.append(i.text)

            else:
                print("{} is not displayed".format(i.text))

        return item_list

    def delete_menu(self):
        if self._is_displayed(self._delete_button):

            return self._find(self._delete_button)

        else:
            raise StaleElementReferenceException


    def display_delete_button(self):
        if self._is_displayed(self._all_items):
            self._click(self._delete_button)
            section = self._wait_for_not_display(self._all_items, 5)
            # the section will not be displayed=>True
            return section

        else:
            return None


    #menu items: delete button
    def delete_button_menu(self):
        #self._click(self._drop_down)
        self._wait_for_click(self._all_items, 5)
        self._click(self._delete_button)
        section = self._wait_for_not_display(self._all_items, 5)
        #the section will not be displayed=>True
        return section

    #menu items: pick one out of menu bar
    def pick_item_from_menu(self, name):
        self._wait_for_click(self._all_items, 5)
        items = self.driver.find_elements(self._all_items["by"], self._all_items["value"])
        #self._wait_for_click(self._all_items, 5)

        for i in items:
            try:
                if i.text != name:
                    continue
                else:
                    i.click()
            except StaleElementReferenceException:
                print("StaleElementReferenceException")






