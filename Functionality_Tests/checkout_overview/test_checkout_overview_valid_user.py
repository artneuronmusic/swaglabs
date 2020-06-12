import pytest
import os.path
import sys
import time
import allure
import datetime



sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from Info import var_info

from Pages.login_page import LoginPage
from Pages.product_page import ProductPage
from Pages.cart_page import CartPage
from Pages.client_info import ClientInfoPage
from Pages.outside_element import OutSideElement
from Pages.checkout_overview import CheckoutOverview
from Pages.general_page import GeneralPage
from Utils import utils
# #
@pytest.mark.usefixtures("driver")
class TestOverview1():

    #@pytest.mark.skip
    def test_info_displayed(self):
        try:
            driver = self.driver
            driver.get(var_info.url_login)
            driver.refresh()
            loginpage = LoginPage(driver)
            loginpage.enter_login_info(var_info.username_s, var_info.password_s)

            inventory = ProductPage(driver)
            inventory.click_add_to_cart(2)
            inventory.product_add_to_cart(4).click()
            general = GeneralPage(driver)
            general.cart_sign().click()

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

        except AssertionError as error:
            print("AssertionError occurred")
            print(error)
            cur_time = datetime.datetime.now().strftime("%H-%M-%S_%d_%m_%Y")
            testName = utils.whoami()
            screenshotName = testName + "_" + cur_time

            allure.attach(self.driver.get_screenshot_as_png(), name=screenshotName,
                          attachment_type=allure.attachment_type.PNG)
            self.driver.get_screenshot_as_file(
                "/Users/yuchienhuang/Desktop/Swag_labs/Funtionality_Reports/checkout_overview/checkout_overview_screenshots/checkout_overview_valid_user/" + screenshotName + ".png")

            raise
        except:
            print("There is an exception")
            raise

        finally:
            print("Done")

@pytest.mark.usefixtures("driver")
class TestOverview2():
    #@pytest.mark.skip
    def test_nothing_purchased_info_displayed(self):
        try:

            driver = self.driver
            driver.get(var_info.url_login)
            driver.refresh()
            loginpage = LoginPage(driver)
            loginpage.enter_login_info(var_info.username_s, var_info.password_s)

            general = GeneralPage(driver)
            general.cart_sign().click()

            cartpage = CartPage(driver)
            continue_button = cartpage.cart_checkout_button()
            continue_button.click()

            client_info = ClientInfoPage(driver)
            client_info.input_first_name("Erica")
            client_info.input_last_name("Liam")
            client_info.input_zipcode("78666")
            client_info.continue_button().click()


            cart_qty = general.cart_qty()
            overview = CheckoutOverview(driver)
            qty_item = overview.total_item()
            payment_info = overview.check_payment_all_info()
            delivery_info = overview.check_delivery_all_info()
            item_total, tax, total = overview.total_amount()
            finish_button = overview.overview_finish()
            cancel_button = overview.overview_cancel()


            #assert qty_item == 0
            #assert cart_qty == None
            assert payment_info.is_displayed() == False
            assert delivery_info.is_displayed() == False
            assert item_total == "Item total: $0"
            assert tax == "Tax: $0.00"
            assert total == "Total: $0.00"
            assert finish_button.is_displayed()
            assert cancel_button.is_displayed()



        except AssertionError as error:
            print("AssertionError occurred")
            print(error)
            cur_time = datetime.datetime.now().strftime("%H-%M-%S_%d_%m_%Y")
            testName = utils.whoami()
            screenshotName = testName + "_" + cur_time

            allure.attach(self.driver.get_screenshot_as_png(), name=screenshotName,
                          attachment_type=allure.attachment_type.PNG)
            self.driver.get_screenshot_as_file(
                "/Users/yuchienhuang/Desktop/Swag_labs/Funtionality_Reports/checkout_overview/checkout_overview_screenshots/checkout_overview_valid_user/" + screenshotName + ".png")

            raise
        except:
            print("There is an exception")
            raise

        finally:
            print("Done")

@pytest.mark.usefixtures("driver")
class TestOverview3():
    #@pytest.mark.skip
    def test_successful_order(self):
        try:
            driver = self.driver
            driver.get(var_info.url_login)
            driver.refresh()
            loginpage = LoginPage(driver)
            loginpage.enter_login_info(var_info.username_s, var_info.password_s)

            inventory = ProductPage(driver)
            inventory.click_add_to_cart(2)
            inventory.product_add_to_cart(4).click()
            general = GeneralPage(driver)
            general.cart_sign().click()


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
            finish_button = overview.overview_finish()
            finish_button.click()
            successful_order = overview.successfully_placed_order()
            successful_img = overview.successfully_img()
            final_cart_qty = outside.cart_qty()


            assert successful_order.is_displayed()
            assert successful_order.text == "THANK YOU FOR YOUR ORDER"
            assert successful_img == True
            assert final_cart_qty == None
            assert driver.current_url == "https://www.saucedemo.com/checkout-complete.html"


        except AssertionError as error:
            print("AssertionError occurred")
            print(error)
            cur_time = datetime.datetime.now().strftime("%H-%M-%S_%d_%m_%Y")
            testName = utils.whoami()
            screenshotName = testName + "_" + cur_time

            allure.attach(self.driver.get_screenshot_as_png(), name=screenshotName,
                          attachment_type=allure.attachment_type.PNG)
            self.driver.get_screenshot_as_file(
                "/Users/yuchienhuang/Desktop/Swag_labs/Funtionality_Reports/checkout_overview/checkout_overview_screenshots/checkout_overview_valid_user/" + screenshotName + ".png")

            raise
        except:
            print("There is an exception")
            raise

        finally:
            print("Done")

@pytest.mark.usefixtures("driver")
class TestOverview4():

    def test_cancel_order(self):
        try:
            driver = self.driver
            driver.get(var_info.url_login)
            driver.refresh()
            loginpage = LoginPage(driver)
            loginpage.enter_login_info(var_info.username_s, var_info.password_s)

            inventory = ProductPage(driver)
            inventory.click_add_to_cart(2)
            inventory.product_add_to_cart(4).click()
            general = GeneralPage(driver)
            general.cart_sign().click()

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


        except AssertionError as error:
            print("AssertionError occurred")
            print(error)
            cur_time = datetime.datetime.now().strftime("%H-%M-%S_%d_%m_%Y")
            testName = utils.whoami()
            screenshotName = testName + "_" + cur_time

            allure.attach(self.driver.get_screenshot_as_png(), name=screenshotName,
                          attachment_type=allure.attachment_type.PNG)
            self.driver.get_screenshot_as_file(
                "/Users/yuchienhuang/Desktop/Swag_labs/Funtionality_Reports/checkout_overview/checkout_overview_screenshots/checkout_overview_valid_user/" + screenshotName + ".png")

            raise
        except:
            print("There is an exception")
            raise

        finally:
            print("Done")



@pytest.mark.usefixtures("driver")
class TestOverview5():

    def test_reset_order(self):
        try:

            driver = self.driver
            driver.get(var_info.url_login)
            driver.refresh()
            loginpage = LoginPage(driver)
            loginpage.enter_login_info(var_info.username_s, var_info.password_s)

            inventory = ProductPage(driver)
            inventory.click_add_to_cart(2)
            inventory.product_add_to_cart(4).click()
            general = GeneralPage(driver)
            general.cart_sign().click()

            cartpage = CartPage(driver)
            continue_button = cartpage.cart_checkout_button()
            continue_button.click()

            client_info = ClientInfoPage(driver)
            client_info.input_first_name("Erica")
            client_info.input_last_name("Liam")
            client_info.input_zipcode("78666")
            client_info.continue_button().click()

            outside = OutSideElement(driver)
            overview = CheckoutOverview(driver)
            overview.overview_finish().click()
            general.drop_down_menu()
            general.pick_item_from_menu("Reset App State")
            general.delete_menu().click()
            final_cart_qty = outside.cart_qty()


            assert final_cart_qty == None
            assert driver.current_url == "https://www.saucedemo.com/checkout-complete.html"


        except AssertionError as error:
            print("AssertionError occurred")
            print(error)
            cur_time = datetime.datetime.now().strftime("%H-%M-%S_%d_%m_%Y")
            testName = utils.whoami()
            screenshotName = testName + "_" + cur_time

            allure.attach(self.driver.get_screenshot_as_png(), name=screenshotName,
                          attachment_type=allure.attachment_type.PNG)
            self.driver.get_screenshot_as_file(
                "/Users/yuchienhuang/Desktop/Swag_labs/Funtionality_Reports/checkout_overview/checkout_overview_screenshots/checkout_overview_valid_user/" + screenshotName + ".png")

            raise
        except:
            print("There is an exception")
            raise

        finally:
            print("Done")








