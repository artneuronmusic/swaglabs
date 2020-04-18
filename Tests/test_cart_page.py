import pytest
import os.path
import sys
import time


sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from Info import var_info
from Pages.login_page import LoginPage
from Pages.product_page import ProductPage
from Pages.cart_page import CartPage
from Pages.outside_element import OutSideElement

@pytest.mark.usefixtures("test_setup")
class TestCartPage():

    @pytest.mark.skip
    # accepted:username=standard_user, pw=secret_sauce
    def test_displayed_elements_in_page(self):
        driver = self.driver
        driver.get(var_info.url_login)
        loginpage = LoginPage(driver)
        loginpage.enter_login_info(var_info.username_s, var_info.password_s)

        inventory = ProductPage(driver)
        inventory.cart_sign().click()

        cartpage = CartPage(driver)
        title = cartpage.cart_title()
        qty_label = cartpage.cart_qty_label()
        cart_desc = cartpage.cart_desc()
        shopping_button = cartpage.cart_continue_shopping()
        checkout_button = cartpage.cart_checkout_button()

        outside = OutSideElement(driver)
        cart_sign = outside.cart_sign()
        cart_qty = outside.cart_qty()


        assert title.text == "Your Cart"
        assert qty_label.text == "QTY"
        assert cart_desc.text == "DESCRIPTION"
        assert cart_sign.is_displayed()
        assert cart_qty == None
        assert shopping_button.is_displayed()
        assert checkout_button.is_displayed()

    @pytest.mark.skip
    def test_selected_products_in_checkout(self):
        driver = self.driver
        driver.get(var_info.url_login)
        driver.refresh()
        loginpage = LoginPage(driver)
        loginpage.enter_login_info(var_info.username_s, var_info.password_s)

        inventory = ProductPage(driver)
        inventory.click_add_to_cart(2)
        inventory.label_add_to_cart("Sauce Labs Fleece Jacket")
        inventory.cart_sign().click()


        cartpage = CartPage(driver)
        sum_items = cartpage.to_buy_total()
        outside = OutSideElement(driver)
        cart_qty = outside.cart_qty()
        product_list = cartpage.cart_product_name()
        qty_display = cartpage.cart_input_qty()
        #price_display = cartpage.cart_product_price()


        print(product_list)

        assert sum_items == 2
        assert cart_qty.text =="2"
        assert qty_display.text == "1"

    @pytest.mark.skip
    def test_remove_products_in_checkout(self):
        driver = self.driver
        driver.get(var_info.url_login)
        driver.refresh()
        loginpage = LoginPage(driver)
        loginpage.enter_login_info(var_info.username_s, var_info.password_s)

        inventory = ProductPage(driver)
        inventory.click_add_to_cart(2)
        inventory.label_add_to_cart("Sauce Labs Fleece Jacket")
        inventory.cart_sign().click()


        cartpage = CartPage(driver)

        qty_display = cartpage.cart_input_qty()
        remove = cartpage.cart_product_remove(2)

        outside = OutSideElement(driver)
        cart_qty = outside.cart_qty()
        sum_items = cartpage.to_buy_total()

        assert sum_items == 1
        assert cart_qty.text =="1"
        assert qty_display.text == "1"

    @pytest.mark.skip
    def test_continue_shopping_button(self):

        driver = self.driver
        driver.get(var_info.url_login)
        driver.refresh()
        loginpage = LoginPage(driver)
        loginpage.enter_login_info(var_info.username_s, var_info.password_s)

        inventory = ProductPage(driver)
        inventory.click_add_to_cart(2)
        inventory.label_add_to_cart("Sauce Labs Fleece Jacket")
        inventory.cart_sign().click()

        cartpage = CartPage(driver)

        qty_display = cartpage.cart_input_qty()
        remove = cartpage.cart_product_remove(2)

        outside = OutSideElement(driver)

        sum_items = cartpage.to_buy_total()

        continue_button = cartpage.cart_continue_shopping()
        continue_button.click()
        cart_qty = outside.cart_qty()

        assert cart_qty.text == "1"
        assert driver.current_url == "https://www.saucedemo.com/inventory.html"

    def test_checkout_button(self):
        driver = self.driver
        driver.get(var_info.url_login)
        driver.refresh()
        loginpage = LoginPage(driver)
        loginpage.enter_login_info(var_info.username_s, var_info.password_s)

        inventory = ProductPage(driver)
        inventory.click_add_to_cart(2)
        inventory.label_add_to_cart("Sauce Labs Fleece Jacket")
        inventory.cart_sign().click()

        cartpage = CartPage(driver)

        qty_display = cartpage.cart_input_qty()
        outside = OutSideElement(driver)
        checkout_button = cartpage.cart_checkout_button()
        checkout_button.click()
        cart_qty = outside.cart_qty()

        assert cart_qty.text == "2"
        assert driver.current_url == "https://www.saucedemo.com/checkout-step-one.html"


"""
    def test_selected_products(self):
        driver = self.driver
        driver.get(var_info.url_login)
        driver.refresh()
        loginpage = LoginPage(driver)
        loginpage.enter_login_info(var_info.username_s, var_info.password_s)

        inventory = ProductPage(driver)
        time.sleep(5)
        
"""













