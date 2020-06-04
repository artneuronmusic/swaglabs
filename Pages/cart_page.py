from selenium.webdriver.common.by import By
from Pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException, TimeoutException, StaleElementReferenceException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.select import Select as WebDriverSelect
import time

class CartPage(BasePage):



    #cart.html
    _cart_sign = {"by": By.XPATH, "value": "//*[name()='path' and contains( @ fill, 'currentCol')]"}
    _cart_qty = {"by": By.XPATH, "value": "//span[@class='fa-layers-counter shopping_cart_badge']"}
    _cart_title = {"by": By.XPATH, "value": "//div[@class='subheader']"}
    _cart_qty_label = {"by": By.XPATH, "value": "//div[@class='cart_quantity_label']"}
    _cart_desc_label = {"by": By.XPATH, "value": "//div[@class='cart_desc_label']"}
    _cart_input_qty = {"by": By.XPATH, "value": "//div[@class='cart_quantity']"}
    _cart_product_name = {"by": By.CLASS_NAME, "value": "inventory_item_name"}
    _cart_product_description = {"by": By.CLASS_NAME, "value": "inventory_item_desc"}
    _cart_product_price = {"by": By.CLASS_NAME, "value": "inventory_item_price"}
    _cart_product_remove = {"by": By.XPATH, "value": "//button[@class='btn_secondary cart_button']"}
    # _cart_page_amount = {"by": By.CLASS_NAME, "value": "shopping_cart_badge"}
    _items_total = {"by": By.CLASS_NAME, "value": "cart_item"}

    _continue_shopping = {"by": By.XPATH, "value": "//a[@class='btn_secondary']"}
    _checkout_button = {"by": By.CLASS_NAME, "value": "checkout_button"}

    #_cart_sign = {"by": By.XPATH, "value": "//*[name()='path' and contains(@fill,'currentCol')]"}
    #_cart_qty = {"by": By.XPATH, "value": "//span[@class='fa-layers-counter shopping_cart_badge']"}



    def cart_title(self):
        try:
            self._is_displayed(self._cart_title)
            return self._find(self._cart_title)


        except AssertionError:
            return False


    def cart_qty_label(self):
        try:
            self._is_displayed(self._cart_qty_label)

            return self._find(self._cart_qty_label)

        except AssertionError:
            return False


    def cart_desc_label(self):


        try:
            self._is_displayed(self._cart_desc_label)

            return self._find(self._cart_desc_label)

        except AssertionError:
            return False


    def cart_input_qty(self):
        try:
            self._is_displayed(self._cart_input_qty)

            return self._find(self._cart_input_qty)

        except AssertionError:
            return False


    def cart_product_name(self):
        product_names = self._find_elements(self._cart_product_name)
        result = ""
        name_list = []
        for i in range(len(product_names)):
            if product_names[i].is_displayed():
                name_list.append(product_names[i].text)
                result = name_list

            else:
                result = None

        return result



    def cart_product_description(self):
        self._is_displayed(self._cart_product_description)

        return self._find(self._cart_product_description)


    def cart_product_remove(self, index):
        item_remove = self._find_elements(self._cart_product_remove)
        new_index = int(index) - 1

        for i in range(len(item_remove)):
            if i == new_index:
                item_remove[i].click()


            else:
                pass

    def cart_continue_shopping(self):
        try:
            self._is_displayed(self._continue_shopping)

            return self._find(self._continue_shopping)

        except AssertionError:
            raise("The button does not exist")


    def cart_checkout_button(self):
        try:

            self._is_displayed(self._checkout_button)

            return self._find(self._checkout_button)

        except AssertionError:
            return None

    def total_product_in_cart(self):
        all_items = self._find_elements(self._items_total)
        if all_items:
            return len(all_items)

        else:
            return None

    def cart_sign(self):

        return self._find(self._cart_sign)

        # the cart_amount

    def cart_qty(self):
        if self._is_displayed(self._cart_qty):
            qty = self._find(self._cart_qty)
            return qty

        else:
            return None


