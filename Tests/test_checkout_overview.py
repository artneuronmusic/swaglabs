import pytest
import os.path
import sys
import time


sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from Info import var_info
from Pages.product_after_page import ProductAfterClickPage
from Pages.login_page import LoginPage
from Pages.product_page import ProductPage
from Pages.cart_page import CartPage
from Pages.client_info import ClientInfoPage
from Pages.outside_element import OutSideElement
from Pages.checkout_overview import CheckoutOverview

@pytest.mark.usefixtures("test_setup")
class TestOverview():

    @pytest.mark.skip
    def test_info_displayed(self):
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
        continue_button = cartpage.cart_checkout_button()
        continue_button.click()

        client_info = ClientInfoPage(driver)
        client_info.input_first_name("Erica")
        client_info.input_last_name("Liam")
        client_info.input_zipcode("78666")
        client_info.continue_button().click()

        outside = OutSideElement(driver)
        cart_qty = outside.cart_qty()

        overview = CheckoutOverview(driver)
        qty_item = overview.total_item()
        payment_info = overview.check_payment_all_info()
        delivery_info = overview.check_delivery_all_info()
        item_total, tax, total = overview.total_amount()
        finish_button = overview.overview_finish()
        cancel_button = overview.overview_cancel()


        print(item_total, tax, total)
        assert qty_item == 2
        assert cart_qty.text == "2"
        assert payment_info.is_displayed()
        assert delivery_info.is_displayed()
        assert item_total == "Item total: $59.980000000000004"
        assert tax == "Tax: $4.80"
        assert total == "Total: $64.78"
        assert finish_button.is_displayed()
        assert cancel_button.is_displayed()

    @pytest.mark.skip
    def test_nothing_purchased_info_displayed(self):

        driver = self.driver
        driver.get(var_info.url_login)
        driver.refresh()
        loginpage = LoginPage(driver)
        loginpage.enter_login_info(var_info.username_s, var_info.password_s)

        inventory = ProductPage(driver)
        inventory.cart_sign().click()

        cartpage = CartPage(driver)
        continue_button = cartpage.cart_checkout_button()
        continue_button.click()

        client_info = ClientInfoPage(driver)
        client_info.input_first_name("Erica")
        client_info.input_last_name("Liam")
        client_info.input_zipcode("78666")
        client_info.continue_button().click()

        outside = OutSideElement(driver)
        cart_qty = outside.cart_qty()

        overview = CheckoutOverview(driver)
        qty_item = overview.total_item()
        payment_info = overview.check_payment_all_info()
        delivery_info = overview.check_delivery_all_info()
        item_total, tax, total = overview.total_amount()
        finish_button = overview.overview_finish()
        cancel_button = overview.overview_cancel()


        print(item_total, tax, total)
        assert qty_item == 0
        assert cart_qty == None
        assert payment_info.is_displayed() == False
        assert delivery_info.is_displayed() == False
        assert item_total == "Item total: $0"
        assert tax == "Tax: $0.00"
        assert total == "Total: $0.00"
        assert finish_button.is_displayed()
        assert cancel_button.is_displayed()

    @pytest.mark.skip
    def test_successful_order(self):
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
        continue_button = cartpage.cart_checkout_button()
        continue_button.click()

        client_info = ClientInfoPage(driver)
        client_info.input_first_name("Erica")
        client_info.input_last_name("Liam")
        client_info.input_zipcode("78666")
        client_info.continue_button().click()

        outside = OutSideElement(driver)
        cart_qty = outside.cart_qty()
        assert cart_qty.text == "2"

        overview = CheckoutOverview(driver)
        finish_button = overview.overview_finish()
        finish_button.click()
        successful_order = overview.successfully_placed_order()
        successful_img = overview.successfully_img()
        final_cart_qty = outside.cart_qty()


        print(successful_order.text)


        assert successful_order.is_displayed()
        assert successful_order.text == "THANK YOU FOR YOUR ORDER"
        assert successful_img == True
        assert final_cart_qty == None
        assert driver.current_url == "https://www.saucedemo.com/checkout-complete.html"



    def test_cancel_order(self):
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
        continue_button = cartpage.cart_checkout_button()
        continue_button.click()

        client_info = ClientInfoPage(driver)
        client_info.input_first_name("Erica")
        client_info.input_last_name("Liam")
        client_info.input_zipcode("78666")
        client_info.continue_button().click()

        outside = OutSideElement(driver)
        cart_qty = outside.cart_qty()
        assert cart_qty.text == "2"

        overview = CheckoutOverview(driver)
        cancel_button = overview.overview_cancel()
        cancel_button.click()
        final_cart_qty = outside.cart_qty()



        assert final_cart_qty.text == "2"
        assert driver.current_url == "https://www.saucedemo.com/inventory.html"









