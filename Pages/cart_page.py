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
    _cart_title = {"by": By.XPATH, "value": "//div[@class='subheader']"}
    _cart_qty_label = {"by": By.XPATH, "value": "//div[@class='cart_quantity_label']"}
    _cart_desc = {"by": By.XPATH, "value": "//div[@class='cart_desc_label']"}
    _cart_input_qty = {"by": By.XPATH, "value": "//div[@class='cart_quantity']"}
    _cart_product_name = {"by": By.CLASS_NAME, "value": "inventory_item_name"}
    _cart_product_description = {"by": By.CLASS_NAME, "value": "inventory_item_desc"}
    _cart_product_price = {"by": By.CLASS_NAME, "value": "inventory_item_price"}
    _cart_product_add_to_cart = {"by": By.XPATH, "value": "//button[@class='btn_secondary cart_button']"}
    # _cart_page_amount = {"by": By.CLASS_NAME, "value": "shopping_cart_badge"}
    _items_total = {"by": By.CLASS_NAME, "value": "cart_item"}

    _continue_shopping = {"by": By.XPATH, "value": "//a[@class='btn_secondary']"}
    _checkout_button = {"by": By.CLASS_NAME, "value": "checkout_button"}

    #_cart_sign = {"by": By.XPATH, "value": "//*[name()='path' and contains(@fill,'currentCol')]"}
    #_cart_qty = {"by": By.XPATH, "value": "//span[@class='fa-layers-counter shopping_cart_badge']"}


    def cart_title(self):
        self._is_displayed(self._cart_title)

        return self._find(self._cart_title)


    def cart_qty_label(self):
        self._is_displayed(self._cart_qty_label)

        return self._find(self._cart_qty_label)


    def cart_desc(self):
        self._is_displayed(self._cart_desc)

        return self._find(self._cart_desc)


    def cart_input_qty(self):
        self._is_displayed(self._cart_input_qty)

        return self._find(self._cart_input_qty)


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


    #def cart_product_price(self, input_info):
     #   product_names = self._find_elements(self._cart_product_name)
      #  product_prices = self._find_elements(self._cart_product_price())
       # if isinstance(input, int):

        #for i in
        #self._is_displayed(self._cart_product_price)

        #return self._find(self._cart_product_price)


    def cart_product_remove(self, index):
        item_remove = self._find_elements(self._cart_product_add_to_cart)
        new_index = int(index) - 1

        for i in range(len(item_remove)):
            if i == new_index:
                item_remove[i].click()


            else:
                pass

    def cart_continue_shopping(self):
        self._is_displayed(self._continue_shopping)

        return self._find(self._continue_shopping)


    def cart_checkout_button(self):
        self._is_displayed(self._checkout_button)

        return self._find(self._checkout_button)

    def to_buy_total(self):
        all_items = self._find_elements(self._items_total)
        return len(all_items)



"""
    #the cart sign
    def cart_sign(self):
        sign = self._find(self._cart_sign)

        return sign


    #the cart_amount
    def cart_qty(self):
        if self._is_displayed(self._cart_qty):

            return self._find(self._cart_qty)

        else:
            return None

"""


