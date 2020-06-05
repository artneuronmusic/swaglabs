import pytest
import os.path
import sys
import time


sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from Info import var_info

from Pages.login_page import LoginPage
from Pages.product_page import ProductPage
from Pages.cart_page import CartPage
from Pages.client_info import ClientInfoPage
from Pages.outside_element import OutSideElement
from Pages.checkout_overview import CheckoutOverview

@pytest.mark.usefixtures("driver")
class TestWebsite():

    #@pytest.mark.skip
    def test_standard_account_password(self):

        driver = self.driver
        driver.get(var_info.url_login)
        login = LoginPage(driver)
        login.enter_login_info(var_info.username_s, var_info.password_s)
        product = ProductPage(driver)

        # Add no 3 and Sauce Labs Backpack into cart
        product.click_add_to_cart(3)
        product.product_add_to_cart("Sauce Labs Backpack")
        cart_img = product.cart_sign()
        cart_img.click()

        #check cart details
        cart_page = CartPage(driver)
        checkout_button = cart_page.cart_checkout_button()
        checkout_button.click()

        client_info = ClientInfoPage(driver)
        client_info.input_first_name("Lily")
        client_info.input_last_name("Wang")
        client_info.input_zipcode("88599")
        continue_button = client_info.continue_button()
        continue_button.click()

        overview = CheckoutOverview(driver)
        finish = overview.overview_finish()
        finish.click()

        successful_words = overview.successfully_placed_order()
        successful_img = overview.successfully_placed_order()

        final_sign = product.cart_sign()
        final_qty = product.cart_qty()

        assert final_sign.is_displayed()
        assert final_qty == None
        assert successful_words.is_displayed()
        assert successful_img.is_displayed()


    #this one should even not be able to get to the next page
    def test_locked_account(self):

        driver = self.driver
        driver.get(var_info.url_login)
        login = LoginPage(driver)
        login.enter_login_info(var_info.username_l, var_info.password_s)

        product = ProductPage(driver)

        # Add no 3 and Sauce Labs Backpack into cart
        time.sleep(5)
        product.click_add_to_cart(3)
        product.product_add_to_cart("Sauce Labs Backpack")
        cart_img = product.cart_sign()
        cart_img.click()

        #check cart details
        cart_page = CartPage(driver)
        checkout_button = cart_page.cart_checkout_button()
        checkout_button.click()

        client_info = ClientInfoPage(driver)
        client_info.input_first_name("Lily")
        client_info.input_last_name("Wang")
        client_info.input_zipcode("88599")
        continue_button = client_info.continue_button()
        continue_button.click()

        overview = CheckoutOverview(driver)
        finish = overview.overview_finish()
        finish.click()

        successful_words = overview.successfully_placed_order()
        successful_img = overview.successfully_placed_order()

        final_sign = product.cart_sign()
        final_qty = product.cart_qty()

        assert final_sign.is_displayed()
        assert final_qty == None
        assert successful_words.is_displayed()
        assert successful_img.is_displayed()

    #@pytest.mark.skip
    def test_problem_account(self):

        driver = self.driver
        driver.get(var_info.url_login)
        login = LoginPage(driver)
        login.enter_login_info(var_info.username_p, var_info.password_s)
        product = ProductPage(driver)

        # Add no 3 and Sauce Labs Backpack into cart
        product.click_add_to_cart(3)
        product.product_add_to_cart("Sauce Labs Backpack")
        cart_img = product.cart_sign()
        cart_img.click()

        #check cart details
        cart_page = CartPage(driver)
        checkout_button = cart_page.cart_checkout_button()
        checkout_button.click()

        client_info = ClientInfoPage(driver)
        client_info.input_first_name("Lily")
        client_info.input_last_name("Wang")
        client_info.input_zipcode("88599")
        continue_button = client_info.continue_button()
        continue_button.click()

        overview = CheckoutOverview(driver)
        finish = overview.overview_finish()
        finish.click()

        successful_words = overview.successfully_placed_order()
        successful_img = overview.successfully_placed_order()

        final_sign = product.cart_sign()
        final_qty = product.cart_qty()

        assert final_sign.is_displayed()
        assert final_qty == None
        assert successful_words.is_displayed()
        assert successful_img.is_displayed()

    #@pytest.mark.skip
    def test_performance_glitch_account(self):

        driver = self.driver
        driver.get(var_info.url_login)
        login = LoginPage(driver)
        login.enter_login_info(var_info.username_pe, var_info.password_s)
        product = ProductPage(driver)

        # Add no 3 and Sauce Labs Backpack into cart
        product.click_add_to_cart(3)
        product.product_add_to_cart("Sauce Labs Backpack")
        cart_img = product.cart_sign()
        cart_img.click()

        #check cart details
        cart_page = CartPage(driver)
        checkout_button = cart_page.cart_checkout_button()
        checkout_button.click()

        client_info = ClientInfoPage(driver)
        client_info.input_first_name("Lily")
        client_info.input_last_name("Wang")
        client_info.input_zipcode("88599")
        continue_button = client_info.continue_button()
        continue_button.click()

        overview = CheckoutOverview(driver)
        finish = overview.overview_finish()
        finish.click()

        successful_words = overview.successfully_placed_order()
        successful_img = overview.successfully_placed_order()

        final_sign = product.cart_sign()
        final_qty = product.cart_qty()

        assert final_sign.is_displayed()
        assert final_qty == None
        assert successful_words.is_displayed()
        assert successful_img.is_displayed()

