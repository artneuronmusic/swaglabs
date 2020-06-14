from selenium.webdriver.common.by import By
from Pages.base_page import BasePage
from Pages.product_page import ProductPage
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException, TimeoutException, StaleElementReferenceException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.select import Select as WebDriverSelect
from Info.error_control import Error
import time
import pytest


class DetailsPage(BasePage):

    _back_button = {"by": By.XPATH, "value": "//button[@class='inventory_details_back_button']"}
    _single_product_img = {"by": By.CLASS_NAME, "value": "inventory_details_img"}
    _single_title = {"by": By.CLASS_NAME, "value": "inventory_details_name"}
    _single_description = {"by": By.CLASS_NAME, "value": "inventory_details_desc"}
    _single_price = {"by": By.CLASS_NAME, "value": "inventory_details_price"}
    _single_product_img = {"by": By.CLASS_NAME, "value": "inventory_details_img"}
    _single_add_to_cart = {"by": By.CLASS_NAME, "value": "btn_inventory"}
    _cart_sign = {"by": By.XPATH, "value": "//*[name() = 'path' and contains( @ fill, 'currentCol')]"}
    _cart_qty = {"by": By.XPATH, "value": "//span[@class='fa-layers-counter shopping_cart_badge']"}


    def check_single_description(self):
        # try:
        #     self._wait_for_display(self._product_description)
        #
        # except StaleElementReferenceException:
        #     print("StaleElementReferenceException")

        return self._find(self._single_description)


    def check_single_price(self):


        return self._find(self._single_price)


    def check_single_label(self):
        return self._find(self._single_title)


    def check_single_add_to_cart(self):
        return self._find(self._single_add_to_cart)


    def check_single_img(self):
        img = self._find(self._single_product_img)
        img_att = img.get_attribute('src')
        if img_att.endswith(".jpg"):
            return img

        else:
            return None



    def back_button(self):
        return self._find(self._back_button)







