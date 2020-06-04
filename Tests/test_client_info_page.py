import pytest
import os.path
import sys
import time


sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from Info import var_info
from Pages.product_individual_page import DetailsPage
from Pages.login_page import LoginPage
from Pages.product_page import ProductPage
from Pages.cart_page import CartPage
from Pages.client_info import ClientInfoPage
from Pages.checkout_overview import CheckoutOverview
from Pages.outside_element import OutSideElement




@pytest.mark.usefixtures("driver")
class TestClientInfoPage():

    @pytest.mark.skip
    #since the default is no product, so the information should not go through if clicking continue
    def test_valid_info_continue(self):
        driver = self.driver
        driver.get(var_info.url_checkout_step_one)
        info_page = ClientInfoPage(driver)

        info_page.input_first_name("Jojo")
        info_page.input_last_name("Wang")
        info_page.input_zipcode("77759")
        continue_button = info_page.continue_button()
        continue_button.click()

        cart_sign = info_page.info_cart_sign()
        cart_qty = info_page.info_cart_qty()

        assert driver.current_url != "https://www.saucedemo.com/checkout-step-two.html"
        assert cart_sign.is_displayed()
        assert cart_qty == None

    @pytest.mark.skip
    def test_valid_info_cancel(self):
        driver = self.driver
        driver.get(var_info.url_checkout_step_one)
        info_page = ClientInfoPage(driver)

        info_page.input_first_name("Jojo")
        info_page.input_last_name("Wang")
        info_page.input_zipcode("77759")
        info_page.cancel_button()

        assert driver.current_url == "https://www.saucedemo.com/cart.html"

    @pytest.mark.skip
    def test_blank_info_cancel(self):
        driver = self.driver
        driver.get(var_info.url_checkout_step_one)
        info_page = ClientInfoPage(driver)

        info_page.input_first_name("")
        info_page.input_last_name("")
        info_page.input_zipcode("")
        info_page.cancel_button()


        assert driver.current_url == "https://www.saucedemo.com/cart.html"

    @pytest.mark.skip
    def test_blank_first_name_continue(self):
        driver = self.driver
        driver.get(var_info.url_checkout_step_one)
        info_page = ClientInfoPage(driver)

        info_page.input_first_name("")
        info_page.input_last_name("Korh")
        info_page.input_zipcode("77759")
        c_button = info_page.continue_button()
        c_button.click()

        warning = info_page.warning_sign()

        assert warning.text == "Error: First Name is required"

    @pytest.mark.skip
    def test_blank_last_name_continue(self):
        driver = self.driver
        driver.get(var_info.url_checkout_step_one)
        info_page = ClientInfoPage(driver)

        info_page.input_first_name("JOJO")
        info_page.input_last_name("")
        info_page.input_zipcode("77759")
        c_button = info_page.continue_button()
        c_button.click()

        warning = info_page.warning_sign()

        assert warning.text == "Error: Last Name is required"

    @pytest.mark.skip
    def test_blank_zipcode_continue(self):
        driver = self.driver
        driver.get(var_info.url_checkout_step_one)
        info_page = ClientInfoPage(driver)

        info_page.input_first_name("Jojo")
        info_page.input_last_name("Kong")
        info_page.input_zipcode("")
        c_button = info_page.continue_button()
        c_button.click()

        warning = info_page.warning_sign()

        assert warning.text == "Error: Postal Code is required"

    @pytest.mark.skip
    def test_with_character_zipcode_continue(self):
        driver = self.driver
        driver.get(var_info.url_checkout_step_one)
        info_page = ClientInfoPage(driver)

        info_page.input_first_name("Jojo")
        info_page.input_last_name("Kong")
        info_page.input_zipcode("$%667")

        c_button = info_page.continue_button()
        c_button.click()
        warning = info_page.warning_sign()

        assert warning == True
        assert driver.current_url != "https://www.saucedemo.com/checkout-step-two.html"


    @pytest.mark.skip
    def test_with_character_all_info(self):
        driver = self.driver
        driver.get(var_info.url_checkout_step_one)
        info_page = ClientInfoPage(driver)

        info_page.input_first_name("@#$%^")
        info_page.input_last_name("#$%^")
        info_page.input_zipcode("$%667")
        c_button = info_page.continue_button()
        c_button.click()

        warning = info_page.warning_sign()

        assert warning == True
        assert driver.current_url != "https://www.saucedemo.com/checkout-step-two.html"




@pytest.mark.usefixtures("driver")
class TestBillPage():

    @pytest.mark.skip
    def test_info_display_default(self):
        driver = self.driver
        driver.get(var_info.url_checkout_step_one)
        info_page = ClientInfoPage(driver)

        info_page.input_first_name("@#$%^")
        info_page.input_last_name("#$%^")
        info_page.input_zipcode("$%667")
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

    @pytest.mark.skip
    def test_finish_with_default(self):
        driver = self.driver
        driver.get(var_info.url_checkout_step_one)
        info_page = ClientInfoPage(driver)

        info_page.input_first_name("@#$%^")
        info_page.input_last_name("#$%^")
        info_page.input_zipcode("$%667")
        c_button = info_page.continue_button()
        c_button.click()
        overview = CheckoutOverview(driver)
        result = overview.overview_finish()
        result.click()

        assert result != "https://www.saucedemo.com/checkout-complete.html"

    @pytest.mark.skip
    def test_cancel_with_default(self):
        driver = self.driver
        driver.get(var_info.url_checkout_step_one)
        info_page = ClientInfoPage(driver)
        info_page.input_first_name("@#$%^")
        info_page.input_last_name("#$%^")
        info_page.input_zipcode("$%667")
        c_button = info_page.continue_button()
        c_button.click()
        overview = CheckoutOverview(driver)
        cancel = overview.overview_cancel()
        cancel.click()

        assert driver.current_url == ("https://www.saucedemo.com/inventory.html")



    #@pytest.mark.skip
    def test_cancel_on_your_information(self):
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
        info_page = ClientInfoPage(driver)
        info_page.cancel_button()
        qty = product.cart_qty()
        total = cart.total_product_in_cart()

        assert driver.current_url == "https://www.saucedemo.com/cart.html"
        assert qty.text == "2"
        assert total == 2


    @pytest.mark.skip
    def test_reset_with_items_overview(self):
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

        info_page = ClientInfoPage(driver)
        info_page.input_first_name("@#$%^")
        info_page.input_last_name("#$%^")
        info_page.input_zipcode("$%667")
        c_button = info_page.continue_button()
        c_button.click()

        product.pick_item_from_menu("Reset App State")
        product.delete_button_menu()

        overview = CheckoutOverview(driver)
        total_product = overview.total_product_in_cart()

        qty = product.cart_qty()


        assert qty == None
        assert total_product == None


@pytest.mark.usefixtures("driver")
class TestLastProcess():

    #@pytest.mark.skip
    def test_purchase_successfully_with_products(self):
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

        info_page = ClientInfoPage(driver)
        info_page.input_first_name("@#$%^")
        info_page.input_last_name("#$%^")
        info_page.input_zipcode("$%667")
        c_button = info_page.continue_button()
        c_button.click()

        overview = CheckoutOverview(driver)
        result = overview.overview_finish()
        result.click()
        success = overview.successfully_img()

        product = ProductPage(driver)
        qty = product.cart_qty()
        sign = product.cart_sign()

        assert success == True
        assert driver.current_url == "https://www.saucedemo.com/checkout-complete.html"
        assert qty == None
        assert sign.is_displayed()

    @pytest.mark.skip
    def test_cancel_purchase_before_complete(self):
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

        info_page = ClientInfoPage(driver)
        info_page.input_first_name("@#$%^")
        info_page.input_last_name("#$%^")
        info_page.input_zipcode("$%667")
        c_button = info_page.continue_button()
        c_button.click()

        overview = CheckoutOverview(driver)
        result = overview.overview_cancel()
        result.click()

        product2 = product.product_add_to_cart(2)
        product6 = product.product_add_to_cart(6)

        assert product2.text == "REMOVE"
        assert product6.text == "REMOVE"









