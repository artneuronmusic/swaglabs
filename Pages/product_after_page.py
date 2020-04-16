from selenium.webdriver.common.by import By
from Pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException, TimeoutException, StaleElementReferenceException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.select import Select as WebDriverSelect




class ProductAfterClickPage(BasePage):
    _back_button = {"by": By.XPATH, "value": "//button[@class='inventory_details_back_button']"}

    _detail_img = {"by": By.CLASS_NAME, "value": "inventory_details_img"}
    _detail_title = {"by": By.CLASS_NAME, "value": "inventory_details_name"}
    _detail_description = {"by": By.CLASS_NAME, "value": "inventory_details_desc"}
    _detail_price = {"by": By.CLASS_NAME, "value": "inventory_details_price"}
    _detail_add_to_cart = {"by": By.CLASS_NAME, "value": "btn_inventory"}
    _detail_amount = {"by": By.CLASS_NAME, "value": "shopping_cart_badge"}
    _cart_sign = {"by": By.XPATH, "value": "//*[name()='path' and contains(@fill,'currentCol')]"}
    _cart_qty = {"by": By.XPATH, "value": "//span[@class='fa-layers-counter shopping_cart_badge']"}


    def check_back_button(self):
        self._is_displayed(self._back_button)

        return self._find(self._back_button)


    def check_detail_img(self):
        return self._is_displayed(self._detail_img)


    def check_detail_title(self):
        try:
            self._is_displayed(self._detail_title)
            return

        except ValueError:
            # except ValueError as ve:
            raise ("This item is not displayed")
            # print(ve)


    def check_detail_description(self):
        self._is_displayed(self._detail_description)

        return self._find(self._detail_description)


    def check_detail_price(self):
        self._is_displayed(self._detail_price)

        return self._find(self._detail_price)


    def check_add_to_cart(self):

        self._is_displayed(self._detail_add_to_cart)
        return self._find(self._detail_add_to_cart)

    # the cart sign
    def check_cart_sign(self):
        sign = self._find(self._cart_sign)

        return sign

    # the cart_amount
    def check_cart_qty(self):
        if self._is_displayed(self._cart_qty):

            return self._find(self._cart_qty).text

        else:
            return None



