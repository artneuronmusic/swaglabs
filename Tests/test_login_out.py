import pytest
import os.path
import sys
import time


sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from Info import var_info
from Pages.login_page import LoginPage
from Pages.product_page import ProductPage

@pytest.mark.usefixtures("test_setup")
class TestLoginOut():


    #accepted:username=standard_user, pw=secret_sauce
    def test_username_password_1(self):
        driver = self.driver
        driver.get(var_info.url_login)
        login = LoginPage(driver)
        login.enter_login_info(var_info.username_s, var_info.password_s)

        logo_title = login.title_after_login()
        product = ProductPage(driver)
        product.menu_items()
        assert driver.current_url == "https://www.saucedemo.com/inventory.html"
        assert logo_title == True
        product.pick_item_from_menu("Logout")

        assert driver.current_url == "https://www.saucedemo.com/index.html"


    # accepted:username=problem_user, pw=secret_sauce
    def test_username_password_2(self):
        driver = self.driver
        driver.get(var_info.url_login)
        login = LoginPage(driver)
        login.enter_login_info(var_info.username_p, var_info.password_s)

        logo_title = login.title_after_login()
        product = ProductPage(driver)
        product.menu_items()
        assert driver.current_url == "https://www.saucedemo.com/inventory.html"
        assert logo_title == True
        product.pick_item_from_menu("Logout")

        assert driver.current_url == "https://www.saucedemo.com/index.html"


    # accepted:username=performance_glitch_user, pw=secret_sauce
    def test_username_password_3(self):
        driver = self.driver
        driver.get(var_info.url_login)
        login = LoginPage(driver)
        login.enter_login_info(var_info.username_pe, var_info.password_s)
        logo_title = login.title_after_login()
        product = ProductPage(driver)
        product.menu_items()
        assert driver.current_url == "https://www.saucedemo.com/inventory.html"
        assert logo_title == True
        product.pick_item_from_menu("Logout")

        assert driver.current_url == "https://www.saucedemo.com/index.html"

    @pytest.mark.skip
    # accepted:username=locked_user, pw=secret_sauce
    def test_username_password_4(self):
        driver = self.driver
        driver.get(var_info.url_login)
        login = LoginPage(driver)
        login.enter_login_info(var_info.username_l, var_info.password_s)
        print(driver.current_url)
        error_message = login.failed_message()
        logo_title = login.title_after_login()
        print(error_message.text)

        assert driver.current_url == "https://www.saucedemo.com/inventory.html"
        assert logo_title == False
        assert error_message.text == "Epic sadface: Username and password do not match any user in this service"
        product = ProductPage(driver)
        product.pick_item_from_menu("Logout")
        assert driver.current_url == "https://www.saucedemo.com/index.html"


    @pytest.mark.skip
    #accepted/invalid:username=standard_user, pw=""
    def test_username_password_5(self):
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

    @pytest.mark.skip
    # accepted/invalid:username=standard_user, pw='fghgf435@' =>random pw
    def test_username_password_6(self):
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

    @pytest.mark.skip
    #unaccepted:username=" ", pw= 'secret_sauce'
    def test_username_password_7(self):
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

    @pytest.mark.skip
    # unaccepted:username="", pw= ""
    def test_username_password_8(self):
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

    @pytest.mark.skip
    # unaccepted:username="345trewet", pw= "fghgf435@"  =>random
    def test_username_password_9(self):
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










