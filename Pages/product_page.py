from selenium.webdriver.common.by import By
from Pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException, TimeoutException, StaleElementReferenceException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.select import Select as WebDriverSelect


class ProductPage(BasePage):
    #the same as _after_login
    _product_logo = {"by": By.XPATH, "value": "//div[@class='product_label']"}
    _drop_down = {"by": By.XPATH, "value": "//button[contains(text(), 'Open Menu')]"}
    _all_items = {"by": By.XPATH, "value": "//nav[@class='bm-item-list']//a[@class='bm-item menu-item']"}
    _all_products = {"by": By.CLASS_NAME, "value": "inventory_item"}
    _delete_button = {"by": By.XPATH, "value": "//button[contains(text(),'Close Menu')]"}

    def product_logo(self):
        return self._is_displayed(self._product_logo)

    def menu_items(self):

        self._click(self._drop_down)
        self._wait_for_click(self._all_items, 5)
        delete = self._find(self._delete_button)
        items = self.driver.find_elements(self._all_items["by"], self._all_items["value"])

        i_list = []
        for i in items:
            i_list.append(i.text)

        return i_list, delete
        # return items.text #delete

    def pick_item_from_menu(self, name):
        items = self.driver.find_elements(self._all_items["by"], self._all_items["value"])
        self._wait_for_click(self._all_items, 5)
        for i in items:



            try:
                if i.text == name:
                    i.click()

                else:
                    continue
            except StaleElementReferenceException:
                print("StaleElementReferenceException")
            return (self.driver.current_url)

    def delete_button_on_menu(self):
        return self._click(self._delete_button)