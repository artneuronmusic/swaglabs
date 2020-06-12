import pytest
import os.path
import sys
import time
import datetime
import allure


sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
from Info import var_info
from Pages.product_individual_page import DetailsPage
from Pages.login_page import LoginPage
from Pages.product_page import ProductPage
from Pages.cart_page import CartPage
from Pages.client_info import ClientInfoPage
from Pages.checkout_overview import CheckoutOverview
from Pages.outside_element import OutSideElement
from Pages.general_page import GeneralPage
from Utils import utils




@pytest.mark.usefixtures("driver")
class TestClientInfoPage():

    #@pytest.mark.skip
    #since the default is no product, so the information should not go through if clicking continue
    def test_valid_info_checkout(self):
        try:
            driver = self.driver
            driver.get(var_info.url_login)
            login = LoginPage(driver)
            # get account and password
            login.enter_login_info(var_info.username_p, var_info.password_s)
            general = GeneralPage(driver)
            general.cart_sign().click()
            cartpage = CartPage(driver)
            time.sleep(3)
            cartpage.cart_checkout_button().click()
            info_page = ClientInfoPage(driver)
            info_page.input_first_name("Jojo")
            info_page.input_last_name("Wang")
            info_page.input_zipcode("77759")
            continue_button = info_page.continue_button()
            continue_button.click()

            cart_sign = info_page.info_cart_sign()
            cart_qty = info_page.info_cart_qty()

            assert driver.current_url == "https://www.saucedemo.com/checkout-step-two.html"
            assert cart_sign.is_displayed()
            assert cart_qty == None

        except AssertionError as error:
            print("AssertionError occurred")
            print(error)
            cur_time = datetime.datetime.now().strftime("%H-%M-%S_%d_%m_%Y")
            testName = utils.whoami()
            screenshotName = testName + "_" + cur_time

            allure.attach(self.driver.get_screenshot_as_png(), name=screenshotName,
                          attachment_type=allure.attachment_type.PNG)
            self.driver.get_screenshot_as_file(
                "/Users/yuchienhuang/Desktop/Swag_labs/Funtionality_Reports/client_info/client_info_screenshots//Users/yuchienhuang/Desktop/Swag_labs/Funtionality_Reports/client_info/client_info_screenshots/client_info_page_problem_user/" + screenshotName + ".png")

            raise


    def test_valid_info_cancel(self):
        try:
            driver = self.driver
            driver.get(var_info.url_login)
            login = LoginPage(driver)
            # get account and password
            login.enter_login_info(var_info.username_p, var_info.password_s)
            general = GeneralPage(driver)
            general.cart_sign().click()
            cartpage = CartPage(driver)
            cartpage.cart_checkout_button().click()
            info_page = ClientInfoPage(driver)
            info_page.input_first_name("Jojo")
            info_page.input_last_name("Wang")
            info_page.input_zipcode("77759")
            cancel_button = info_page.cancel_button()
            cancel_button.click()

            cart_sign = info_page.info_cart_sign()
            cart_qty = info_page.info_cart_qty()

            assert driver.current_url == "https://www.saucedemo.com/cart.html"
            assert cart_sign.is_displayed()
            assert cart_qty == None

        except AssertionError as error:
            print("AssertionError occurred")
            print(error)
            cur_time = datetime.datetime.now().strftime("%H-%M-%S_%d_%m_%Y")
            testName = utils.whoami()
            screenshotName = testName + "_" + cur_time

            allure.attach(self.driver.get_screenshot_as_png(), name=screenshotName,
                          attachment_type=allure.attachment_type.PNG)
            self.driver.get_screenshot_as_file(
                "/Users/yuchienhuang/Desktop/Swag_labs/Funtionality_Reports/client_info/client_info_screenshots/client_info_page_problem_user/" + screenshotName + ".png")

            raise


    #@pytest.mark.skip
    def test_blank_info_cancel(self):
        try:
            driver = self.driver
            driver.get(var_info.url_login)
            login = LoginPage(driver)
            # get account and password
            login.enter_login_info(var_info.username_p, var_info.password_s)
            general = GeneralPage(driver)
            general.cart_sign().click()
            cartpage = CartPage(driver)
            time.sleep(3)
            cartpage.cart_checkout_button().click()
            info_page = ClientInfoPage(driver)

            info_page.input_first_name("")
            info_page.input_last_name("")
            info_page.input_zipcode("")
            info_page.cancel_button().click()

            assert driver.current_url == "https://www.saucedemo.com/cart.html"

        except AssertionError as error:
            print("AssertionError occurred")
            print(error)
            cur_time = datetime.datetime.now().strftime("%H-%M-%S_%d_%m_%Y")
            testName = utils.whoami()
            screenshotName = testName + "_" + cur_time

            allure.attach(self.driver.get_screenshot_as_png(), name=screenshotName,
                          attachment_type=allure.attachment_type.PNG)
            self.driver.get_screenshot_as_file(
                "/Users/yuchienhuang/Desktop/Swag_labs/Funtionality_Reports/client_info/client_info_screenshots/client_info_page_problem_user/" + screenshotName + ".png")

            raise


     # @pytest.mark.skip

    def test_blank_info_continue(self):
        try:
            driver = self.driver
            driver.get(var_info.url_login)
            login = LoginPage(driver)
            # get account and password
            login.enter_login_info(var_info.username_p, var_info.password_s)
            general = GeneralPage(driver)
            general.cart_sign().click()
            cartpage = CartPage(driver)
            time.sleep(3)
            cartpage.cart_checkout_button().click()
            info_page = ClientInfoPage(driver)

            info_page.input_first_name("")
            info_page.input_last_name("")
            info_page.input_zipcode("")
            info_page.continue_button().click()
            warning = info_page.warning_sign()

            assert driver.current_url == "https://www.saucedemo.com/checkout-step-one.html"
            assert warning.text == "Error: First Name is required"

        except AssertionError as error:
            print("AssertionError occurred")
            print(error)
            cur_time = datetime.datetime.now().strftime("%H-%M-%S_%d_%m_%Y")
            testName = utils.whoami()
            screenshotName = testName + "_" + cur_time

            allure.attach(self.driver.get_screenshot_as_png(), name=screenshotName,
                          attachment_type=allure.attachment_type.PNG)
            self.driver.get_screenshot_as_file(
                "/Users/yuchienhuang/Desktop/Swag_labs/Funtionality_Reports/client_info/client_info_screenshots/client_info_page_problem_user/" + screenshotName + ".png")

            raise


    #@pytest.mark.skip
    def test_blank_first_name_continue(self):
        try:
            driver = self.driver
            driver.get(var_info.url_login)
            login = LoginPage(driver)
            # get account and password
            login.enter_login_info(var_info.username_p, var_info.password_s)
            general = GeneralPage(driver)
            general.cart_sign().click()
            cartpage = CartPage(driver)
            time.sleep(3)
            cartpage.cart_checkout_button().click()
            info_page = ClientInfoPage(driver)

            info_page.input_first_name("")
            info_page.input_last_name("Korh")
            info_page.input_zipcode("77759")
            c_button = info_page.continue_button()
            c_button.click()
            time.sleep(3)
            warning = info_page.warning_sign()

            assert warning.text == "Error: First Name is required"

        except AssertionError as error:
            print("AssertionError occurred")
            print(error)
            cur_time = datetime.datetime.now().strftime("%H-%M-%S_%d_%m_%Y")
            testName = utils.whoami()
            screenshotName = testName + "_" + cur_time

            allure.attach(self.driver.get_screenshot_as_png(), name=screenshotName,
                          attachment_type=allure.attachment_type.PNG)
            self.driver.get_screenshot_as_file(
                "/Users/yuchienhuang/Desktop/Swag_labs/Funtionality_Reports/client_info/client_info_screenshots/client_info_page_problem_user/" + screenshotName + ".png")

            raise


    #@pytest.mark.skip
    def test_blank_last_name_continue(self):
        try:
            driver = self.driver
            driver.get(var_info.url_login)
            login = LoginPage(driver)
            # get account and password
            login.enter_login_info(var_info.username_p, var_info.password_s)
            general = GeneralPage(driver)
            general.cart_sign().click()
            cartpage = CartPage(driver)
            time.sleep(3)
            cartpage.cart_checkout_button().click()
            info_page = ClientInfoPage(driver)

            info_page.input_first_name("JOJO")
            info_page.input_last_name("")
            info_page.input_zipcode("77759")
            c_button = info_page.continue_button()
            c_button.click()

            warning = info_page.warning_sign()

            assert warning.text == "Error: Last Name is required"

        except AssertionError as error:
            print("AssertionError occurred")
            print(error)
            cur_time = datetime.datetime.now().strftime("%H-%M-%S_%d_%m_%Y")
            testName = utils.whoami()
            screenshotName = testName + "_" + cur_time

            allure.attach(self.driver.get_screenshot_as_png(), name=screenshotName,
                          attachment_type=allure.attachment_type.PNG)
            self.driver.get_screenshot_as_file(
                "/Users/yuchienhuang/Desktop/Swag_labs/Funtionality_Reports/client_info/client_info_screenshots/client_info_page_problem_user/" + screenshotName + ".png")

            raise

    #@pytest.mark.skip
    def test_blank_zipcode_continue(self):
        try:
            driver = self.driver
            driver.get(var_info.url_login)
            login = LoginPage(driver)
            # get account and password
            login.enter_login_info(var_info.username_p, var_info.password_s)
            general = GeneralPage(driver)
            general.cart_sign().click()
            cartpage = CartPage(driver)
            time.sleep(3)
            cartpage.cart_checkout_button().click()
            info_page = ClientInfoPage(driver)

            info_page.input_first_name("Jojo")
            info_page.input_last_name("Kong")
            info_page.input_zipcode("")
            c_button = info_page.continue_button()
            c_button.click()

            warning = info_page.warning_sign()

            assert warning.text == "Error: Postal Code is required"

        except AssertionError as error:
            print("AssertionError occurred")
            print(error)
            cur_time = datetime.datetime.now().strftime("%H-%M-%S_%d_%m_%Y")
            testName = utils.whoami()
            screenshotName = testName + "_" + cur_time

            allure.attach(self.driver.get_screenshot_as_png(), name=screenshotName,
                          attachment_type=allure.attachment_type.PNG)
            self.driver.get_screenshot_as_file(
                "/Users/yuchienhuang/Desktop/Swag_labs/Funtionality_Reports/client_info/client_info_screenshots/client_info_page_problem_user/" + screenshotName + ".png")

            raise

    #
    #@pytest.mark.skip
    def test_with_character_zipcode_continue(self):
        try:
            driver = self.driver
            driver.get(var_info.url_login)
            login = LoginPage(driver)
            # get account and password
            login.enter_login_info(var_info.username_p, var_info.password_s)
            general = GeneralPage(driver)
            general.cart_sign().click()
            cartpage = CartPage(driver)
            time.sleep(3)
            cartpage.cart_checkout_button().click()
            info_page = ClientInfoPage(driver)

            info_page.input_first_name("Jojo")
            info_page.input_last_name("Kong")
            info_page.input_zipcode("$%667")

            c_button = info_page.continue_button()
            c_button.click()
            warning = info_page.warning_sign()

            assert warning == True
            assert driver.current_url != "https://www.saucedemo.com/checkout-step-two.html"

        except AssertionError as error:
            print("AssertionError occurred")
            print(error)
            cur_time = datetime.datetime.now().strftime("%H-%M-%S_%d_%m_%Y")
            testName = utils.whoami()
            screenshotName = testName + "_" + cur_time

            allure.attach(self.driver.get_screenshot_as_png(), name=screenshotName,
                          attachment_type=allure.attachment_type.PNG)
            self.driver.get_screenshot_as_file(
                "/Users/yuchienhuang/Desktop/Swag_labs/Funtionality_Reports/client_info/client_info_screenshots/client_info_page_problem_user/" + screenshotName + ".png")

            raise


    #
    #@pytest.mark.skip
    #those fill in  should not be any characters
    def test_with_character_all_info(self):
        try:
            driver = self.driver
            driver.get(var_info.url_login)
            login = LoginPage(driver)
            # get account and password
            login.enter_login_info(var_info.username_p, var_info.password_s)
            general = GeneralPage(driver)
            general.cart_sign().click()
            cartpage = CartPage(driver)
            time.sleep(3)
            cartpage.cart_checkout_button().click()
            info_page = ClientInfoPage(driver)

            info_page.input_first_name("@#$%^")
            info_page.input_last_name("#$%^")
            info_page.input_zipcode("$%667")
            c_button = info_page.continue_button()
            c_button.click()

            warning = info_page.warning_sign()

            assert warning == True
            assert driver.current_url != "https://www.saucedemo.com/checkout-step-two.html"

        except AssertionError as error:
            print("AssertionError occurred")
            print(error)
            cur_time = datetime.datetime.now().strftime("%H-%M-%S_%d_%m_%Y")
            testName = utils.whoami()
            screenshotName = testName + "_" + cur_time

            allure.attach(self.driver.get_screenshot_as_png(), name=screenshotName,
                          attachment_type=allure.attachment_type.PNG)
            self.driver.get_screenshot_as_file(
                "/Users/yuchienhuang/Desktop/Swag_labs/Funtionality_Reports/client_info/client_info_screenshots/client_info_page_problem_user/" + screenshotName + ".png")

            raise


@pytest.mark.usefixtures("driver")
class TestBillPage():
    # #if there is nothing, there should be no payment info, delivery info
    # #@pytest.mark.skip
    def test_info_display_default(self):
        try:
            driver = self.driver
            driver.get(var_info.url_login)
            login = LoginPage(driver)
            # get account and password
            login.enter_login_info(var_info.username_p, var_info.password_s)
            general = GeneralPage(driver)
            general.cart_sign().click()
            cartpage = CartPage(driver)
            time.sleep(3)
            cartpage.cart_checkout_button().click()
            info_page = ClientInfoPage(driver)

            info_page.input_first_name("Jill")
            info_page.input_last_name("Norstrom^")
            info_page.input_zipcode("77888")
            c_button = info_page.continue_button()
            c_button.click()
            overview = CheckoutOverview(driver)
            items = overview.total_product_in_cart()
            payment = overview.check_payment_all_info()
            delivery = overview.check_delivery_all_info()
            amount = overview.total_amount()

            assert items == None
            assert payment.is_displayed() == False
            assert delivery.is_displayed() == False
            assert isinstance(amount, list) == False

        except AssertionError as error:
            print("AssertionError occurred")
            print(error)
            cur_time = datetime.datetime.now().strftime("%H-%M-%S_%d_%m_%Y")
            testName = utils.whoami()
            screenshotName = testName + "_" + cur_time

            allure.attach(self.driver.get_screenshot_as_png(), name=screenshotName,
                          attachment_type=allure.attachment_type.PNG)
            self.driver.get_screenshot_as_file(
                "/Users/yuchienhuang/Desktop/Swag_labs/Funtionality_Reports/client_info/client_info_screenshots/client_info_page_problem_user/" + screenshotName + ".png")

            raise


    #@pytest.mark.skip
    def test_finish_with_default(self):
        try:
            driver = self.driver
            driver.get(var_info.url_login)
            login = LoginPage(driver)
            # get account and password
            login.enter_login_info(var_info.username_p, var_info.password_s)
            general = GeneralPage(driver)
            general.cart_sign().click()
            cartpage = CartPage(driver)
            time.sleep(3)
            cartpage.cart_checkout_button().click()
            info_page = ClientInfoPage(driver)

            info_page.input_first_name("Jill")
            info_page.input_last_name("Norstrom^")
            info_page.input_zipcode("77888")
            c_button = info_page.continue_button()
            c_button.click()
            overview = CheckoutOverview(driver)
            result = overview.overview_finish()
            result.click()

            assert result != "https://www.saucedemo.com/checkout-complete.html"

        except AssertionError as error:
            print("AssertionError occurred")
            print(error)
            cur_time = datetime.datetime.now().strftime("%H-%M-%S_%d_%m_%Y")
            testName = utils.whoami()
            screenshotName = testName + "_" + cur_time

            allure.attach(self.driver.get_screenshot_as_png(), name=screenshotName,
                          attachment_type=allure.attachment_type.PNG)
            self.driver.get_screenshot_as_file(
                "/Users/yuchienhuang/Desktop/Swag_labs/Funtionality_Reports/client_info/client_info_screenshots/client_info_page_problem_user/" + screenshotName + ".png")

            raise


    #@pytest.mark.skip
    def test_cancel_with_default(self):
        try:
            driver = self.driver
            driver.get(var_info.url_login)
            login = LoginPage(driver)
            # get account and password
            login.enter_login_info(var_info.username_p, var_info.password_s)
            general = GeneralPage(driver)
            general.cart_sign().click()
            cartpage = CartPage(driver)
            time.sleep(3)
            cartpage.cart_checkout_button().click()
            info_page = ClientInfoPage(driver)
            info_page.input_first_name("Jill")
            info_page.input_last_name("Norstrom^")
            info_page.input_zipcode("77888")
            c_button = info_page.continue_button()
            c_button.click()
            overview = CheckoutOverview(driver)
            cancel = overview.overview_cancel()
            cancel.click()

            assert driver.current_url == ("https://www.saucedemo.com/inventory.html")

        except AssertionError as error:
            print("AssertionError occurred")
            print(error)
            cur_time = datetime.datetime.now().strftime("%H-%M-%S_%d_%m_%Y")
            testName = utils.whoami()
            screenshotName = testName + "_" + cur_time

            allure.attach(self.driver.get_screenshot_as_png(), name=screenshotName,
                          attachment_type=allure.attachment_type.PNG)
            self.driver.get_screenshot_as_file(
                "/Users/yuchienhuang/Desktop/Swag_labs/Funtionality_Reports/client_info/client_info_screenshots/client_info_page_problem_user/" + screenshotName + ".png")

            raise


    #@pytest.mark.skip
    def test_cancel_on_your_information(self):
        try:
            driver = self.driver
            driver.get(var_info.url_login)
            login = LoginPage(driver)
            # get account and password
            login.enter_login_info(var_info.username_p, var_info.password_s)
            product = ProductPage(driver)
            product.click_add_to_cart(2)
            product.click_add_to_cart(6)
            general = GeneralPage(driver)
            sign = general.cart_sign()
            sign.click()

            cart = CartPage(driver)
            checkout_button = cart.cart_checkout_button()
            checkout_button.click()
            info_page = ClientInfoPage(driver)
            info_page.cancel_button().click()
            qty = general.cart_qty()
            total = cart.total_product_in_cart()

            assert driver.current_url == "https://www.saucedemo.com/cart.html"
            assert qty.text == "2"
            assert total == 2

        except AssertionError as error:
            print("AssertionError occurred")
            print(error)
            cur_time = datetime.datetime.now().strftime("%H-%M-%S_%d_%m_%Y")
            testName = utils.whoami()
            screenshotName = testName + "_" + cur_time

            allure.attach(self.driver.get_screenshot_as_png(), name=screenshotName,
                          attachment_type=allure.attachment_type.PNG)
            self.driver.get_screenshot_as_file(
                "/Users/yuchienhuang/Desktop/Swag_labs/Funtionality_Reports/client_info/client_info_screenshots/client_info_page_problem_user/" + screenshotName + ".png")

            raise


    #@pytest.mark.skip
    def test_reset_with_items_overview(self):
        try:
            driver = self.driver
            driver.get(var_info.url_login)
            login = LoginPage(driver)
            # get account and password
            login.enter_login_info(var_info.username_p, var_info.password_s)
            product = ProductPage(driver)
            product.click_add_to_cart(2)
            product.click_add_to_cart(6)
            general = GeneralPage(driver)
            sign = general.cart_sign()
            sign.click()

            cart = CartPage(driver)
            checkout_button = cart.cart_checkout_button()
            checkout_button.click()

            info_page = ClientInfoPage(driver)
            info_page.input_first_name("Jill")
            info_page.input_last_name("Maddison")
            info_page.input_zipcode("10990")
            c_button = info_page.continue_button()
            c_button.click()
            time.sleep(3)
            general.drop_down_menu()
            general.pick_item_from_menu("Reset App State")
            general.delete_menu().click()

            overview = CheckoutOverview(driver)
            total_product = overview.total_product_in_cart()
            time.sleep(5)

            qty = general.cart_qty()

            assert qty == None
            assert total_product == None

        except AssertionError as error:
            print("AssertionError occurred")
            print(error)
            cur_time = datetime.datetime.now().strftime("%H-%M-%S_%d_%m_%Y")
            testName = utils.whoami()
            screenshotName = testName + "_" + cur_time

            allure.attach(self.driver.get_screenshot_as_png(), name=screenshotName,
                          attachment_type=allure.attachment_type.PNG)
            self.driver.get_screenshot_as_file(
                "/Users/yuchienhuang/Desktop/Swag_labs/Funtionality_Reports/client_info/client_info_screenshots/client_info_page_problem_user/" + screenshotName + ".png")

            raise


#
@pytest.mark.usefixtures("driver")
class TestLastProcess1():

    #@pytest.mark.skip
    def test_purchase_successfully_with_products(self):
        try:
            driver = self.driver
            driver.get(var_info.url_login)
            login = LoginPage(driver)
            # get account and password
            login.enter_login_info(var_info.username_p, var_info.password_s)

            product = ProductPage(driver)
            product.click_add_to_cart(2)
            product.click_add_to_cart(6)
            general = GeneralPage(driver)
            sign = general.cart_sign()
            sign.click()

            cart = CartPage(driver)
            checkout_button = cart.cart_checkout_button()
            checkout_button.click()

            info_page = ClientInfoPage(driver)
            info_page.input_first_name("Jill")
            info_page.input_last_name("Maddison")
            info_page.input_zipcode("10990")
            c_button = info_page.continue_button()
            c_button.click()

            overview = CheckoutOverview(driver)
            result = overview.overview_finish()
            result.click()
            success = overview.successfully_img()

            general = GeneralPage(driver)
            qty = general.cart_qty()
            sign = general.cart_sign()

            assert success == True
            assert driver.current_url == "https://www.saucedemo.com/checkout-complete.html"
            assert qty == None
            assert sign.is_displayed()

        except AssertionError as error:
            print("AssertionError occurred")
            print(error)
            cur_time = datetime.datetime.now().strftime("%H-%M-%S_%d_%m_%Y")
            testName = utils.whoami()
            screenshotName = testName + "_" + cur_time

            allure.attach(self.driver.get_screenshot_as_png(), name=screenshotName,
                          attachment_type=allure.attachment_type.PNG)
            self.driver.get_screenshot_as_file(
                "/Users/yuchienhuang/Desktop/Swag_labs/Funtionality_Reports/client_info/client_info_screenshots/client_info_page_problem_user/" + screenshotName + ".png")

            raise

@pytest.mark.usefixtures("driver")
class TestLastProcess2():

    #product
    #@pytest.mark.skip
    def test_cancel_purchase_before_complete(self):
        try:
            driver = self.driver
            driver.get(var_info.url_login)
            login = LoginPage(driver)
            # get account and password
            login.enter_login_info(var_info.username_p, var_info.password_s)

            product = ProductPage(driver)
            product.click_add_to_cart(2)
            product.click_add_to_cart(6)
            time.sleep(3)
            general = GeneralPage(driver)
            sign = general.cart_sign()
            sign.click()
            cart = CartPage(driver)
            checkout_button = cart.cart_checkout_button()
            checkout_button.click()

            info_page = ClientInfoPage(driver)
            info_page.input_first_name("Jill")
            info_page.input_last_name("Maddison")
            info_page.input_zipcode("10990")
            c_button = info_page.continue_button()
            c_button.click()

            overview = CheckoutOverview(driver)
            result = overview.overview_cancel()
            result.click()


            product2 = product.product_add_to_cart(2)
            product6 = product.product_add_to_cart(6)

            assert product2.text == "REMOVE"
            assert product6.text == "REMOVE"

        except AssertionError as error:
            print("AssertionError occurred")
            print(error)
            cur_time = datetime.datetime.now().strftime("%H-%M-%S_%d_%m_%Y")
            testName = utils.whoami()
            screenshotName = testName + "_" + cur_time

            allure.attach(self.driver.get_screenshot_as_png(), name=screenshotName,
                          attachment_type=allure.attachment_type.PNG)
            self.driver.get_screenshot_as_file(
                "/Users/yuchienhuang/Desktop/Swag_labs/Funtionality_Reports/client_info/client_info_screenshots/client_info_page_problem_user/" + screenshotName + ".png")

            raise
