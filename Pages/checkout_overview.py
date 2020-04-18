from selenium.webdriver.common.by import By
from Pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException, TimeoutException, StaleElementReferenceException
from selenium.webdriver.support.wait import WebDriverWait



class CheckoutOverview(BasePage):


    _overview_quantity = {"by": By.CLASS_NAME, "value": "summary_quantity"}
    _overview_desc_title = {"by": By.CLASS_NAME, "value": "inventory_item_name"}
    _overview_desc_desc = {"by": By.CLASS_NAME, "value": "inventory_item_desc"}
    _overview_desc_price = {"by": By.CLASS_NAME, "value": "inventory_item_price"}

    _overview_payment_info = {"by": By.XPATH, "value": "//div[contains(text(),'Payment Information:')]"}
    _overview_payment_value = {"by": By.XPATH, "value": "//div[contains(text(),'SauceCard')]"}
    _overview_delivery_info = {"by": By.XPATH, "value": "//div[contains(text(),'Shipping Information:')]"}
    _overview_delivery_value = {"by": By.XPATH, "value": "//div[contains(text(),'FREE PONY EXPRESS DELIVERY!')]"}
    _overview_subtotal = {"by": By.CLASS_NAME, "value": "summary_subtotal_label"}
    _overview_tax = {"by": By.CLASS_NAME, "value": "summary_tax_label"}
    _overview_total = {"by": By.CLASS_NAME, "value": "summary_total_label"}
    _items_total = {"by": By.CLASS_NAME, "value": "cart_item"}

    # the same as the top
    #https://www.saucedemo.com/inventory.html
    _overview_cancel = {"by": By.XPATH, "value": "//a[@class='cart_cancel_link btn_secondary']"}
    _overview_finish = {"by": By.XPATH, "value": "//a[@class='btn_action cart_button']"}

    _thank_order = {"by": By.XPATH, "value": "//h2[@class='complete-header']"}
    _thank_img = {"by": By.XPATH, "value": "//div[@class='pony_express']"}
    # the cart should be nothing

    def check_payment_all_info(self):
        result = ""
        try:
            self._is_displayed(self._overview_payment_info)
            self._is_displayed(self._overview_payment_value)
            result = self._find(self._overview_payment_value)

        except NoSuchElementException:
            result = False

        return result


    def check_delivery_all_info(self):
        result = ""
        try:
            self._is_displayed(self._overview_delivery_info)
            self._is_displayed(self._overview_delivery_value)
            result = self._find(self._overview_delivery_value)

        except NoSuchElementException:
            result = False

        return result


    def total_amount(self):
        result = ""
        try:
            self._is_displayed(self._overview_subtotal)
            self._is_displayed(self._overview_tax)
            self._is_displayed(self._overview_total)

            item_total = self._find(self._overview_subtotal)
            tax = self._find(self._overview_tax)
            total = self._find(self._overview_total)

            result = [item_total.text, tax.text, total.text]

        except NoSuchElementException:
            result = False

        return result


    def overview_finish(self):
        result = ""
        try:
            self._is_displayed(self._overview_finish)
            result = self._find(self._overview_finish)

        except NoSuchElementException:
            result = False

        return result


    def overview_cancel(self):
        result = ""
        try:
            self._is_displayed(self._overview_cancel)
            result = self._find(self._overview_cancel)


        except NoSuchElementException:
            result = False

        return result


    def successfully_placed_order(self):
        result = ""
        try:
            self._is_displayed(self._thank_order)
            result = self._find(self._thank_order)


        except NoSuchElementException:
            result = False

        return result


    def successfully_img(self):
        result = ""
        try:

            img = self._is_displayed(self._thank_img)
            result = img

        except NoSuchElementException:
            result = False

        return result


    def total_item(self):
        all_items = self._find_elements(self._items_total)
        return len(all_items)


