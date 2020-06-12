
import pytest
import os.path
import sys
import time
import datetime
import allure


sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
from Info import var_info
from Pages.login_page import LoginPage
from Pages.product_page import ProductPage
from Pages.cart_page import CartPage
from Pages.product_individual_page import DetailsPage
from Pages.general_page import GeneralPage
from Utils import utils

#one error will be found out in def test_reset_button
#reset the app in cart page, however, only qty of cart gets done, the content

@pytest.mark.usefixtures("driver")
class TestCartPageWithoutProducts():

    #@pytest.mark.skip
    #should not
    def test_a_cart_with_no_product_product_page(self):
        try:
            driver = self.driver
            driver.get(var_info.url_login)
            login = LoginPage(driver)

            # get account and password
            login.enter_login_info(var_info.username_pe, var_info.password_s)
            product = ProductPage(driver)
            general = GeneralPage(driver)
            general.cart_sign().click()
            cart = CartPage(driver)
            title = cart.cart_title()
            qty_label = cart.cart_qty_label()
            desc_label = cart.cart_desc_label()
            items_display = cart.total_product_in_cart()

            assert title.text == "Your Cart"
            assert qty_label.is_displayed()
            assert desc_label.is_displayed()
            assert items_display == None

        except AssertionError as error:
            print("AssertionError occurred")
            print(error)
            cur_time = datetime.datetime.now().strftime("%H-%M-%S_%d_%m_%Y")
            testName = utils.whoami()
            screenshotName = testName + "_" + cur_time

            allure.attach(self.driver.get_screenshot_as_png(), name=screenshotName,
                          attachment_type=allure.attachment_type.PNG)
            self.driver.get_screenshot_as_file("/Users/yuchienhuang/Desktop/Swag_labs/Funtionality_Reports/cart_page/cart_page_screenshots/cart_page_performance_glitch/" + screenshotName + ".png")

            raise


    #@pytest.mark.skip
    # should not
    def test_no_product_no_checkout_page(self):
        try:
            driver = self.driver
            driver.get(var_info.url_login)
            login = LoginPage(driver)
            login.enter_login_info(var_info.username_pe, var_info.password_s)
            product = ProductPage(driver)
            general = GeneralPage(driver)
            general.cart_sign().click()
            cart = CartPage(driver)
            checkout_button = cart.cart_checkout_button()
            checkout_button.click()

            assert driver.current_url == "https://www.saucedemo.com/checkout-step-one.html"

        except AssertionError as error:
            print("AssertionError occurred")
            print(error)
            cur_time = datetime.datetime.now().strftime("%H-%M-%S_%d_%m_%Y")
            testName = utils.whoami()
            screenshotName = testName + "_" + cur_time

            allure.attach(self.driver.get_screenshot_as_png(), name=screenshotName,
                          attachment_type=allure.attachment_type.PNG)
            self.driver.get_screenshot_as_file("/Users/yuchienhuang/Desktop/Swag_labs/Funtionality_Reports/cart_page/cart_page_screenshots/cart_page_performance_glitch/" + screenshotName + ".png")

            raise


    #@pytest.mark.skip
    # should not
    def test_no_product_continue_shopping(self):
        try:
            driver = self.driver
            driver.get(var_info.url_login)
            login = LoginPage(driver)
            login.enter_login_info(var_info.username_pe, var_info.password_s)
            product = ProductPage(driver)
            general = GeneralPage(driver)
            general.cart_sign().click()
            cart = CartPage(driver)
            shopping_button = cart.cart_continue_shopping()
            shopping_button.click()

            assert driver.current_url == "https://www.saucedemo.com/inventory.html"


        except AssertionError as error:
            print("AssertionError occurred")
            print(error)
            cur_time = datetime.datetime.now().strftime("%H-%M-%S_%d_%m_%Y")
            testName = utils.whoami()
            screenshotName = testName + "_" + cur_time

            allure.attach(self.driver.get_screenshot_as_png(), name=screenshotName,
                          attachment_type=allure.attachment_type.PNG)
            self.driver.get_screenshot_as_file("/Users/yuchienhuang/Desktop/Swag_labs/Funtionality_Reports/cart_page/cart_page_screenshots/cart_page_performance_glitch/" + screenshotName + ".png")

            raise



@pytest.mark.usefixtures("driver")
class TestDisplay1():

    #@pytest.mark.skip
    def test_displayed_products_in_page(self):
        try:

            driver = self.driver
            driver.get(var_info.url_login)
            login = LoginPage(driver)
            # get account and password
            login.enter_login_info(var_info.username_pe, var_info.password_s)
            product = ProductPage(driver)
            product.click_add_to_cart(2)
            product.click_add_to_cart(6)

            general = GeneralPage(driver)
            general.cart_sign().click()
            cart = CartPage(driver)
            items_display = cart.total_product_in_cart()
            qty = general.cart_qty()

            assert items_display == 2
            assert qty.text == "2"


        except AssertionError as error:
            print("AssertionError occurred")
            print(error)
            cur_time = datetime.datetime.now().strftime("%H-%M-%S_%d_%m_%Y")
            testName = utils.whoami()
            screenshotName = testName + "_" + cur_time

            allure.attach(self.driver.get_screenshot_as_png(), name=screenshotName,
                          attachment_type=allure.attachment_type.PNG)
            self.driver.get_screenshot_as_file("/Users/yuchienhuang/Desktop/Swag_labs/Funtionality_Reports/cart_page/cart_page_screenshots/cart_page_performance_glitch/" + screenshotName + ".png")

            raise


@pytest.mark.usefixtures("driver")
class TestDisplay2():
    #@pytest.mark.skip
    #checkout successfully
    def test_displayed_products_checkout_button(self):
        try:

            driver = self.driver
            driver.get(var_info.url_login)
            login = LoginPage(driver)
            # get account and password
            login.enter_login_info(var_info.username_pe, var_info.password_s)
            driver = self.driver
            driver.get(var_info.url_product)
            product = ProductPage(driver)
            product.click_add_to_cart(2)
            product.click_add_to_cart(6)
            general = GeneralPage(driver)
            general.cart_sign().click()
            cart = CartPage(driver)
            checkout_button = cart.cart_checkout_button()
            checkout_button.click()

            assert driver.current_url == "https://www.saucedemo.com/checkout-step-one.html"


        except AssertionError as error:
            print("AssertionError occurred")
            print(error)
            cur_time = datetime.datetime.now().strftime("%H-%M-%S_%d_%m_%Y")
            testName = utils.whoami()
            screenshotName = testName + "_" + cur_time

            allure.attach(self.driver.get_screenshot_as_png(), name=screenshotName,
                          attachment_type=allure.attachment_type.PNG)
            self.driver.get_screenshot_as_file("/Users/yuchienhuang/Desktop/Swag_labs/Funtionality_Reports/cart_page/cart_page_screenshots/cart_page_performance_glitch/" + screenshotName + ".png")

            raise



@pytest.mark.usefixtures("driver")
class TestDisplay3():
    #@pytest.mark.skip
    def test_remove_checkout(self):
        try:
            driver = self.driver
            driver.get(var_info.url_login)
            login = LoginPage(driver)
            login.enter_login_info(var_info.username_pe, var_info.password_s)
            product = ProductPage(driver)
            product.click_add_to_cart(2)
            product.click_add_to_cart(6)
            general = GeneralPage(driver)
            general.cart_sign().click()
            cart = CartPage(driver)
            cart.cart_product_remove(1)
            items_display = cart.total_product_in_cart()
            qty =general.cart_qty()

            assert items_display == 1
            assert qty.text == "1"


        except AssertionError as error:
            print("AssertionError occurred")
            print(error)
            cur_time = datetime.datetime.now().strftime("%H-%M-%S_%d_%m_%Y")
            testName = utils.whoami()
            screenshotName = testName + "_" + cur_time

            allure.attach(self.driver.get_screenshot_as_png(), name=screenshotName,
                          attachment_type=allure.attachment_type.PNG)
            self.driver.get_screenshot_as_file("/Users/yuchienhuang/Desktop/Swag_labs/Funtionality_Reports/cart_page/cart_page_screenshots/cart_page_performance_glitch/" + screenshotName + ".png")

            raise



@pytest.mark.usefixtures("driver")
class TestDisplay4():
    #@pytest.mark.skip
    #redierect to prodcut page
    def test_continue_shopping_button(self):

        try:
            driver = self.driver
            driver.get(var_info.url_login)
            login = LoginPage(driver)
            login.enter_login_info(var_info.username_pe, var_info.password_s)
            product = ProductPage(driver)
            product.click_add_to_cart(2)
            product.click_add_to_cart(6)
            general = GeneralPage(driver)
            general.cart_sign().click()
            cart = CartPage(driver)
            shopping_button = cart.cart_continue_shopping()
            shopping_button.click()
            pro2 = product.product_add_to_cart(2)
            pro6 = product.product_add_to_cart(6)
            general = GeneralPage(driver)
            qty = general.cart_qty()

            assert pro2.text == "REMOVE"
            assert pro6.text == "REMOVE"
            assert driver.current_url == "https://www.saucedemo.com/inventory.html"
            assert qty.text == "2"

        except AssertionError as error:
            print("AssertionError occurred")
            print(error)
            cur_time = datetime.datetime.now().strftime("%H-%M-%S_%d_%m_%Y")
            testName = utils.whoami()
            screenshotName = testName + "_" + cur_time

            allure.attach(self.driver.get_screenshot_as_png(), name=screenshotName,
                          attachment_type=allure.attachment_type.PNG)
            self.driver.get_screenshot_as_file("/Users/yuchienhuang/Desktop/Swag_labs/Funtionality_Reports/cart_page/cart_page_screenshots/cart_page_performance_glitch/" + screenshotName + ".png")

            raise




@pytest.mark.usefixtures("driver")
class TestDisplay5():
    #@pytest.mark.skip
    #displays should be all gone, but....u will get ERROR
    def test_reset_button(self):
        try:
            driver = self.driver
            driver.get(var_info.url_login)
            login = LoginPage(driver)
            login.enter_login_info(var_info.username_pe, var_info.password_s)
            product = ProductPage(driver)
            product.click_add_to_cart(2)
            product.click_add_to_cart(6)
            general = GeneralPage(driver)
            general.cart_sign().click()
            general.drop_down_menu()
            general.pick_item_from_menu("Reset App State")
            general.display_delete_button()
            cart = CartPage(driver)
            qty = general.cart_qty()
            items_display = cart.total_product_in_cart()

            assert qty == None
            assert items_display == None #it should has nothing after hitting reset


        except AssertionError as error:
            print("AssertionError occurred")
            print(error)
            cur_time = datetime.datetime.now().strftime("%H-%M-%S_%d_%m_%Y")
            testName = utils.whoami()
            screenshotName = testName + "_" + cur_time

            allure.attach(self.driver.get_screenshot_as_png(), name=screenshotName,
                          attachment_type=allure.attachment_type.PNG)
            self.driver.get_screenshot_as_file("/Users/yuchienhuang/Desktop/Swag_labs/Funtionality_Reports/cart_page/cart_page_screenshots/cart_page_performance_glitch/" + screenshotName + ".png")

            raise


@pytest.mark.usefixtures("driver")
class TestIndividualPageToCart():

    #@pytest.mark.skip
    #it will redirect back to product page
    def test_individual_page_to_cart(self):
        try:
            driver = self.driver
            driver.get(var_info.url_login)
            login = LoginPage(driver)
            login.enter_login_info(var_info.username_pe, var_info.password_s)
            product = ProductPage(driver)
            product.click_product_label(4)
            general = GeneralPage(driver)
            individual = DetailsPage(driver)
            individual.check_single_add_to_cart().click()
            general.cart_sign().click()
            cart = CartPage(driver)
            qty = general.cart_qty()
            items_display = cart.total_product_in_cart()

            assert items_display == 1
            assert qty.text == "1"
            assert driver.current_url == "https://www.saucedemo.com/cart.html"

        except AssertionError as error:
            print("AssertionError occurred")
            print(error)
            cur_time = datetime.datetime.now().strftime("%H-%M-%S_%d_%m_%Y")
            testName = utils.whoami()
            screenshotName = testName + "_" + cur_time

            allure.attach(self.driver.get_screenshot_as_png(), name=screenshotName,
                          attachment_type=allure.attachment_type.PNG)
            self.driver.get_screenshot_as_file("/Users/yuchienhuang/Desktop/Swag_labs/Funtionality_Reports/cart_page/cart_page_screenshots/cart_page_performance_glitch/" + screenshotName + ".png")

            raise














