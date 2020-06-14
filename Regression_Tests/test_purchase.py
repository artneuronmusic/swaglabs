import pytest
import os.path
import sys
import time
import datetime
import allure


sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
from Info import var_info

from Info import var_info
from Pages.login_page import LoginPage
from Pages.product_page import ProductPage
from Pages.cart_page import CartPage
from Pages.product_individual_page import DetailsPage
from Pages.general_page import GeneralPage
from Pages.client_info import ClientInfoPage
from Pages.checkout_overview import CheckoutOverview
from Utils import utils

@pytest.mark.usefixtures("driver")
class TestWebsite():

    @pytest.mark.parametrize("acc, pws", [(var_info.username_s, var_info.password_s), (var_info.username_p, var_info.password_s), (var_info.username_pe, var_info.password_s)])
    def test_order_placed_through_inventory_page(self, acc, pws):
        try:
            driver = self.driver
            driver.get(var_info.url_login)
            login = LoginPage(driver)
            login.enter_login_info(acc, pws)
            #login.enter_login_info(var_info.username_s, var_info.password_s)
            product = ProductPage(driver)
            product.click_add_to_cart(3)
            product.click_add_to_cart(5)
            general = GeneralPage(driver)
            general.cart_sign().click()
            cart_page = CartPage(driver)
            cart_page.cart_checkout_button().click()
            client_info = ClientInfoPage(driver)
            client_info.input_first_name("Leyla")
            client_info.input_last_name("Hinderson")
            client_info.input_zipcode("78990")
            client_info.continue_button().click()
            checkout_overview = CheckoutOverview(driver)
            checkout_overview.overview_finish().click()
            success_img = checkout_overview.successfully_img()
            success_note = checkout_overview.successfully_placed_order()

            assert success_note == True
            assert success_img == True


        except AssertionError as error:
            print("AssertionError occurred")
            print(error)
            cur_time = datetime.datetime.now().strftime("%H-%M-%S_%d_%m_%Y")
            testName = utils.whoami()
            screenshotName = testName + "_" + cur_time

            allure.attach(self.driver.get_screenshot_as_png(), name=screenshotName,
                          attachment_type=allure.attachment_type.PNG)
            self.driver.get_screenshot_as_file(
                "/Users/yuchienhuang/Desktop/Swag_labs/Regression_Reports/" + screenshotName + ".png")

            raise





@pytest.mark.usefixtures("driver")
class TestWholeProcess():

    @pytest.mark.parametrize("acc, pws",
                             [(var_info.username_s, var_info.password_s), (var_info.username_p, var_info.password_s),
                              (var_info.username_pe, var_info.password_s)])
    def test_order_placed_through_inventory_page(self, acc, pws):

        try:
            driver = self.driver
            driver.get(var_info.url_login)
            login = LoginPage(driver)
            login.enter_login_info(acc, pws)
            # login.enter_login_info(var_info.username_s, var_info.password_s)
            product = ProductPage(driver)
            product.click_add_to_cart(6)
            product.click_add_to_cart(3)
            product.click_add_to_cart(2)
            product.click_product_img(1)
            detail = DetailsPage(driver)
            detail.check_single_add_to_cart().click()
            general = GeneralPage(driver)
            general.cart_sign().click()
            cart_page = CartPage(driver)
            cart_page.cart_continue_shopping().click()
            product.click_add_to_cart(1)
            general.cart_sign().click()
            cart_page.cart_product_remove(1)
            cart_page.cart_checkout_button().click()
            client_info = ClientInfoPage(driver)
            client_info.input_first_name("Leyla")
            client_info.input_last_name("Hinderson")
            client_info.input_zipcode("78990")
            client_info.cancel_button().click()
            cart_page.cart_checkout_button().click()
            client_info.input_first_name("Leyla")
            client_info.input_last_name("Hinderson")
            client_info.input_zipcode("78990")
            client_info.continue_button().click()
            checkout_overview = CheckoutOverview(driver)
            checkout_overview.overview_cancel().click()
            general.cart_sign().click()
            cart_page.cart_checkout_button().click()
            client_info.input_first_name("Leyla")
            client_info.input_last_name("Hinderson")
            client_info.input_zipcode("78990")
            client_info.continue_button().click()
            checkout_overview = CheckoutOverview(driver)
            checkout_overview.overview_finish().click()
            success_img = checkout_overview.successfully_img()
            success_note = checkout_overview.successfully_placed_order()

            assert success_note == True
            assert success_img == True

        except AssertionError as error:
            print("AssertionError occurred")
            print(error)
            cur_time = datetime.datetime.now().strftime("%H-%M-%S_%d_%m_%Y")
            testName = utils.whoami()
            screenshotName = testName + "_" + cur_time

            allure.attach(self.driver.get_screenshot_as_png(), name=screenshotName,
                          attachment_type=allure.attachment_type.PNG)
            self.driver.get_screenshot_as_file(
                "/Users/yuchienhuang/Desktop/Swag_labs/Regression_Reports/" + screenshotName + ".png")

            raise


