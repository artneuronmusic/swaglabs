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
from Pages.product_individual_page import DetailsPage
from Pages.general_page import GeneralPage
from Utils import utils

#The problem for this page is that the add to cart button needed to become ADD TO CART after reset



@pytest.mark.usefixtures("driver")
class TestImgsDisplay():

    #IMGS ALL DISPLAY?
    #accepted:username=standard_user, pw=secret_sauce

        def test_imgs_exist(self):
            try:
                driver = self.driver
                # get url from var_info
                driver.get(var_info.url_login)

                # take driver into LoginPage
                login = LoginPage(driver)

                # get account and password
                login.enter_login_info(var_info.username_s, var_info.password_s)
                product = ProductPage(driver)
                logo = product.product_logo()
                imgs_display = product.products_img()

                assert imgs_display == True
                assert logo.is_displayed()

            except AssertionError as error:
                print("AssertionError occurred")
                print(error)
                cur_time = datetime.datetime.now().strftime("%H-%M-%S_%d_%m_%Y")
                testName = utils.whoami()
                screenshotName = testName + "_" + cur_time

                allure.attach(self.driver.get_screenshot_as_png(), name=screenshotName,
                              attachment_type=allure.attachment_type.PNG)
                self.driver.get_screenshot_as_file(
                    "Funtionality_Reports/product_page/product_page_screentshots/product_page_valid_user/" + screenshotName + ".png")

                raise

        #EACH IMG WORKS
        @pytest.mark.parametrize('num', [1, 2, 3, 4, 5, 6])
        def test_img1_in_default_order(self, num):
            try:
                driver = self.driver
                driver.get(var_info.url_login)
                login = LoginPage(driver)
                login.enter_login_info(var_info.username_s, var_info.password_s)
                product = ProductPage(driver)
                img = product.specific_product_img(num)
                assert img == True

            except AssertionError as error:
                print("AssertionError occurred")
                print(error)
                cur_time = datetime.datetime.now().strftime("%H-%M-%S_%d_%m_%Y")
                testName = utils.whoami()
                screenshotName = testName + "_" + cur_time

                allure.attach(self.driver.get_screenshot_as_png(), name=screenshotName,
                              attachment_type=allure.attachment_type.PNG)
                self.driver.get_screenshot_as_file(
                    "Funtionality_Reports/product_page/product_page_screentshots/product_page_valid_user/" + screenshotName + ".png")

                raise


@pytest.mark.usefixtures("driver")
class TestProductsDisplay():

    #PRODUCT LABELS DISPLAY
    def test_product_labels(self):
        try:
            driver = self.driver
            driver.get(var_info.url_login)
            login = LoginPage(driver)
            login.enter_login_info(var_info.username_s, var_info.password_s)
            product = ProductPage(driver)
            names_list = product.product_labels()

            assert isinstance(names_list, list)


        except AssertionError as error:
            print("AssertionError occurred")
            print(error)
            cur_time = datetime.datetime.now().strftime("%H-%M-%S_%d_%m_%Y")
            testName = utils.whoami()
            screenshotName = testName + "_" + cur_time

            allure.attach(self.driver.get_screenshot_as_png(), name=screenshotName,
                          attachment_type=allure.attachment_type.PNG)
            self.driver.get_screenshot_as_file(
                "Funtionality_Reports/product_page/product_page_screentshots/product_page_valid_user/" + screenshotName + ".png")

            raise


    #PRODUCTS PRICE DISPLAY
    def test_products_price(self):

        try:
            driver = self.driver
            driver.get(var_info.url_login)
            login = LoginPage(driver)
            login.enter_login_info(var_info.username_s, var_info.password_s)
            product = ProductPage(driver)
            price_list = product.products_price()

            assert isinstance(price_list, list)


        except AssertionError as error:
            print("AssertionError occurred")
            print(error)
            cur_time = datetime.datetime.now().strftime("%H-%M-%S_%d_%m_%Y")
            testName = utils.whoami()
            screenshotName = testName + "_" + cur_time

            allure.attach(self.driver.get_screenshot_as_png(), name=screenshotName,
                          attachment_type=allure.attachment_type.PNG)
            self.driver.get_screenshot_as_file(
                "Funtionality_Reports/product_page/product_page_screentshots/product_page_valid_user/" + screenshotName + ".png")

            raise


    #DESCIPTIONS DISPLAY
    def test_products_description(self):

        try:
            driver = self.driver
            driver.get(var_info.url_login)
            login = LoginPage(driver)
            login.enter_login_info(var_info.username_s, var_info.password_s)
            product = ProductPage(driver)
            description_list = product.products_description()

            assert isinstance(description_list, list)


        except AssertionError as error:
            print("AssertionError occurred")
            print(error)
            cur_time = datetime.datetime.now().strftime("%H-%M-%S_%d_%m_%Y")
            testName = utils.whoami()
            screenshotName = testName + "_" + cur_time

            allure.attach(self.driver.get_screenshot_as_png(), name=screenshotName,
                          attachment_type=allure.attachment_type.PNG)
            self.driver.get_screenshot_as_file(
                "Funtionality_Reports/product_page/product_page_screentshots/product_page_valid_user/" + screenshotName + ".png")

            raise


    #ADD TO CART LABELS DISPLAY
    def test_products_add_to_cart_label(self):
        try:
            driver = self.driver
            driver.get(var_info.url_login)
            login = LoginPage(driver)
            login.enter_login_info(var_info.username_s, var_info.password_s)
            product = ProductPage(driver)
            add_to_cart_label = product.products_add_to_cart_label()

            assert add_to_cart_label == True


        except AssertionError as error:
            print("AssertionError occurred")
            print(error)
            cur_time = datetime.datetime.now().strftime("%H-%M-%S_%d_%m_%Y")
            testName = utils.whoami()
            screenshotName = testName + "_" + cur_time

            allure.attach(self.driver.get_screenshot_as_png(), name=screenshotName,
                          attachment_type=allure.attachment_type.PNG)
            self.driver.get_screenshot_as_file(
                "Funtionality_Reports/product_page/product_page_screentshots/product_page_valid_user/" + screenshotName + ".png")

            raise


@pytest.mark.usefixtures("driver")
class TestDisplayOrder():
    # check the default display for products(from A to Z)
    #@pytest.mark.skip
    def test_display_default_product_order(self):
        try:

            driver = self.driver
            # get url from var_info
            driver.get(var_info.url_login)

            # take driver into LoginPage
            login = LoginPage(driver)

            # get account and password
            login.enter_login_info(var_info.username_s, var_info.password_s)

            driver.get(var_info.url_product)
            product = ProductPage(driver)
            order = product.default_name_order()
            product_title1 = product.product_label(1)
            product_price1 = product.product_price(1)
            product_description1 = product.product_description(1)

            product_title3 = product.product_label(3)
            product_price3 = product.product_price(3)
            product_description3 = product.product_description(3)

            product_title6 = product.product_label(5)
            product_price6 = product.product_price(5)
            product_description6 = product.product_description(5)

            assert order.text == "Name (A to Z)"
            assert product_title1.text == "Sauce Labs Backpack"
            assert product_price1.text == "$29.99"
            assert product_description1.text == var_info.desc_a_to_z[0]
            assert product_title3.text == "Sauce Labs Bolt T-Shirt"
            assert product_price3.text == "$15.99"
            assert product_description3.text == var_info.desc_a_to_z[2]
            assert product_title6.text == "Sauce Labs Onesie"
            assert product_price6.text == "$7.99"
            assert product_description6.text == var_info.desc_a_to_z[4]



        except AssertionError as error:
            print("AssertionError occurred")
            print(error)
            cur_time = datetime.datetime.now().strftime("%H-%M-%S_%d_%m_%Y")
            testName = utils.whoami()
            screenshotName = testName + "_" + cur_time

            allure.attach(self.driver.get_screenshot_as_png(), name=screenshotName,
                          attachment_type=allure.attachment_type.PNG)
            self.driver.get_screenshot_as_file(
                "Funtionality_Reports/product_page/product_page_screentshots/product_page_valid_user/" + screenshotName + ".png")

            raise




    # check product display from Z to A
    #@pytest.mark.skip
    def test_display_name_a_to_z(self):
        try:

            driver = self.driver
            driver.get(var_info.url_login)
            login = LoginPage(driver)
            login.enter_login_info(var_info.username_s, var_info.password_s)
            product = ProductPage(driver)
            order = product.pick_display_order("Name (Z to A)")
            product_title1 = product.product_label(1)
            product_price1 = product.product_price(1)
            product_description1 = product.product_description(1)

            product_title3 = product.product_label(3)
            product_price3 = product.product_price(3)
            product_description3 = product.product_description(3)

            product_title6 = product.product_label(5)
            product_price6 = product.product_price(5)
            product_description6 = product.product_description(5)


            assert product_title1.text == "Test.allTheThings() T-Shirt (Red)"
            assert product_price1.text == "$15.99"
            assert product_description1.text == var_info.desc_z_to_a[0]
            assert product_title3.text == "Sauce Labs Fleece Jacket"
            assert product_price3.text == "$49.99"
            assert product_description3.text == var_info.desc_z_to_a[2]
            assert product_title6.text == "Sauce Labs Bike Light"
            assert product_price6.text == "$9.99"
            assert product_description6.text == var_info.desc_z_to_a[4]



        except AssertionError as error:
            print("AssertionError occurred")
            print(error)
            cur_time = datetime.datetime.now().strftime("%H-%M-%S_%d_%m_%Y")
            testName = utils.whoami()
            screenshotName = testName + "_" + cur_time

            allure.attach(self.driver.get_screenshot_as_png(), name=screenshotName,
                          attachment_type=allure.attachment_type.PNG)
            self.driver.get_screenshot_as_file(
                "Funtionality_Reports/product_page/product_page_screentshots/product_page_valid_user/" + screenshotName + ".png")

            raise


    # check product display from Z to A
    #@pytest.mark.skip
    def test_display_price_low_to_high(self):
        try:
            driver = self.driver
            driver.get(var_info.url_login)
            login = LoginPage(driver)
            login.enter_login_info(var_info.username_s, var_info.password_s)
            product = ProductPage(driver)
            product.pick_display_order(3)
            product_title1 = product.product_label(1)
            product_price1 = product.product_price(1)
            product_description1 = product.product_description(1)

            product_title3 = product.product_label(3)
            product_price3 = product.product_price(3)
            product_description3 = product.product_description(3)

            product_title6 = product.product_label(5)
            product_price6 = product.product_price(5)
            product_description6 = product.product_description(5)


            assert product_title1.text == "Sauce Labs Onesie"
            assert product_price1.text == "$7.99"
            assert product_description1.text == var_info.desc_low_to_high[0]
            assert product_title3.text == "Sauce Labs Bolt T-Shirt"
            assert product_price3.text == "$15.99"
            assert product_description3.text == var_info.desc_low_to_high[2]
            assert product_title6.text == "Sauce Labs Backpack"
            assert product_price6.text == "$29.99"
            assert product_description6.text == var_info.desc_low_to_high[4]


        except AssertionError as error:
            print("AssertionError occurred")
            print(error)
            cur_time = datetime.datetime.now().strftime("%H-%M-%S_%d_%m_%Y")
            testName = utils.whoami()
            screenshotName = testName + "_" + cur_time

            allure.attach(self.driver.get_screenshot_as_png(), name=screenshotName,
                          attachment_type=allure.attachment_type.PNG)
            self.driver.get_screenshot_as_file(
                "Funtionality_Reports/product_page/product_page_screentshots/product_page_valid_user/" + screenshotName + ".png")

            raise



    def test_display_price_high_to_low(self):
        try:
            driver = self.driver
            driver.get(var_info.url_login)
            login = LoginPage(driver)
            login.enter_login_info(var_info.username_s, var_info.password_s)
            product = ProductPage(driver)
            product.pick_display_order(4)
            product_title1 = product.product_label(1)
            product_price1 = product.product_price(1)
            product_description1 = product.product_description(1)

            product_title3 = product.product_label(3)
            product_price3 = product.product_price(3)
            product_description3 = product.product_description(3)

            product_title6 = product.product_label(5)
            product_price6 = product.product_price(5)
            product_description6 = product.product_description(5)


            assert product_title1.text == "Sauce Labs Fleece Jacket"
            assert product_price1.text == "$49.99"
            assert product_description1.text == var_info.desc_high_to_low[0]
            assert product_title3.text == "Test.allTheThings() T-Shirt (Red)"
            assert product_price3.text == "$15.99"
            assert product_description3.text == var_info.desc_high_to_low[2]
            assert product_title6.text == "Sauce Labs Bike Light"
            assert product_price6.text == "$9.99"
            assert product_description6.text == var_info.desc_high_to_low[4]


        except AssertionError as error:
            print("AssertionError occurred")
            print(error)
            cur_time = datetime.datetime.now().strftime("%H-%M-%S_%d_%m_%Y")
            testName = utils.whoami()
            screenshotName = testName + "_" + cur_time

            allure.attach(self.driver.get_screenshot_as_png(), name=screenshotName,
                          attachment_type=allure.attachment_type.PNG)
            self.driver.get_screenshot_as_file(
                "Funtionality_Reports/product_page/product_page_screentshots/product_page_valid_user/" + screenshotName + ".png")

            raise



@pytest.mark.usefixtures("driver")
class ProductDetail():

    def test_default_display_click_product_label1(self):
        try:
            driver = self.driver
            driver.get(var_info.url_login)
            login = LoginPage(driver)
            login.enter_login_info(var_info.username_s, var_info.password_s)
            product = ProductPage(driver)
            p_title = product.product_label(1)
            p_price = product.product_price(1)
            p_description = product.product_description()
            price = p_price.text
            p_description = p_description.text
            title = p_title.text
            title.click()
            details = DetailsPage(driver)
            title_label = details.check_single_label()
            price_label = details.check_single_price()
            description_label = details.check_single_description()
            img = details.check_single_img()

            assert price == price_label.text
            assert p_description == description_label.text
            assert title == title_label.text
            assert img.id_displayed()


        except AssertionError as error:
            print("AssertionError occurred")
            print(error)
            cur_time = datetime.datetime.now().strftime("%H-%M-%S_%d_%m_%Y")
            testName = utils.whoami()
            screenshotName = testName + "_" + cur_time

            allure.attach(self.driver.get_screenshot_as_png(), name=screenshotName,
                          attachment_type=allure.attachment_type.PNG)
            self.driver.get_screenshot_as_file(
                "Funtionality_Reports/product_page/product_page_screentshots/product_page_valid_user/" + screenshotName + ".png")

            raise


    def test_default_display_click_product_label3(self):
        try:
            driver = self.driver
            driver.get(var_info.url_login)
            login = LoginPage(driver)
            login.enter_login_info(var_info.username_s, var_info.password_s)
            product = ProductPage(driver)
            p_title = product.product_label(3)
            p_price = product.product_price(3)
            p_description = product.product_description()
            price = p_price.text
            p_description = p_description.text
            title = p_title.text
            title.click()
            details = DetailsPage(driver)
            title_label = details.check_single_label()
            price_label = details.check_single_price()
            description_label = details.check_single_description()
            img = details.check_single_img()

            assert price == price_label.text
            assert p_description == description_label.text
            assert title == title_label.text
            assert img.id_displayed()


        except AssertionError as error:
            print("AssertionError occurred")
            print(error)
            cur_time = datetime.datetime.now().strftime("%H-%M-%S_%d_%m_%Y")
            testName = utils.whoami()
            screenshotName = testName + "_" + cur_time

            allure.attach(self.driver.get_screenshot_as_png(), name=screenshotName,
                          attachment_type=allure.attachment_type.PNG)
            self.driver.get_screenshot_as_file(
                "Funtionality_Reports/product_page/product_page_screentshots/product_page_valid_user/" + screenshotName + ".png")

            raise


    def test_default_display_click_product_label5(self):
        try:
            driver = self.driver
            driver.get(var_info.url_login)
            login = LoginPage(driver)
            login.enter_login_info(var_info.username_s, var_info.password_s)
            product = ProductPage(driver)
            p_title = product.product_label(5)
            p_price = product.product_price(5)
            p_description = product.product_description()
            price = p_price.text
            p_description = p_description.text
            title = p_title.text
            title.click()
            details = DetailsPage(driver)
            title_label = details.check_single_label()
            price_label = details.check_single_price()
            description_label = details.check_single_description()
            img = details.check_single_img()

            assert price == price_label.text
            assert p_description == description_label.text
            assert title == title_label.text
            assert img.id_displayed()


        except AssertionError as error:
            print("AssertionError occurred")
            print(error)
            cur_time = datetime.datetime.now().strftime("%H-%M-%S_%d_%m_%Y")
            testName = utils.whoami()
            screenshotName = testName + "_" + cur_time

            allure.attach(self.driver.get_screenshot_as_png(), name=screenshotName,
                          attachment_type=allure.attachment_type.PNG)
            self.driver.get_screenshot_as_file(
                "Funtionality_Reports/product_page/product_page_screentshots/product_page_valid_user/" + screenshotName + ".png")

            raise



@pytest.mark.usefixtures("driver")
class TestAddDisplay():

    #ALL CART LABELS CAN BE CLICKABLE, CLICK=>REMOVE, QUANTITY
    #@pytest.mark.parametrize('info', [1, 2, 3, 4, 5, 6])
    def test_products_add_to_cart_clickable(self):
        try:
            driver = self.driver
            driver.refresh()
            driver.get(var_info.url_login)
            login = LoginPage(driver)
            login.enter_login_info(var_info.username_s, var_info.password_s)
            product = ProductPage(driver)
            for i in range(1, 7):
                add_to_cart = product.product_add_to_cart(i)
                add_to_cart.click()
            general = GeneralPage(driver)
            qty = general.cart_qty()

            a1 = product.product_add_to_cart(1)
            a2 = product.product_add_to_cart(2)
            a3 = product.product_add_to_cart(3)

            assert qty.is_displayed() == True
            assert qty.text == "6"
            assert a1.text == "REMOVE"
            assert a2.text == "REMOVE"
            assert a3.text == "REMOVE"


        except AssertionError as error:
            print("AssertionError occurred")
            print(error)
            cur_time = datetime.datetime.now().strftime("%H-%M-%S_%d_%m_%Y")
            testName = utils.whoami()
            screenshotName = testName + "_" + cur_time

            allure.attach(self.driver.get_screenshot_as_png(), name=screenshotName,
                          attachment_type=allure.attachment_type.PNG)
            self.driver.get_screenshot_as_file(
                "Funtionality_Reports/product_page/product_page_screentshots/product_page_valid_user/" + screenshotName + ".png")

            raise


@pytest.mark.usefixtures("driver")
class TestAddDisplay():

    # ALL CART LABELS CAN BE MULTIPLY CLICK, CLICK=>ADD TO CART, QUANTITY =>0
    # @pytest.mark.parametrize('info', [1, 2, 3, 4, 5, 6])
    def test_products_add_to_cart_clickable_multiple_times(self):

        try:
            driver = self.driver
            #driver.refresh()
            driver.get(var_info.url_login)
            login = LoginPage(driver)
            login.enter_login_info(var_info.username_s, var_info.password_s)
            product = ProductPage(driver)
            for i in range(1, 7):
                add_to_cart = product.product_add_to_cart(i)
                add_to_cart.click()

            a1 = product.product_add_to_cart(1)
            a1.click()
            a2 = product.product_add_to_cart(2)
            a2.click()
            a3 = product.product_add_to_cart(3)
            a3.click()
            a4 = product.product_add_to_cart(4)
            a4.click()
            a5 = product.product_add_to_cart(5)
            a5.click()
            a6 = product.product_add_to_cart(6)
            a6.click()

            general = GeneralPage(driver)
            qty = general.cart_qty()

            assert qty == None
            assert a4.text == "ADD TO CART"
            assert a5.text == "ADD TO CART"
            assert a6.text == "ADD TO CART"


        except AssertionError as error:
            print("AssertionError occurred")
            print(error)
            cur_time = datetime.datetime.now().strftime("%H-%M-%S_%d_%m_%Y")
            testName = utils.whoami()
            screenshotName = testName + "_" + cur_time

            allure.attach(self.driver.get_screenshot_as_png(), name=screenshotName,
                          attachment_type=allure.attachment_type.PNG)
            self.driver.get_screenshot_as_file(
                "/Users/yuchienhuang/Desktop/Swag_labs/Funtionality_Reports/product_page/product_page_screentshots/product_page_valid_user/" + screenshotName + ".png")

            raise



@pytest.mark.usefixtures("driver")
class TestMainItems():

    #check logout
    def test_a_logout_product_page(self):
        try:

            driver = self.driver
            # get url from var_info
            driver.get(var_info.url_login)

            # take driver into LoginPage
            login = LoginPage(driver)

            # get account and password
            login.enter_login_info(var_info.username_s, var_info.password_s)
            product = ProductPage(driver)
            general = GeneralPage(driver)
            product.product_logo()
            general.drop_down_menu()
            general.pick_item_from_menu("Logout")

            assert driver.current_url == "https://www.saucedemo.com/index.html"
            assert driver.current_url != "https://www.saucedemo.com/"


        except AssertionError as error:
            print("AssertionError occurred")
            print(error)
            cur_time = datetime.datetime.now().strftime("%H-%M-%S_%d_%m_%Y")
            testName = utils.whoami()
            screenshotName = testName + "_" + cur_time

            allure.attach(self.driver.get_screenshot_as_png(), name=screenshotName,
                          attachment_type=allure.attachment_type.PNG)
            self.driver.get_screenshot_as_file(
                "/Users/yuchienhuang/Desktop/Swag_labs/Funtionality_Reports/product_page/product_page_screentshots/product_page_valid_user/" + screenshotName + ".png")

            raise

    #check about
    def test_about_product_page(self):
        try:

            driver = self.driver
            # get url from var_info
            driver.get(var_info.url_login)

            # take driver into LoginPage
            login = LoginPage(driver)

            # get account and password
            login.enter_login_info(var_info.username_s, var_info.password_s)
            product = ProductPage(driver)
            general = GeneralPage(driver)
            product.product_logo()
            general.drop_down_menu()
            general.pick_item_from_menu("About")

            assert driver.current_url == "https://saucelabs.com/"

        except AssertionError as error:
            print("AssertionError occurred")
            print(error)
            cur_time = datetime.datetime.now().strftime("%H-%M-%S_%d_%m_%Y")
            testName = utils.whoami()
            screenshotName = testName + "_" + cur_time

            allure.attach(self.driver.get_screenshot_as_png(), name=screenshotName,
                          attachment_type=allure.attachment_type.PNG)
            self.driver.get_screenshot_as_file(
                "/Users/yuchienhuang/Desktop/Swag_labs/Funtionality_Reports/product_page/product_page_screentshots/product_page_valid_user/" + screenshotName + ".png")

            raise


    #check "all items" in product page
    def test_all_items_product_page(self):
        try:
            driver = self.driver
            driver.get(var_info.url_login)
            login = LoginPage(driver)
            login.enter_login_info(var_info.username_s, var_info.password_s)
            product = ProductPage(driver)
            general = GeneralPage(driver)
            product.product_logo()
            product.click_add_to_cart(1)
            product.click_add_to_cart(6)
            product.click_add_to_cart(3)
            product.click_add_to_cart(6)
            general.drop_down_menu()
            general.pick_item_from_menu("All Items")
            qty = general.cart_qty()

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
            self.driver.get_screenshot_as_file(
                "/Users/yuchienhuang/Desktop/Swag_labs/Funtionality_Reports/product_page/product_page_screentshots/product_page_valid_user/" + screenshotName + ".png")

            raise


    #check "Reset App State" in product_page, the whole label should be remove
    def test_reset_app_product_page(self):
        try:
            driver = self.driver
            driver.get(var_info.url_login)
            login = LoginPage(driver)
            login.enter_login_info(var_info.username_s, var_info.password_s)
            product = ProductPage(driver)
            general = GeneralPage(driver)
            product.click_add_to_cart(2)
            product.click_add_to_cart(4)
            general.drop_down_menu()
            general.pick_item_from_menu("Reset App State")
            add_to_cart2 = product.add_to_cart_label(2)
            add_to_cart4 = product.add_to_cart_label(4)
            product.add_to_cart_label(4)
            general.delete_button_menu()
            cart_qty = general.cart_qty()

            assert cart_qty == None
            assert add_to_cart2.text == "ADD TO CART"
            assert add_to_cart4.text == "ADD TO CART"
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
                "/Users/yuchienhuang/Desktop/Swag_labs/Funtionality_Reports/product_page/product_page_screentshots/product_page_valid_user/" + screenshotName + ".png")

            raise


    #check "Reset App State" in individual_page
    def test_reset_app_individual_page(self):
        try:
            driver = self.driver
            driver.get(var_info.url_login)
            login = LoginPage(driver)
            login.enter_login_info(var_info.username_s, var_info.password_s)
            product = ProductPage(driver)
            product.click_add_to_cart(3)
            product.click_product_label(3)
            general = GeneralPage(driver)
            general.drop_down_menu()
            general.pick_item_from_menu("Reset App State")
            general.delete_button_menu()
            details = DetailsPage(driver)
            add_to_cart_product = details.check_single_add_to_cart()
            cart_qty = general.cart_qty()


            assert add_to_cart_product.text == "ADD TO CART"
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
                "/Users/yuchienhuang/Desktop/Swag_labs/Funtionality_Reports/product_page/product_page_screentshots/product_page_valid_user/" + screenshotName + ".png")

            raise

    ##check "all items" in individual page
    def test_all_items_details_page(self):
        try:
            driver = self.driver
            driver.get(var_info.url_login)
            login = LoginPage(driver)
            login.enter_login_info(var_info.username_s, var_info.password_s)
            product = ProductPage(driver)
            product.click_product_label(1) #click label 1
            details = DetailsPage(driver)
            add_to_cart = details.check_single_add_to_cart() #click add_to_cart
            add_to_cart.click()
            general = GeneralPage(driver)
            general.drop_down_menu()
            general.pick_item_from_menu("Reset App State")
            general.delete_button_menu()
            add_to_cart_product = details.check_single_add_to_cart()

            #cart_qty = general.cart_qty()

            assert driver.current_url != "https://www.saucedemo.com/inventory.html"
            assert add_to_cart_product.text == "ADD TO CART"
                #assert cart_qty == None


        except AssertionError as error:
            print("AssertionError occurred")
            print(error)
            cur_time = datetime.datetime.now().strftime("%H-%M-%S_%d_%m_%Y")
            testName = utils.whoami()
            screenshotName = testName + "_" + cur_time

            allure.attach(self.driver.get_screenshot_as_png(), name=screenshotName,
                          attachment_type=allure.attachment_type.PNG)
            self.driver.get_screenshot_as_file(
                "/Users/yuchienhuang/Desktop/Swag_labs/Funtionality_Reports/product_page/product_page_screentshots/product_page_valid_user/" + screenshotName + ".png")

            raise

@pytest.mark.usefixtures("driver")
class TestCartCheckout():

    def test_cart_checkout(self):
        try:
            driver = self.driver
            driver.refresh()
            driver.get(var_info.url_login)
            login = LoginPage(driver)
            login.enter_login_info(var_info.username_p, var_info.password_s)
            product = ProductPage(driver)
            p_label1 = product.add_to_cart_label(1)
            p_label1.click()

            p_label2 = product.add_to_cart_label()
            p_label2.click()
            p_label3 = product.add_to_cart_label(3)
            p_label3.click()
            p_label4 = product.add_to_cart_label(4)
            p_label4.click()
            p_label5 = product.add_to_cart_label(5)
            p_label5.click()
            product.click_product_label(6)
            details = DetailsPage(driver)
            details.check_single_add_to_cart().click()

            general = GeneralPage(driver)
            general.cart_sign().click()
            cart_qty = general.cart_qty()

            assert driver.current_url == "https://www.saucedemo.com/cart.html"
            assert p_label1.text == "Remove"
            assert p_label3.text == "Remove"
            assert p_label4.text == "Remove"
            assert p_label5.text == "Remove"
            assert cart_qty.text == "6"


        except AssertionError as error:
            print("AssertionError occurred")
            print(error)
            cur_time = datetime.datetime.now().strftime("%H-%M-%S_%d_%m_%Y")
            testName = utils.whoami()
            screenshotName = testName + "_" + cur_time

            allure.attach(self.driver.get_screenshot_as_png(), name=screenshotName,
                          attachment_type=allure.attachment_type.PNG)
            self.driver.get_screenshot_as_file(
                "/Users/yuchienhuang/Desktop/Swag_labs/Funtionality_Reports/product_page/product_page_screentshots/product_page_valid_user/" + screenshotName + ".png")

            raise


@pytest.mark.usefixtures("driver")
class TestProductDetails():

    def return_button_from_detail_page(self):
        try:
            driver = self.driver
            driver.get(var_info.url_login)
            login = LoginPage(driver)
            login.enter_login_info(var_info.username_s, var_info.password_s)
            product = ProductPage(driver)
            product.product_label(3).click()
            details = DetailsPage(driver)
            details.back_button().click()

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
                "/Users/yuchienhuang/Desktop/Swag_labs/Funtionality_Reports/product_page/product_page_screentshots/product_page_valid_user/" + screenshotName + ".png")

            raise


    def reset_from_detail_page(self):
        try:
            driver = self.driver
            driver.get(var_info.url_login)
            login = LoginPage(driver)
            login.enter_login_info(var_info.username_s, var_info.password_s)
            product = ProductPage(driver)
            product.product_label(4).click()
            details = DetailsPage(driver)
            add_to_cart_label = details.check_single_add_to_cart()
            add_to_cart_label.click()
            general = GeneralPage(driver)
            general.drop_down_menu()
            general.pick_item_from_menu("Reset App State")
            general.delete_menu().click()
            add_label = details.check_single_add_to_cart()
            cart_qty = general.cart_qty()

            assert cart_qty == None
            assert add_label.text == "ADD TO CART"


        except AssertionError as error:
            print("AssertionError occurred")
            print(error)
            cur_time = datetime.datetime.now().strftime("%H-%M-%S_%d_%m_%Y")
            testName = utils.whoami()
            screenshotName = testName + "_" + cur_time

            allure.attach(self.driver.get_screenshot_as_png(), name=screenshotName,
                          attachment_type=allure.attachment_type.PNG)
            self.driver.get_screenshot_as_file(
                "/Users/yuchienhuang/Desktop/Swag_labs/Funtionality_Reports/product_page/product_page_screentshots/product_page_valid_user/" + screenshotName + ".png")

            raise


    def reset_then_all_items_from_detail_page(self):
        try:
            driver = self.driver
            driver.get(var_info.url_login)
            login = LoginPage(driver)
            login.enter_login_info(var_info.username_s, var_info.password_s)
            product = ProductPage(driver)
            product.product_label(4).click()
            details = DetailsPage(driver)
            add_to_cart_label = details.check_single_add_to_cart()
            add_to_cart_label.click()
            general = GeneralPage(driver)
            general.drop_down_menu()
            general.pick_item_from_menu("Reset App State")
            time.sleep(2)
            general.pick_item_from_menu("All Items")
            general.delete_menu().click()
            cart_label = product.add_to_cart_label(4)
            cart_qty = general.cart_qty()


            assert driver.current_url == "https://www.saucedemo.com/inventory.html"
            assert cart_label.text == "ADD TO CART"
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
                "/Users/yuchienhuang/Desktop/Swag_labs/Funtionality_Reports/product_page/product_page_screentshots/product_page_valid_user/" + screenshotName + ".png")

            raise








