import pytest
import os.path
import sys
import time


sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from Info import var_info
from Pages.product_after_page import ProductAfterClickPage
from Pages.login_page import LoginPage
from Pages.product_page import ProductPage


@pytest.mark.usefixtures("test_setup")
class TestProductSecondPage1():

    # test back button
    #@pytest.mark.skip
    def test_click_img_check_return_button(self):
        driver = self.driver
        driver.get(var_info.url_product)
        product = ProductPage(driver)
        product.click_img(2)
        after_click = ProductAfterClickPage(driver)
        back = after_click.check_back_button()
        back.click()
        driver.delete_all_cookies()

        print(driver.current_url)
        assert driver.current_url == "https://www.saucedemo.com/inventory.html"

    # test cart sign by default
    #@pytest.mark.skip
    def test_click_img_check_return_button(self):
        driver = self.driver
        driver.get(var_info.url_product)
        product = ProductPage(driver)
        product.click_img(2)
        after_click = ProductAfterClickPage(driver)
        cart_sign = after_click.check_cart_sign()
        cart_qty = after_click.check_cart_qty()
        driver.implicitly_wait(5)

        assert cart_sign.is_displayed()
        assert cart_qty == None

    # check in with product name and test back button
    #@pytest.mark.skip
    def test_click_title_check_return_button(self):
        driver = self.driver
        driver.get(var_info.url_product)
        product = ProductPage(driver)
        product.click_product_label("Sauce Labs Bolt T-Shirt")
        after_click = ProductAfterClickPage(driver)
        back = after_click.check_back_button()
        back.click()

        print(driver.current_url)
        assert driver.current_url == "https://www.saucedemo.com/inventory.html"

    # test in add to cart clickable? displayed?
    #@pytest.mark.skip
    def test_add_to_cart(self):
        driver = self.driver
        driver.get(var_info.url_product)
        product = ProductPage(driver)
        product.click_product_label("Sauce Labs Onesie")

        after_click = ProductAfterClickPage(driver)
        add_to_cart = after_click.check_add_to_cart()
        add_to_cart.click()
        cart_sign = after_click.check_cart_sign()
        cart_qty = after_click.check_cart_qty()
        add_to_cart1 = after_click.check_add_to_cart()

        assert add_to_cart1.text == "REMOVE"
        assert cart_sign.is_displayed()
        assert cart_qty == "1"


@pytest.mark.usefixtures("test_setup")
class TestProductSecondPage2():
    #@pytest.mark.skip
    def test_add_items_back_and_forth(self):
        driver = self.driver
        driver.delete_all_cookies()
        driver.get(var_info.url_product)
        #driver.refresh()
        product = ProductPage(driver)
        product.click_product_label("Test.allTheThings() T-Shirt (Red)")
        after_click = ProductAfterClickPage(driver)
        driver.refresh()
        add_to_cart1 = after_click.check_add_to_cart()
        add_to_cart1.click()
        after_click.check_cart_qty()
        back = after_click.check_back_button()
        back.click()
        product.click_img(3)
        add_to_cart2 = after_click.check_add_to_cart()
        add_to_cart2.click()
        check_add_label = after_click.check_add_to_cart()
        cart_qty_total = after_click.check_cart_qty()

        assert cart_qty_total == "2"
        assert check_add_label.text == "REMOVE"


@pytest.mark.usefixtures("test_setup")
class TestProductSecondPage3():

    #@pytest.mark.skip
    def test_add_items_checkout(self):
        driver = self.driver
        driver.delete_all_cookies()
        driver.get(var_info.url_product)
        product = ProductPage(driver)
        #driver.refresh()
        product.click_product_label("Sauce Labs Bike Light")
        after_click = ProductAfterClickPage(driver)
        add_to_cart1 = after_click.check_add_to_cart()
        add_to_cart1.click()
        cart_qty = after_click.check_cart_qty()
        # cart_qty.click()
        cart_sign = after_click.check_cart_sign()
        cart_sign.click()

        assert cart_qty == "1"
        assert driver.current_url == "https://www.saucedemo.com/cart.html"







"""
    #test back button
    @pytest.mark.skip
    def test_click_img_check_return_button(self):
        driver = self.driver
        driver.get(var_info.url_product)
        product = ProductPage(driver)
        product.click_img(2)
        after_click = ProductAfterClickPage(driver)
        back = after_click.check_back_button()
        back.click()

        print(driver.current_url)
        assert driver.current_url == "https://www.saucedemo.com/inventory.html"


    #test cart sign by default
    @pytest.mark.skip
    def test_click_img_check_return_button(self):
        driver = self.driver
        driver.get(var_info.url_product)
        product = ProductPage(driver)
        product.click_img(2)
        after_click = ProductAfterClickPage(driver)
        cart_sign = after_click.check_cart_sign()
        cart_qty = after_click.check_cart_qty()

        assert cart_sign.is_displayed()
        assert cart_qty == None

    #check in with product name and test back button
    @pytest.mark.skip
    def test_click_title_check_return_button(self):
        driver = self.driver
        driver.get(var_info.url_product)
        product = ProductPage(driver)
        product.click_product_label("Sauce Labs Bolt T-Shirt")
        after_click = ProductAfterClickPage(driver)
        back = after_click.check_back_button()
        back.click()

        print(driver.current_url)
        assert driver.current_url == "https://www.saucedemo.com/inventory.html"



    #test in add to cart clickable? displayed?
    #@pytest.mark.skip
    def test_add_to_cart(self):
        driver = self.driver
        driver.get(var_info.url_product)
        product = ProductPage(driver)
        product.click_product_label("Sauce Labs Onesie")

        after_click = ProductAfterClickPage(driver)
        add_to_cart = after_click.check_add_to_cart()
        add_to_cart.click()
        cart_sign = after_click.check_cart_sign()
        cart_qty = after_click.check_cart_qty()
        add_to_cart1 = after_click.check_add_to_cart()
        time.sleep(3)

        assert add_to_cart1.text == "REMOVE"
        assert cart_sign.is_displayed()
        assert cart_qty == "1"


    #@pytest.mark.skip
    def test_add_items_back_and_forth(self):
        driver = self.driver
        driver.get(var_info.url_product)
        product = ProductPage(driver)
        product.click_product_label("Test.allTheThings() T-Shirt (Red)")
        time.sleep(8)
        after_click = ProductAfterClickPage(driver)
        add_to_cart1 = after_click.check_add_to_cart()
        add_to_cart1.click()
        after_click.check_cart_qty()
        back = after_click.check_back_button()
        back.click()
        product.click_img(3)
        time.sleep(8)
        add_to_cart2 = after_click.check_add_to_cart()
        add_to_cart2.click()
        check_add_label = after_click.check_add_to_cart()
        cart_qty_total = after_click.check_cart_qty()
        time.sleep(3)

        assert cart_qty_total == "2"
        assert check_add_label.text == "REMOVE"


    @pytest.mark.skip
    def test_add_items_checkout(self):
        driver = self.driver
        driver.get(var_info.url_product)
        product = ProductPage(driver)
        product.click_product_label("Sauce Labs Bike Light")
        after_click = ProductAfterClickPage(driver)
        add_to_cart1 = after_click.check_add_to_cart()
        add_to_cart1.click()
        cart_qty = after_click.check_cart_qty()
        #cart_qty.click()
        cart_sign = after_click.check_cart_sign()
        cart_sign.click()

        assert cart_qty == "1"
        assert driver.current_url == "https://www.saucedemo.com/cart.html"





"""



