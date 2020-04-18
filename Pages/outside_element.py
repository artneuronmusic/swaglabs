from selenium.webdriver.common.by import By
from Pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException, TimeoutException, StaleElementReferenceException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.select import Select as WebDriverSelect
import time


class OutSideElement(BasePage):

    _section_title = {"by": By.XPATH, "value": "//div[@class='subheader']"}

    _drop_down = {"by": By.XPATH, "value": "//button[contains(text(), 'Open Menu')]"}
    _item_section = {"by": By.XPATH, "value": "//nav[@class='bm-item-list']"}
    _all_items = {"by": By.XPATH, "value": "//nav[@class='bm-item-list']//a[@class='bm-item menu-item']"}
    _all_products = {"by": By.CLASS_NAME, "value": "inventory_item"}
    _delete_button = {"by": By.XPATH, "value": "//button[contains(text(),'Close Menu')]"}

    _cart_sign = {"by": By.XPATH, "value": "//*[name()='path' and contains(@fill,'currentCol')]"}
    _cart_qty = {"by": By.XPATH, "value": "//span[@class='fa-layers-counter shopping_cart_badge']"}


    def section_title(self):
        self._is_displayed(self._section_title)

        return self._find(self._section_title)


    # the cart sign
    def cart_sign(self):
        sign = self._find(self._cart_sign)

        return sign


    # the cart_amount
    def cart_qty(self):
        if self._is_displayed(self._cart_qty):

            return self._find(self._cart_qty)

        else:
            return None

    # element list in menu bar
    def menu_items(self):
        self._click(self._drop_down)
        self._wait_for_click(self._all_items, 5)
        items = self.driver.find_elements(self._all_items["by"], self._all_items["value"])

        i_list = []
        for i in items:
            i_list.append(i.text)

        return i_list
        # return items.text #delete

    # menu items: delete button
    def delete_button_menu(self):
        self._click(self._drop_down)
        self._is_displayed(self._item_section)
        self._click(self._delete_button)
        section = self._wait_for_not_display(self._item_section, 5)

        return section == True

    # menu items: pick one out of menu bar
    def pick_item_from_menu(self, name):
        self._click(self._drop_down)
        items = self.driver.find_elements(self._all_items["by"], self._all_items["value"])
        self._wait_for_click(self._all_items, 5)

        for i in items:

            try:
                if i.text != name:
                    continue

                else:
                    i.click()
            except StaleElementReferenceException:
                print("StaleElementReferenceException")









