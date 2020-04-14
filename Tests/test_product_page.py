import pytest
import os.path
import sys
import time


sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from Info import var_info
from Pages.login_page import LoginPage
from Pages.product_page import ProductPage

@pytest.mark.usefixtures("test_setup")
class TestProductPage():

    @pytest.mark.skip
    def test_display_menu_items(self):
        driver = self.driver
        driver.get(var_info.url_product)
        product = ProductPage(driver)
        items = product.menu_items()

        assert items == ["All Items", "About", "Logout", "Reset App State"]


    @pytest.mark.skip
    def test_click_All_from_menu(self):
        driver = self.driver
        driver.get(var_info.url_product)
        product = ProductPage(driver)
        product.pick_item_from_menu("All Items")

        assert driver.current_url == "https://www.saucedemo.com/inventory.html"

    @pytest.mark.skip
    def test_click_About_from_menu(self):
        driver = self.driver
        driver.get(var_info.url_product)
        product = ProductPage(driver)
        product.pick_item_from_menu("About")

        assert driver.current_url == "https://saucelabs.com/"

    @pytest.mark.skip
    def test_click_Logout_from_menu(self):
        driver = self.driver
        driver.get(var_info.url_product)
        product = ProductPage(driver)
        product.pick_item_from_menu("Logout")

        assert driver.current_url == "https://www.saucedemo.com/index.html"

    @pytest.mark.skip
    def test_click_Reset_from_menu(self):
        driver = self.driver
        driver.get(var_info.url_product)
        product = ProductPage(driver)
        product.pick_item_from_menu("Reset App State")

        assert driver.current_url == "https://www.saucedemo.com/inventory.html"

    #there is bug here!!!! CHECK IT
    @pytest.mark.skip
    def test_result_Reset_after_select_item(self):
        driver = self.driver
        driver.get(var_info.url_product)
        product = ProductPage(driver)
        click2 = product.click_add_to_cart(2)
        click2 = product.click_add_to_cart(3)
        product.pick_item_from_menu("Reset App State")
        qty_cart = product.cart_qty()

        assert driver.current_url == "https://www.saucedemo.com/inventory.html"
        assert qty_cart == None
        assert click2.text == "ADD TO CART"


    #after delete, the drop down in menu bar is gone
    @pytest.mark.skip
    def test_click_delete_button(self):
        driver = self.driver
        driver.get(var_info.url_product)
        product = ProductPage(driver)
        section = product.delete_button_menu()

        assert section


    @pytest.mark.skip
    def test_display_cart_sign(self):
        driver = self.driver
        driver.get(var_info.url_product)
        product = ProductPage(driver)
        display_cart = product.cart_sign()

        assert display_cart.is_display() == True


    @pytest.mark.skip
    def test_qty_cart_before_add(self):
        driver = self.driver
        driver.get(var_info.url_product)
        product = ProductPage(driver)
        qty_cart = product.cart_qty()

        assert qty_cart == None


    @pytest.mark.skip
    def test_qty_cart_after_add_items(self):
        driver = self.driver
        driver.get(var_info.url_product)
        product = ProductPage(driver)
        click_item1 = product.click_add_to_cart(1)
        click_item3 = product.click_add_to_cart(3)
        click_item4 = product.click_add_to_cart(4)

        qty_cart = product.cart_qty()

        assert qty_cart == "3"
        assert click_item1 == "REMOVE"
        assert click_item3 == "REMOVE"
        assert click_item4 == "REMOVE"


    @pytest.mark.skip
    def test_qty_cart_after_add_or_remove(self):
        driver = self.driver
        driver.get(var_info.url_product)
        product = ProductPage(driver)

        click4 = product.click_add_to_cart(4)
        print(click4.text)
        after_click4 = product.click_add_to_cart(4)
        #print(after_click4.text)

        product.click_add_to_cart(1)
        click2 = product.click_add_to_cart(2)
        click3 = product.click_add_to_cart(3)
        after_click3 = product.click_add_to_cart(3)
        qty_cart = product.cart_qty()

        #assert click4.text == "REMOVE"  =>wont show after u double click it.
        assert after_click4.text == "ADD TO CART"
        assert click2.text == "REMOVE"
        assert after_click3.text == "ADD TO CART"
        assert qty_cart == "2"


    @pytest.mark.skip
    def test_click_cart_sign(self):
        driver = self.driver
        driver.get(var_info.url_product)
        product = ProductPage(driver)
        display_cart = product.cart_sign()
        display_cart.click()

        assert driver.current_url == "https://www.saucedemo.com/cart.html"

    @pytest.mark.skip
    def test_default_product_order(self):
        driver = self.driver
        driver.get(var_info.url_product)
        product = ProductPage(driver)
        order = product.name_display_order()

        assert order == "Name (A to Z)"

    @pytest.mark.skip
    def test_select_index2_product_order(self):
        driver = self.driver
        driver.get(var_info.url_product)
        product = ProductPage(driver)
        order = product.pick_display_order(2)
        list_display = product.name_display_order()

        assert list_display == "Name (Z to A)"

    @pytest.mark.skip
    def test_select_index3_product_order(self):
        driver = self.driver
        driver.get(var_info.url_product)
        product = ProductPage(driver)
        order = product.pick_display_order(3)
        list_display = product.name_display_order()

        assert list_display == "Price (low to high)"

    @pytest.mark.skip
    def test_select_text2_product_order(self):
        driver = self.driver
        driver.get(var_info.url_product)
        product = ProductPage(driver)
        order = product.pick_display_order("Name (A to Z)")
        list_display = product.name_display_order()

        assert list_display == "Name (A to Z)"

    @pytest.mark.skip
    def test_select_text4_product_order(self):
        driver = self.driver
        driver.get(var_info.url_product)
        product = ProductPage(driver)
        order = product.pick_display_order("Price (high to low)")
        list_display = product.name_display_order()

        assert list_display == "Price (high to low)"

    @pytest.mark.skip
    def test_product_label_desc_price_and_index_order(self):
        driver = self.driver
        driver.get(var_info.url_product)
        product = ProductPage(driver)
        order = product.pick_display_order(3)
        label_list = product.product_labels()
        desc_list = product.product_description()
        price_list = product.product_price()


        assert label_list == var_info.name_low_to_high
        assert desc_list == var_info.desc_low_to_high
        assert price_list == var_info.price_low_to_high

    @pytest.mark.skip
    def test_product_label_desc_price_and_text_order(self):
        driver = self.driver
        driver.get(var_info.url_product)
        product = ProductPage(driver)
        order = product.pick_display_order("Price (high to low)")
        label_list = product.product_labels()
        desc_list = product.product_description()
        price_list = product.product_price()


        assert label_list == var_info.name_high_to_low
        assert desc_list == var_info.desc_high_to_low
        assert price_list == var_info.price_high_to_low


    @pytest.mark.skip
    def test_product_imgs_availability(self):
        driver = self.driver
        driver.get(var_info.url_product)
        product = ProductPage(driver)
        imgs_display = product.product_imgs_display_loop()

        assert imgs_display



    def test_product_img_clickable_default_order(self):
        driver = self.driver
        driver.get(var_info.url_product)
        product = ProductPage(driver)
        order = product.name_display_order()
        assert order == "Name (A to Z)"
        product.click_img(1)
        id = var_info.id_a_to_z[1-1]


        print(driver.current_url)
        assert driver.current_url == "https://www.saucedemo.com/inventory-item.html?id=" + id



    def test_product_img_clickable_assigned_order(self):
        driver = self.driver
        driver.get(var_info.url_product)
        product = ProductPage(driver)
        product.pick_display_order("Price (low to high)")
        #assert order == "Price (low to high)"
        product.click_img(3)
        id = var_info.id_low_to_high[3-1]


        print(driver.current_url)
        assert driver.current_url == "https://www.saucedemo.com/inventory-item.html?id=" + id



    def test_product_label_clickable_default_order(self):
        driver = self.driver
        driver.get(var_info.url_product)
        product = ProductPage(driver)
        order = product.name_display_order()
        product.click_product_label(2)
        id = var_info.id_a_to_z[2 - 1]

        print(driver.current_url)
        assert driver.current_url == "https://www.saucedemo.com/inventory-item.html?id=" + id



    def test_product_img_clickable_assigned_order(self):
        driver = self.driver
        driver.get(var_info.url_product)
        product = ProductPage(driver)
        product.pick_display_order("Price (high to low)")
        #assert order == "Price (low to high)"
        product.click_img(5)
        id = var_info.id_high_to_low[5-1]


        print(driver.current_url)
        assert driver.current_url == "https://www.saucedemo.com/inventory-item.html?id=" + id



"""
    def test_img_display(self):
        driver = self.driver
        driver.get(var_info.url_product)
        product = ProductPage(driver)
        product.get_img_src()
"""











