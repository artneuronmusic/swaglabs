import pytest
import os.path
import sys
import time
import datetime
from Utils import utils
import allure


sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from Info import var_info
from Pages.login_page import LoginPage
from Pages.product_page import ProductPage
from Pages.product_individual_page import DetailsPage
from Pages.general_page import GeneralPage
from Utils import utils

#@pytest.mark.usefixtures("test_setup")
@pytest.mark.usefixtures("driver")
class TestLoginOut():

    #@pytest.mark.skip
    #accepted:username=standard_user, pw=secret_sauce
    def test_username_password_both_valid(self):
        try:
            driver = self.driver
            #get url from var_info
            driver.get(var_info.url_login)

            #take driver into LoginPage
            login = LoginPage(driver)

            #get account and password
            login.enter_login_info(var_info.username_s, var_info.password_s)

            product = ProductPage(driver)
            general = GeneralPage(driver)
            #pick the option: "Logout"
            general.pick_item_from_menu("Logout")

            assert driver.current_url != "https://www.saucedemo.com/"
            assert driver.current_url == "https://www.saucedemo.com/index.html"

        except AssertionError as error:
            print("AssertionError occurred")
            print(error)
            cur_time = datetime.datetime.now().strftime("%H-%M-%S_%d_%m_%Y")
            testName = utils.whoami()
            screenshotName = testName + "_" + cur_time
            #screenshotName = "screenshot" + cur_time

            allure.attach(driver.get_screenshot_as_png(), name=screenshotName,
                          attachment_type=allure.attachment_type.PNG)
            driver.get_screenshot_as_file("/Users/yuchienhuang/Desktop/Swag_labs/Funtionality_Reports/login_out/login_out_screenhsots" + screenshotName + ".png")

            raise
        except:
            print("There is an exception")
            raise


    #@pytest.mark.skip
    # accepted:username=problem_user, valid pw
    def test_problem_username_password(self):
        try:
            driver = self.driver
            #get url from var_info
            driver.get(var_info.url_login)

            #take driver into LoginPage
            login = LoginPage(driver)

            #get account and password
            login.enter_login_info(var_info.username_p, var_info.password_s)

            product = ProductPage(driver)

            #pick the option: "Logout"
            general = GeneralPage(driver)
            general.pick_item_from_menu("Logout")

            assert driver.current_url != "https://www.saucedemo.com/"
            assert driver.current_url == "https://www.saucedemo.com/index.html"

        except AssertionError as error:
            print("AssertionError occurred")
            print(error)
            cur_time = datetime.datetime.now().strftime("%H-%M-%S_%d_%m_%Y")
            testName = utils.whoami()
            screenshotName = testName + "_" + cur_time
            #screenshotName = "screenshot" + cur_time

            allure.attach(driver.get_screenshot_as_png(), name=screenshotName,
                          attachment_type=allure.attachment_type.PNG)
            driver.get_screenshot_as_file("/Users/yuchienhuang/Desktop/Swag_labs/Funtionality_Reports/login_out/login_out_screenhsots" + screenshotName + ".png")

            raise
        except:
            print("Sth wrong with username")
            raise

    #@pytest.mark.skip
    # accepted:username=performance_glitch_user, pw=secret_sauce
    def test_glitch_username_password(self):
        try:
            driver = self.driver
            #get url from var_info
            driver.get(var_info.url_login)

            #take driver into LoginPage
            login = LoginPage(driver)

            #get account and password
            login.enter_login_info(var_info.username_pe, var_info.password_s)

            product = ProductPage(driver)
            general = GeneralPage(driver)
            #pick the option: "Logout"
            general.pick_item_from_menu("Logout")

            assert driver.current_url != "https://www.saucedemo.com/"
            assert driver.current_url == "https://www.saucedemo.com/index.html"

        except AssertionError as error:
            print("AssertionError occurred")
            print(error)
            cur_time = datetime.datetime.now().strftime("%H-%M-%S_%d_%m_%Y")
            testName = utils.whoami()
            screenshotName = testName + "_" + cur_time
            # screenshotName = "screenshot" + cur_time

            allure.attach(driver.get_screenshot_as_png(), name=screenshotName,
                          attachment_type=allure.attachment_type.PNG)
            driver.get_screenshot_as_file(
                "/Users/yuchienhuang/Desktop/Swag_labs/Funtionality_Reports/login_out/login_out_screenhsots" + screenshotName + ".png")

            raise
        except:
            print("Sth wrong with username")
            raise



    #@pytest.mark.skip
    # accepted:username=locked_user, pw=secret_sauce
    def test_locked_username_password(self):
        try:
            driver = self.driver
            driver.get(var_info.url_login)
            login = LoginPage(driver)
            login.enter_login_info(var_info.username_l, var_info.password_s)
            print(driver.current_url)
            error_message = login.failed_message()
            logo_title = login.title_after_login()
            print(error_message.text)


            assert logo_title == False
            assert error_message.text == "Epic sadface: Sorry, this user has been locked out."
            assert driver.current_url != "https://www.saucedemo.com/inventory.html"
            assert driver.current_url == "https://www.saucedemo.com/"

        except AssertionError as error:
            print("AssertionError occurred")
            print(error)
            cur_time = datetime.datetime.now().strftime("%H-%M-%S_%d_%m_%Y")
            testName = utils.whoami()
            screenshotName = testName + "_" + cur_time
            #screenshotName = "screenshot" + cur_time

            allure.attach(driver.get_screenshot_as_png(), name=screenshotName,
                          attachment_type=allure.attachment_type.PNG)
            driver.get_screenshot_as_file("/Users/yuchienhuang/Desktop/Swag_labs/Funtionality_Reports/login_out/login_out_screenhsots" + screenshotName + ".png")

            raise
        except:
            print("Check useraname")
            raise


    #@pytest.mark.skip
    #accepted/invalid:username=standard_user, pw=""
    def test_username_invalid_password(self):
        try:
            driver = self.driver
            driver.get(var_info.url_login)
            login = LoginPage(driver)
            login.enter_login_info(var_info.username_s, var_info.password_b)
            print(driver.current_url)
            error_message = login.failed_message()
            logo_title = login.title_after_login()
            print(error_message.text)

            assert error_message.text == "Epic sadface: Password is required"
            assert driver.current_url == "https://www.saucedemo.com/"
            assert logo_title == False


        except AssertionError as error:
            print("AssertionError occurred")
            print(error)
            cur_time = datetime.datetime.now().strftime("%H-%M-%S_%d_%m_%Y")
            testName = utils.whoami()
            screenshotName = testName + "_" + cur_time
            #screenshotName = "screenshot" + cur_time

            allure.attach(driver.get_screenshot_as_png(), name=screenshotName,
                          attachment_type=allure.attachment_type.PNG)
            driver.get_screenshot_as_file("/Users/yuchienhuang/Desktop/Swag_labs/Funtionality_Reports/login_out/login_out_screenhsots" + screenshotName + ".png")

            raise
        except:
            print("Check password, it might be blank")
            raise

    # @pytest.mark.skip
    # accepted/invalid:username=standard_user, pw='fghgf435@' =>random pw
    def test_username_random_password(self):
        try:
            driver = self.driver
            driver.get(var_info.url_login)
            login = LoginPage(driver)
            login.enter_login_info(var_info.username_s, var_info.password_random)
            print(driver.current_url)
            error_message = login.failed_message()
            logo_title = login.title_after_login()
            print(error_message.text)

            assert error_message.text == "Epic sadface: Username and password do not match any user in this service"
            assert driver.current_url == "https://www.saucedemo.com/"
            assert logo_title == False


        except AssertionError as error:
            print("AssertionError occurred")
            print(error)
            cur_time = datetime.datetime.now().strftime("%H-%M-%S_%d_%m_%Y")
            testName = utils.whoami()
            screenshotName = testName + "_" + cur_time
            #screenshotName = "screenshot" + cur_time

            allure.attach(driver.get_screenshot_as_png(), name=screenshotName,
                          attachment_type=allure.attachment_type.PNG)
            driver.get_screenshot_as_file("/Users/yuchienhuang/Desktop/Swag_labs/Funtionality_Reports/login_out/login_out_screenhsots" + screenshotName + ".png")

            raise
        except:
            print("Sth wrong with password")
            raise
    #
    # @pytest.mark.skip
    # #unaccepted:username=" ", pw= 'secret_sauce'
    def test_blank_username_password(self):
        try:
            driver = self.driver
            driver.get(var_info.url_login)
            login = LoginPage(driver)
            login.enter_login_info(var_info.username_b, var_info.password_s)
            print(driver.current_url)
            error_message = login.failed_message()
            logo_title = login.title_after_login()
            print(error_message.text)

            assert error_message.text == "Epic sadface: Username is required"
            assert driver.current_url == "https://www.saucedemo.com/"
            assert logo_title == False


        except AssertionError as error:
            print("AssertionError occurred")
            print(error)
            cur_time = datetime.datetime.now().strftime("%H-%M-%S_%d_%m_%Y")
            testName = utils.whoami()
            screenshotName = testName + "_" + cur_time
            #screenshotName = "screenshot" + cur_time

            allure.attach(driver.get_screenshot_as_png(), name=screenshotName,
                          attachment_type=allure.attachment_type.PNG)
            driver.get_screenshot_as_file("/Users/yuchienhuang/Desktop/Swag_labs/Funtionality_Reports/login_out/login_out_screenhsots" + screenshotName + ".png")

            raise
        except:
            print("Don't leave account")
            raise
    #
    # @pytest.mark.skip
    # # unaccepted:username="", pw= ""
    def test_both_blank_username_password(self):
        try:
            driver = self.driver
            driver.get(var_info.url_login)
            login = LoginPage(driver)
            login.enter_login_info(var_info.username_b, var_info.password_b)
            print(driver.current_url)
            error_message = login.failed_message()
            logo_title = login.title_after_login()
            print(error_message.text)

            assert error_message.text == "Epic sadface: Username is required"
            assert driver.current_url == "https://www.saucedemo.com/"
            assert logo_title == False

        except AssertionError as error:
            print("AssertionError occurred")
            print(error)
            cur_time = datetime.datetime.now().strftime("%H-%M-%S_%d_%m_%Y")
            testName = utils.whoami()
            screenshotName = testName + "_" + cur_time
            #screenshotName = "screenshot" + cur_time

            allure.attach(driver.get_screenshot_as_png(), name=screenshotName,
                          attachment_type=allure.attachment_type.PNG)
            driver.get_screenshot_as_file("/Users/yuchienhuang/Desktop/Swag_labs/Funtionality_Reports/login_out/login_out_screenhsots" + screenshotName + ".png")

            raise
        except:
            print("Dont leave account and user blank")
            raise
    #
    # @pytest.mark.skip
    # # unaccepted:username="345trewet", pw= "fghgf435@"  =>random
    def test_both_random_username_password(self):
        try:
            driver = self.driver
            driver.get(var_info.url_login)
            login = LoginPage(driver)
            login.enter_login_info(var_info.username_random, var_info.password_random)
            print(driver.current_url)
            error_message = login.failed_message()
            logo_title = login.title_after_login()
            print(error_message.text)

            assert error_message.text == "Epic sadface: Username and password do not match any user in this service"
            assert driver.current_url == "https://www.saucedemo.com/"
            assert logo_title == False

        except AssertionError as error:
            print("AssertionError occurred")
            print(error)
            cur_time = datetime.datetime.now().strftime("%H-%M-%S_%d_%m_%Y")
            testName = utils.whoami()
            screenshotName = testName + "_" + cur_time
            #screenshotName = "screenshot" + cur_time

            allure.attach(driver.get_screenshot_as_png(), name=screenshotName,
                          attachment_type=allure.attachment_type.PNG)
            driver.get_screenshot_as_file("/Users/yuchienhuang/Desktop/Swag_labs/Funtionality_Reports/login_out/login_out_screenhsots" + screenshotName + ".png")

            raise
        except:
            print("Both username and password need to be checked")
            raise










