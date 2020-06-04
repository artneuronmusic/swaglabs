from selenium.webdriver.common.by import By
from Pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException, TimeoutException, StaleElementReferenceException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.select import Select as WebDriverSelect
from Info.error_control import Error
import time



class ProductPage(BasePage):
    #the same as _after_login
    _product_logo = {"by": By.XPATH, "value": "//div[@class='product_label']"}
    _drop_down = {"by": By.XPATH, "value": "//button[contains(text(), 'Open Menu')]"}
    #_item_section = {"by": By.XPATH, "value": "//nav[@class='bm-item-list']"}
    #_all_items = {"by": By.XPATH, "value": "//nav[@class='bm-item-list']//a[@class='bm-item menu-item']"}
    _all_items = {"by": By.CLASS_NAME, "value": "bm-item"}
    _all_products = {"by": By.CLASS_NAME, "value": "inventory_item"}
    _reset_app_state = {"by": By.XPATH, "value": "//a[@id='reset_sidebar_link']"}
    _delete_button = {"by": By.XPATH, "value": "//button[contains(text(),'Close Menu')]"}


    _cart_sign = {"by": By.XPATH, "value": "//*[name()='path' and contains( @ fill, 'currentCol')]"}
    _cart_qty = {"by": By.XPATH, "value": "//span[@class='fa-layers-counter shopping_cart_badge']"}
    _product_list = {"by": By.CLASS_NAME, "value": "inventory_list"}
    _product_section = {"by": By.CLASS_NAME, "value": "inventory_item"}
    _product_img = {"by": By.XPATH, "value": "//img[@class='inventory_item_img']"}
    _product_label = {"by": By.CLASS_NAME, "value": "inventory_item_name"}
    _product_description = {"by": By.CLASS_NAME, "value": "inventory_item_desc"}
    _product_price = {"by": By.CLASS_NAME, "value": "inventory_item_price"}
    _product_add_to_cart = {"by": By.CLASS_NAME, "value": "btn_inventory"}
    _goods_display_order = {"by": By.XPATH, "value": "//select[@class='product_sort_container']"}

    _back_button = {"by": By.XPATH, "value": "//button[@class='inventory_details_back_button']"}

    #product logo
    def product_logo(self):

        return self._is_displayed(self._product_logo)


    def selection_menu(self):
        self._click(self._drop_down)

        #without using sleep to pause script, but wait unitl the last option show
        self._wait_for_display(self._reset_app_state, 5)

        items = self.driver.find_elements(self._all_items["by"], self._all_items["value"])

        item_list = []
        for i in items:
            if i.is_displayed():

                item_list.append(i.text)

        return item_list

    def drop_down_menu(self):
        self._click(self._drop_down)


    #menu items: delete button
    def delete_button_menu(self):
        #self._click(self._drop_down)
        self._wait_for_click(self._all_items, 5)
        self._click(self._delete_button)
        section = self._wait_for_not_display(self._all_items, 3)

        return section

    #menu items: pick one out of menu bar
    def pick_item_from_menu(self, name):
        self._click(self._drop_down)
        self._wait_for_click(self._all_items, 5)
        items = self.driver.find_elements(self._all_items["by"], self._all_items["value"])
        #self._wait_for_click(self._all_items, 5)

        for i in items:
            try:
                if i.text != name:
                    continue
                else:
                    i.click()
            except StaleElementReferenceException:
                print("StaleElementReferenceException")

    def pick_display_order(self, input_info):

        pick_position = Select(self._find(self._goods_display_order))
        try:
            if isinstance(input_info, int):
                 pick_position.select_by_index(input_info - 1)
            else:
                 pick_position.select_by_visible_text(input_info)

        except ValueError:
            print("Check other element, sth like value of the element")


    def name_display_order(self):
        position = WebDriverSelect(self._find(self._goods_display_order))
        display_name = position.first_selected_option.text

        return display_name


    def cart_sign(self):

            return self._find(self._cart_sign)



    #the cart_amount
    def cart_qty(self):
        if self._is_displayed(self._cart_qty):
            qty = self._find(self._cart_qty)
            return qty

        else:
            return None

    def product_labels(self):
        p_label = self._find_elements(self._product_label)
        label_list = []
        for i in p_label:
            try:
                i.is_displayed()
                new_list = i.text
                label_list.append(new_list)

            except AssertionError:

                raise ("Some labels are missing")

        return label_list


    def product_label(self, info):
        p_desc = self._find_elements(self._product_label)
        if isinstance(info, int):
            info = int(info) - 1
            return p_desc[info]

        elif isinstance(info, str):
            for i in p_desc:
                if i.text == info:
                    return p_desc[i]

                else:
                    continue

        else:
            raise Error("Please check type of info")


    #price_product_price
    def products_price(self):
        ps_price = self._find_elements(self._product_price)
        price_list = []

        for i in ps_price:
            try:
                new_list = i.text
                price_list.append(new_list)

            except AssertionError:

                raise ("Price tag(s) missing")

        return price_list
        #print(price_list)



    def product_price(self, info):
        p_price = self._find_elements(self._product_price)
        if isinstance(info, int):
            info = int(info) - 1
            return p_price[info]

        elif isinstance(info, str):
            for i in p_price:
                if i.text == info:
                    return p_price[i]

                else:
                    continue

        else:
            raise Error("Please check type of info")


    def products_description(self):
        p_desc = self._find_elements(self._product_description)
        desc_list = []
        for i in p_desc:
            try:
                i.is_displayed()
                new_list = i.text
                desc_list.append(new_list)

            except AssertionError:

                raise ("Description(s) missing")

        return desc_list

    def product_description(self, info):
        p_desc = self._find_elements(self._product_description)
        if isinstance(info, int):
            info = int(info) - 1
            return p_desc[info]

        elif isinstance(info, str):
            for i in p_desc:
                if i.text == info:
                    return p_desc[i]

                else:
                    continue

        else:
            raise Error("Please check type of info")

    def product_add_to_cart(self, info):
        p_cart = self._find_elements(self._product_add_to_cart)
        if isinstance(info, int):
            info = int(info) - 1
            return p_cart[info]

        elif isinstance(info, str):
            for i in p_cart:
                if i.text == info:
                    return p_cart[i]

                else:
                    continue

        else:
            raise Error("Please check type of info")



    def product_add_to_cart_label(self):
        a_cart_labels = self._find_elements(self._product_add_to_cart)
        appear = False
        for i in a_cart_labels:
            try:
                i.is_displayed()
                appear = True

            except ValueError:
                raise ("Description(s) missing")

        return appear



    def click_add_to_cart(self, num):

        p_add_to_cart = self._find_elements(self._product_add_to_cart)
        new_num = int(num) - 1
        try:

            p_add_to_cart[new_num].click()
            if p_add_to_cart[new_num].is_displayed():
                return p_add_to_cart[new_num].text

        except (IndexError, ValueError):

            raise ("Sth wrong")


    def click_product_label(self, info):
        product_label = self._find_elements(self._product_label)
        try:

            if isinstance(info, int):
                info = info - 1
                product_label[info].click()

            elif isinstance(info, str):
                for i in product_label:
                    if i.text == info:
                        i.click()
                    else:
                        continue


        except StaleElementReferenceException:
            print("StaleElementReferenceException")


    def products_img(self):
        product_labels = self._find_elements(self._product_img)

        for i in product_labels:
            try:
                i.is_displayed()
                img = i.get_attribute('src')
                if img.endswith(".jpg"):

                    return True

            except Exception:

                raise ("{} does not upload img properly".format(i + 1))





    def click_products_img(self, num):

        try:
            self.products_img()
            product_labels = self._find_elements(self._product_img)
            num = int(num)-1
            product_labels[num].click()


        except Exception:
            raise("this img is invalid for clicking")







"""

   def add_from_product_label(self, item):
        item_label = self._find_elements(self._product_label)
        p_add_to_cart = self._find_elements(self._product_add_to_cart)

        for i in range(len(item_label)):
            if item_label[i].text == item:
                p_add_to_cart[i].click()

            else:
                pass


    
    #label
    def product_labels(self):

        p_label = self._find_elements(self._product_label)
        label_list = []
        for i in p_label:
            try:
                i.is_displayed()
                new_list = i.text
                label_list.append(new_list)

            except ValueError:

                raise("Some labels are missing")

        return label_list


    #click label
    def click_product_label(self, input_info):
        p_label = self._find_elements(self._product_label)
        #for i in range(len(p_label)):
         #   if i == num:
          #      self._wait_for_display(p_label[i-1], 5).click()
           #     return self._find(p_label[i-1])
            #else:
             #   continue
        try:
            if isinstance(input_info, int):

                p_label[input_info - 1].click()
                #return self._find(p_label[input_info - 1])

            else:
                for i in p_label:
                    if i.text == input_info:
                        i.click()
                        #return i.text

                    else:
                        continue
        except StaleElementReferenceException:
            print("StaleElementReferenceException")

        #except (IndexError, ValueError, TypeError):
         #   return False



    #product_img
    def product_imgs_display_loop(self):

        cnt_failed = 0
        p_img = self._find_elements(self._product_img)

        # Test is known to give false-positives. Intentionally left for later bug report.
        for i in range(len(p_img)):
            if p_img[i].is_displayed():
                print("{} img is displayed".format(i))

            else:
                cnt_failed += 1
                print("No {} img is displayed".format(i))

        if cnt_failed > 0:
            raise ("test")

        else:
            return True

    def click_img(self, num):
        p_img = self._find_elements(self._product_img)
        new_num = int(num) - 1
        if p_img[new_num].is_displayed():
            p_img[new_num].click()

        else:
            return False

    def get_img_src(self):

        attribute = self._find(self._product_img).get_attribute('src')
        print(attribute)






    #img
    def product_imgs_display_loop(self):

        cnt_failed = 0
        p_img = self._find_elements(self._product_img)

        # Test is known to give false-positives. Intentionally left for later bug report.
        for i in range(len(p_img)):
            if p_img[i].is_displayed():
                print("{} img is displayed".format(i))

            else:
                cnt_failed += 1
                print("No {} img is displayed".format(i))

        if cnt_failed > 0:
            raise("test")

    def product_imgs_display(self):
        is_not_displayed = False

        p_img = self._find_elements(self._product_img)

        # Test is known to give false-positives. Intentionally left for later bug report.
        for i in range(len(p_img)):
            if p_img[i].is_displayed():
                print("{} img is displayed".format(i))

            else:
                is_not_displayed = True
                print("No {} img is displayed".format(i))

        if is_not_displayed:
            raise("test")


    #n += 1
    #print("No {} img is missing".format(n))



    #raise Exception("")
    #print("No {} img is displayed".format(n))
    #raise ValueError("No {} img exists".format(n))

    #continue



    #click img
    def click_img_onereturn(self, num):
        p_img = self._find_elements(self._product_img)
        #p_img[num].click()

        clickable = False

        try:
            int(num)
            p_img[num].click()

            clickable = True
        except (IndexError, ValueError):
            clickable = False

        return clickable

    def click_img(self, num):
        p_img = self._find_elements(self._product_img)
        #p_img[num].click()

        try:
            int(num)
            p_img[num].click()
            return True
        except (IndexError, ValueError):
            return False
            
            
    def add_to_cart(self):
        p_add_to_cart = self._find_elements(self._product_add_to_cart)
        be_displayed = False
    
        for i in p_add_to_cart:
            if i.is_displayed():
                be_displayed = True
            else:
                be_displayed = False
        return be_displayed
                
            
        #//img[@src='imagename.png']@src

        #value:

        #${img}
        
        
        
    

    #the cart sign
    def cart_sign(self):
        sign = self._find(self._cart_sign)
        return sign
"""










