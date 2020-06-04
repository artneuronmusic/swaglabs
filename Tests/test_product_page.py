import pytest
import os.path
import sys
import time


sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from Info import var_info
from Pages.login_page import LoginPage
from Pages.product_page import ProductPage
from Pages.product_individual_page import DetailsPage


#this page is independent, no log in needed

@pytest.mark.usefixtures("driver")
class TestMenuItems():

    #main options for different states
    #@pytest.mark.skip
    def test_display_menu_items(self):
        driver = self.driver
        driver.get(var_info.url_product)
        product = ProductPage(driver)
        items = product.selection_menu()

        #print(items)


        assert items == ["All Items", "About", "Logout", "Reset App State"]

    #@pytest.mark.skip
    # add to two products to cart, click the 'all items', the page will stay the same
    def test_menu_all_items(self):
        driver = self.driver
        driver.get(var_info.url_product)
        product = ProductPage(driver)
        click_add_product = product.click_add_to_cart(1)
        click_another_product = product.click_add_to_cart(3)


        product.pick_item_from_menu("All items")
        product.delete_button_menu()
        time.sleep(2)
        cart_qty = product.cart_qty()

        assert cart_qty.text == "2"
        assert click_add_product == "REMOVE"
        assert click_another_product == "REMOVE"

    #@pytest.mark.skip
    def test_menu_logout(self):
        driver = self.driver
        driver.get(var_info.url_product)
        product = ProductPage(driver)
        product.pick_item_from_menu("Logout")
        assert driver.current_url=="https://www.saucedemo.com/index.html"

    #@pytest.mark.skip
    #'about'  will redirect to new url "https://saucelabs.com/"
    def test_menu_about(self):
        driver = self.driver
        driver.get(var_info.url_product)
        product = ProductPage(driver)
        product.pick_item_from_menu("About")
        assert driver.current_url=="https://saucelabs.com/"

    #@pytest.mark.skip
    # 'Reset' basically should clear cache/data  BUG!!!
    # pick first item in to cart
    def test_menu_reset_state(self):
        driver = self.driver
        driver.get(var_info.url_product)
        product = ProductPage(driver)

        #cart should has one item
        #and the add_to_cart become remove after clicking
        click_add_product = product.click_add_to_cart(1)

        product.pick_item_from_menu("Reset App State")
        product.delete_button_menu()
        cart_qty = product.cart_qty()

        assert click_add_product == "ADD TO CART"
        assert cart_qty == None




    #after delete, the drop down in menu bar is gone
    #@pytest.mark.skip
    def test_click_delete_button(self):
        driver = self.driver
        driver.get(var_info.url_product)
        product = ProductPage(driver)
        product.drop_down_menu()
        section_disappear = product.delete_button_menu()

        assert section_disappear == True

@pytest.mark.usefixtures("driver")
class TestDisplayOrder():
    # check the default display for products(from A to Z)
    #@pytest.mark.skip
    def test_default_product_order(self):
        driver = self.driver
        driver.get(var_info.url_product)
        product = ProductPage(driver)
        order = product.name_display_order()
        product_title = product.product_labels()
        first_display_product = product_title[0]
        last_display_product = product_title[-1]

        assert order == "Name (A to Z)"
        assert first_display_product == "Sauce Labs Backpack"
        assert last_display_product == "Test.allTheThings() T-Shirt (Red)"

    # check product display from Z to A
    #@pytest.mark.skip
    def test_display_Z_to_A(self):
        driver = self.driver
        driver.get(var_info.url_product)
        product = ProductPage(driver)
        order = product.pick_display_order(2)
        list_display = product.name_display_order()
        product_title = product.product_labels()
        first_display_product = product_title[0]
        last_display_product = product_title[-1]

        assert list_display == "Name (Z to A)"
        assert last_display_product == "Sauce Labs Backpack"
        assert first_display_product == "Test.allTheThings() T-Shirt (Red)"

    # check product display from high to low
    #@pytest.mark.skip
    def test_display_high_to_low(self):
        driver = self.driver
        driver.get(var_info.url_product)
        product = ProductPage(driver)
        order = product.pick_display_order(3)
        list_display = product.name_display_order()
        product_title = product.product_labels()
        first_display_product = product_title[0]
        last_display_product = product_title[-1]
        item_price = product.products_price()
        first_price = item_price[0]
        last_price = item_price[-1]

        assert list_display == "Price (low to high)"
        assert first_display_product == "Sauce Labs Onesie"
        assert last_display_product == "Sauce Labs Fleece Jacket"
        assert first_price == "$7.99"
        assert last_price == "$49.99"

    # check is the display
    #@pytest.mark.skip
    def test_display_low_to_high(self):
        driver = self.driver
        driver.get(var_info.url_product)
        product = ProductPage(driver)
        order = product.pick_display_order(4)
        list_display = product.name_display_order()
        product_title = product.product_labels()
        first_display_product = product_title[0]
        last_display_product = product_title[-1]
        item_price = product.products_price()
        first_price = item_price[0]
        last_price = item_price[-1]

        assert list_display == "Price (high to low)"
        assert last_display_product == "Sauce Labs Onesie"
        assert first_display_product == "Sauce Labs Fleece Jacket"
        assert last_price == "$7.99"
        assert first_price == "$49.99"

@pytest.mark.usefixtures("driver")
class TestProductsAndCart():
    # default cart quantity should be none before adding
    #@pytest.mark.skip
    def test_qty_cart_default(self):
        driver = self.driver
        driver.get(var_info.url_product)
        product = ProductPage(driver)
        qty_cart = product.cart_qty()

        assert qty_cart == None

    # the total should be 6 titles, are they all in, default order
    #@pytest.mark.skip
    def test_product_labels(self):
        driver = self.driver
        driver.get(var_info.url_product)
        product = ProductPage(driver)
        product_label_amount = product.product_labels()
        second_label = product_label_amount[1]
        fifth_label = product_label_amount[4]

        assert len(product_label_amount) == 6
        assert second_label != None
        assert fifth_label == "Sauce Labs Onesie"

    # the total should be 6 prices, are they all in, default order
    #@pytest.mark.skip
    def test_product_price(self):
        driver = self.driver
        driver.get(var_info.url_product)
        product = ProductPage(driver)
        product_price = product.products_price()
        third_price = product_price[2]
        fourth_price = product_price[3]

        assert len(product_price) == 6
        assert third_price != None
        assert fourth_price == "$49.99"

    # the total should be 6 descriptions, are they all in, default order
    #@pytest.mark.skip
    def test_product_description(self):
        driver = self.driver
        driver.get(var_info.url_product)
        product = ProductPage(driver)
        product_description = product.products_description()

        assert len(product_description) == 6

    # the total should be 6 'add to cart', are they all in, default order
    #@pytest.mark.skip
    def test_add_to_cart_label(self):
        driver = self.driver
        driver.get(var_info.url_product)
        product = ProductPage(driver)
        displays_add_to_cart = product.product_add_to_cart_label()

        assert displays_add_to_cart == True


    def test_add_to_cart_checkout(self):
        driver = self.driver
        driver.get(var_info.url_product)
        product = ProductPage(driver)
        product.click_add_to_cart(2)
        product.click_add_to_cart(6)
        product.cart_sign().click()

        cart_qty = product.cart_qty()




        assert driver.current_url == "https://www.saucedemo.com/cart.html"
        assert cart_qty.text == "2"


@pytest.mark.usefixtures("driver")
class TestProductClickPage():

    @pytest.mark.skip
    def test_click_label_str(self):
        driver = self.driver
        driver.get(var_info.url_product)
        product = ProductPage(driver)
        product.click_product_label("Sauce Labs Backpack")
        single_page = DetailsPage(driver)
        s_label = single_page.check_single_label()
        assert driver.current_url != "https://www.saucedemo.com/inventory.html"
        assert s_label.text == "Sauce Labs Backpack"
        #s_label.text

    @pytest.mark.skip
    def test_click_label_num(self):
        driver = self.driver
        driver.get(var_info.url_product)
        product = ProductPage(driver)
        product.click_product_label(6)
        single_page = DetailsPage(driver)
        s_label = single_page.check_single_label()
        s_price = single_page.check_single_price()
        s_desc = single_page.check_single_description()
        s_add_to_cart = single_page.check_single_add_to_cart()

        assert driver.current_url != "https://www.saucedemo.com/inventory.html"
        assert s_label.text == "Test.allTheThings() T-Shirt (Red)"
        assert s_price.text == "$15.99"
        assert s_desc.is_displayed()
        assert s_add_to_cart.is_displayed()
        # s_label.text


    @pytest.mark.skip
    def test_products_img_exist(self):

        driver = self.driver
        driver.get(var_info.url_product)
        product = ProductPage(driver)
        time.sleep(5)
        imgs = product.products_img()

        assert imgs == True


    @pytest.mark.skip
    def test_valid_product_img(self):
        driver = self.driver
        driver.get(var_info.url_product)
        product = ProductPage(driver)
        product.click_products_img(5)
        single_page = DetailsPage(driver)
        s_label = single_page.check_single_label()
        s_price = single_page.check_single_price()
        s_desc = single_page.check_single_description()
        s_add_to_cart = single_page.check_single_add_to_cart()




        assert driver.current_url != "https://www.saucedemo.com/inventory.html"
        assert s_label.is_displayed()
        assert s_price.is_displayed()
        assert s_desc.is_displayed()
        assert s_add_to_cart.is_displayed()


@pytest.mark.usefixtures("driver")
class TestIndividualDetail():

    @pytest.mark.skip
    def test_back_button_img(self):
        driver = self.driver
        driver.get(var_info.url_product)
        product = ProductPage(driver)
        product.click_products_img(2)
        single_page = DetailsPage(driver)
        # s_label = single_page.check_single_label()
        # s_price = single_page.check_single_price()
        # s_desc = single_page.check_single_description()
        # s_add_to_cart = single_page.check_single_add_to_cart()
        add_cart = single_page.check_single_add_to_cart()
        add_cart.click()
        total_in_cart = single_page.cart_qty()
        return_button = single_page.back_button()
        return_button.click()

        assert driver.current_url == "https://www.saucedemo.com/inventory.html"
        assert total_in_cart.text == "1"
    #ADD TO CART works
    @pytest.mark.skip
    def test_add_to_cart(self):
        driver = self.driver
        driver.get(var_info.url_product)
        product = ProductPage(driver)
        product.click_products_img(3)
        single_page = DetailsPage(driver)
        add_cart = single_page.check_single_add_to_cart()
        add_cart.click()
        cart_img = single_page.cart_sign()
        total_in_cart = single_page.cart_qty()
        cart_show = single_page.check_single_add_to_cart()


        assert cart_img == True
        assert total_in_cart.text == "1"
        assert cart_show.text == "REMOVE"

    @pytest.mark.skip
    #the remove label should become add to cart
    def test_reset_individual_page(self):
        driver = self.driver
        driver.get(var_info.url_product)
        product = ProductPage(driver)
        product.click_products_img(3)
        single_page = DetailsPage(driver)
        add_cart1 = single_page.check_single_add_to_cart()
        add_cart1.click()
        product.pick_item_from_menu("Reset App State")
        product.delete_button_menu()
        cart_qty = product.cart_qty()
        cart1 = single_page.check_single_add_to_cart()


        assert cart1.text == "ADD TO CART"
        assert cart_qty == None

    @pytest.mark.skip
    def test_resets_then_return(self):
        driver = self.driver
        driver.get(var_info.url_product)
        product = ProductPage(driver)
        product.click_products_img(3)
        single_page = DetailsPage(driver)
        add_cart1 = single_page.check_single_add_to_cart()
        add_cart1.click()
        return_button = single_page.back_button()
        return_button.click()
        product.click_product_label(4)
        add_cart2 = single_page.check_single_add_to_cart()
        add_cart2.click()

        product.pick_item_from_menu("Reset App State")
        product.delete_button_menu()

        return_button = single_page.back_button()
        return_button.click()
        #cart_show_individual = single_page.check_single_add_to_cart()
        cart_qty = product.cart_qty()

        cart3 = product.product_add_to_cart(3)
        cart4 =  product.product_add_to_cart(4)

        #assert cart_show_individual.text == "ADD TO CART"
        assert cart_qty == None
        assert cart3.text == "ADD TO CART"
        assert cart4.text == "ADD TO CART"



    def test_go_checkout_without_product(self):
        driver = self.driver
        driver.get(var_info.url_product)
        product = ProductPage(driver)
        product.click_products_img(3)

        single_page = DetailsPage(driver)
        single_page.cart_sign().click()

        assert driver.current_url == "https://www.saucedemo.com/cart.html"



























