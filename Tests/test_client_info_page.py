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




@pytest.mark.usefixtures("test_setup")
class TestClientInfo():

    @pytest.mark.skip
    def test_valid_client_info(self):
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

        assert driver.current_url == "https://www.saucedemo.com/checkout-step-two.html"


    @pytest.mark.skip
    def test_blank_first_name(self):
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
        client_info.input_first_name("")
        client_info.input_last_name("Liam")
        client_info.input_zipcode("78666")
        client_info.continue_button().click()
        sign = client_info.warning_sign()

        print(sign.text)
        assert driver.current_url == "https://www.saucedemo.com/checkout-step-one.html"
        assert sign.text == "Error: First Name is required"


    @pytest.mark.skip
    def test_blank_last_name(self):
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
        client_info.input_first_name("Cool")
        client_info.input_last_name("")
        client_info.input_zipcode("78666")
        client_info.continue_button().click()
        sign = client_info.warning_sign()

        print(sign.text)
        assert driver.current_url == "https://www.saucedemo.com/checkout-step-one.html"
        assert sign.text == "Error: Last Name is required"

    @pytest.mark.skip
    def test_blank_zipcode(self):
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
        client_info.input_first_name("Cool")
        client_info.input_last_name("Liam")
        client_info.input_zipcode("")
        client_info.continue_button().click()
        sign = client_info.warning_sign()

        print(sign.text)
        assert driver.current_url == "https://www.saucedemo.com/checkout-step-one.html"
        assert sign.text == "Error: Postal Code is required"


    def test_all_blank_info(self):
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
        client_info.input_first_name("")
        client_info.input_last_name("")
        client_info.input_zipcode("")
        client_info.continue_button().click()
        sign = client_info.warning_sign()

        print(sign.text)
        assert driver.current_url == "https://www.saucedemo.com/checkout-step-one.html"
        assert sign.text == "Error: First Name is required"



    def test_invalid_info_with_cancel(self):
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
        client_info.input_first_name("")
        client_info.input_last_name("")
        client_info.input_zipcode("")
        client_info.cancel_button().click()

        outside = OutSideElement(driver)
        checkout_button = cartpage.cart_checkout_button()
        checkout_button.click()
        cart_qty = outside.cart_qty()


        assert driver.current_url == "https://www.saucedemo.com/cart.html"
        assert cart_qty.text == "2"







