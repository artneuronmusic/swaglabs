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
from Pages.product_individual_page import DetailsPage

@pytest.mark.usefixtures("driver")
class TestWebsiteImg():

    @pytest.mark.skip
    def test_standard_account_password(self):
        driver = self.driver
        driver.get(var_info.url_login)
        login = LoginPage(driver)
        login.enter_login_info(var_info.username_s, var_info.password_s)
        product = ProductPage(driver)

        #add img1
        product.click_products_img(1)

        individual_page = DetailsPage(driver)
        add = individual_page.check_single_add_to_cart()
        add.click()
        return_button = individual_page.back_button()
        return_button.click()

        # add img2
        product.click_products_img(2)
        add2 = individual_page.check_single_add_to_cart()
        add2.click()

        sign = individual_page.cart_sign()
        sign.click()

        #remove img2
        cart_page = CartPage(driver)
        cart_page.cart_product_remove(2)

        continue_buy = cart_page.cart_continue_shopping()
        continue_buy.click()

        #add index 4
        product.click_add_to_cart(4)
        p_sign = product.cart_sign()
        p_sign.click()


        checkout = cart_page.cart_checkout_button()
        checkout.click()

        client_info = ClientInfoPage(driver)
        client_info.input_first_name("Lily")
        client_info.input_last_name("Wang")
        client_info.input_zipcode("88599")

        client_info.cancel_button()

        cart_page.cart_checkout_button().click()

        client_info.input_first_name("Lily")
        client_info.input_last_name("Wang")
        client_info.input_zipcode("88599")

        overview = CheckoutOverview(driver)
        o_cancel = overview.overview_cancel()
        o_cancel.click()

        individual_page.cart_sign()
        cart_page.cart_checkout_button().click()

        client_info.input_first_name("Lily")
        client_info.input_last_name("Wang")
        client_info.input_zipcode("88599")

        client_continue = client_info.continue_button()
        client_continue.click()
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

    def test_problem_account_password_img(self):
        driver = self.driver
        driver.get(var_info.url_login)
        login = LoginPage(driver)
        login.enter_login_info(var_info.username_p, var_info.password_s)
        product = ProductPage(driver)

        time.sleep(5)

        # add img1
        product.click_products_img(1)

        individual_page = DetailsPage(driver)
        add = individual_page.check_single_add_to_cart()
        add.click()
        return_button = individual_page.back_button()
        return_button.click()

        # add img2
        product.click_products_img(2)
        add2 = individual_page.check_single_add_to_cart()
        add2.click()

        sign = individual_page.cart_sign()
        sign.click()

        # remove img2
        cart_page = CartPage(driver)
        cart_page.cart_product_remove(2)

        continue_buy = cart_page.cart_continue_shopping()
        continue_buy.click()

        # add index 4
        product.click_add_to_cart(4)
        p_sign = product.cart_sign()
        p_sign.click()

        checkout = cart_page.cart_checkout_button()
        checkout.click()

        client_info = ClientInfoPage(driver)
        client_info.input_first_name("Lily")
        client_info.input_last_name("Wang")
        client_info.input_zipcode("88599")

        client_info.cancel_button()

        cart_page.cart_checkout_button().click()

        client_info.input_first_name("Lily")
        client_info.input_last_name("Wang")
        client_info.input_zipcode("88599")

        overview = CheckoutOverview(driver)
        o_cancel = overview.overview_cancel()
        o_cancel.click()

        individual_page.cart_sign()
        cart_page.cart_checkout_button().click()

        client_info.input_first_name("Lily")
        client_info.input_last_name("Wang")
        client_info.input_zipcode("88599")

        client_continue = client_info.continue_button()
        client_continue.click()
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
    def test_perofrmance_glitch_account_password_img(self):
        driver = self.driver
        driver.get(var_info.url_login)
        login = LoginPage(driver)
        login.enter_login_info(var_info.username_pe, var_info.password_s)
        product = ProductPage(driver)



        # add img1
        product.click_products_img(1)

        individual_page = DetailsPage(driver)
        add = individual_page.check_single_add_to_cart()
        add.click()
        return_button = individual_page.back_button()
        return_button.click()


        # add img2
        product.click_products_img(2)
        add2 = individual_page.check_single_add_to_cart()
        add2.click()

        sign = individual_page.cart_sign()
        sign.click()


        # remove img2
        cart_page = CartPage(driver)
        cart_page.cart_product_remove(2)

        continue_buy = cart_page.cart_continue_shopping()
        continue_buy.click()

        # add index 4
        product.click_add_to_cart(4)
        p_sign = product.cart_sign()
        p_sign.click()

        checkout = cart_page.cart_checkout_button()
        checkout.click()

        client_info = ClientInfoPage(driver)
        client_info.input_first_name("Lily")
        client_info.input_last_name("Wang")
        client_info.input_zipcode("88599")

        client_info.cancel_button()

        cart_page.cart_checkout_button().click()

        client_info.input_first_name("Lily")
        client_info.input_last_name("Wang")
        client_info.input_zipcode("88599")

        overview = CheckoutOverview(driver)
        o_cancel = overview.overview_cancel()
        o_cancel.click()

        individual_page.cart_sign()
        cart_page.cart_checkout_button().click()

        client_info.input_first_name("Lily")
        client_info.input_last_name("Wang")
        client_info.input_zipcode("88599")

        client_continue = client_info.continue_button()
        client_continue.click()
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












