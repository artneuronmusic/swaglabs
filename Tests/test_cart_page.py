import pytest
import os.path
import sys
import time


sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from Info import var_info
from Pages.login_page import LoginPage
from Pages.product_page import ProductPage
from Pages.cart_page import CartPage
from Pages.product_individual_page import DetailsPage
from Pages.outside_element import OutSideElement

@pytest.mark.usefixtures("driver")
class TestCartPageWithoutProducts():

    @pytest.mark.skip
    #should not
    def test_cart_with_no_product_product_page(self):
        driver = self.driver
        driver.get(var_info.url_product)
        product = ProductPage(driver)
        product.cart_sign().click()
        cart = CartPage(driver)
        title = cart.cart_title()
        qty_label = cart.cart_qty_label()
        desc_label = cart.cart_desc_label()
        items_display = cart.total_product_in_cart()




        assert title.text == "Your Cart"
        assert qty_label.is_displayed()
        assert desc_label.is_displayed()
        assert items_display == None


    @pytest.mark.skip
    # should not
    def test_no_product_no_checkout_page(self):
        driver = self.driver
        driver.get(var_info.url_product)
        product = ProductPage(driver)
        product.cart_sign().click()
        cart = CartPage(driver)
        checkout_button = cart.cart_checkout_button()
        checkout_button.click()

        assert driver.current_url != "https://www.saucedemo.com/checkout-step-one.html"

    @pytest.mark.skip
    # should not
    def test_no_product_continue_shopping(self):
        driver = self.driver
        driver.get(var_info.url_product)
        product = ProductPage(driver)
        product.cart_sign().click()
        cart = CartPage(driver)
        shopping_button = cart.cart_continue_shopping()
        shopping_button.click()

        assert driver.current_url == "https://www.saucedemo.com/inventory.html"


@pytest.mark.usefixtures("driver")
class TestDisplay():

    #@pytest.mark.skip
    def test_displayed_products_in_page(self):
        driver = self.driver
        driver.get(var_info.url_product)
        product = ProductPage(driver)
        product.click_add_to_cart(2)
        product.click_add_to_cart(6)

        sign = product.cart_sign()
        sign.click()
        cart = CartPage(driver)
        items_display = cart.total_product_in_cart()
        qty = cart.cart_qty()

        assert items_display == 2
        assert qty.text == "2"



    #@pytest.mark.skip
    #checkout successfully
    def test_displayed_products_checkout_button(self):
        driver = self.driver
        driver.get(var_info.url_product)
        product = ProductPage(driver)
        product.click_add_to_cart(2)
        product.click_add_to_cart(6)

        sign = product.cart_sign()
        sign.click()
        cart = CartPage(driver)
        checkout_button = cart.cart_checkout_button()
        checkout_button.click()

        assert driver.current_url == "https://www.saucedemo.com/checkout-step-one.html"

    #@pytest.mark.skip
    def test_remove_checkout(self):
        driver = self.driver
        driver.get(var_info.url_product)
        product = ProductPage(driver)
        product.click_add_to_cart(2)
        product.click_add_to_cart(6)

        sign = product.cart_sign()
        sign.click()
        cart = CartPage(driver)
        cart.cart_product_remove(1)
        items_display = cart.total_product_in_cart()
        qty = cart.cart_qty()

        assert items_display == 1
        assert qty.text == "1"



    #@pytest.mark.skip
    #redierect to prodcut page
    def test_continue_shopping_button(self):
        driver = self.driver
        driver.get(var_info.url_product)
        product = ProductPage(driver)
        product.click_add_to_cart(2)
        product.click_add_to_cart(6)
        sign = product.cart_sign()
        sign.click()
        cart = CartPage(driver)
        shopping_button = cart.cart_continue_shopping()
        shopping_button.click()

        assert driver.current_url == "https://www.saucedemo.com/inventory.html"
        pro2 = product.product_add_to_cart(2)
        pro6 = product.product_add_to_cart(6)

        assert pro2.text == "REMOVE"
        assert pro6.text == "REMOVE"




    #@pytest.mark.skip
    #displays should be all gone, but....u will get ERROR
    def test_reset_button(self):
        driver = self.driver
        driver.get(var_info.url_product)
        product = ProductPage(driver)
        product.click_add_to_cart(2)
        product.click_add_to_cart(6)
        sign = product.cart_sign()
        sign.click()
        product.pick_item_from_menu("Reset App State")
        cart = CartPage(driver)
        qty = cart.cart_qty()
        items_display = cart.total_product_in_cart()

        assert qty == None
        assert items_display == None



@pytest.mark.usefixtures("driver")
class TestIndividualPageToCart():

    #@pytest.mark.skip
    #it will redirect back to product page
    def test_individual_page_to_cart(self):
        driver = self.driver
        driver.get(var_info.url_product)
        product = ProductPage(driver)
        product.click_product_label(4)
        individual = DetailsPage(driver)
        individual.check_single_add_to_cart().click()
        individual.cart_sign().click()
        cart = CartPage(driver)
        qty = cart.cart_qty()
        items_display = cart.total_product_in_cart()

        assert items_display == 1
        assert qty.text == "1"
        assert driver.current_url == "https://www.saucedemo.com/cart.html"








