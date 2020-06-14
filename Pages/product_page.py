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
    #_item_section = {"by": By.XPATH, "value": "//nav[@class='bm-item-list']"}
    #_all_items = {"by": By.XPATH, "value": "//nav[@class='bm-item-list']//a[@class='bm-item menu-item']"}
    _product_list = {"by": By.CLASS_NAME, "value": "inventory_list"}
    _product_section = {"by": By.CLASS_NAME, "value": "inventory_item"}
    _product_img = {"by": By.XPATH, "value": "//img[@class='inventory_item_img']"}
    _product_label = {"by": By.CLASS_NAME, "value": "inventory_item_name"}
    _product_description = {"by": By.CLASS_NAME, "value": "inventory_item_desc"}
    _product_price = {"by": By.CLASS_NAME, "value": "inventory_item_price"}
    _product_add_to_cart = {"by": By.CLASS_NAME, "value": "btn_inventory"}
    _goods_display_order = {"by": By.XPATH, "value": "//select[@class='product_sort_container']"}


    #product logo
    def product_logo(self):

        return self._find(self._product_logo)


    def pick_display_order(self, input_info):

        pick_position = Select(self._find(self._goods_display_order))
        try:
            if isinstance(input_info, int):
                 pick_position.select_by_index(input_info - 1)

            else:
                 pick_position.select_by_visible_text(input_info)


        except Error:
            raise Error



    #u need to specify the default name
    def default_name_order(self):

        try:
            position = WebDriverSelect(self._find(self._goods_display_order))
            display_name = position.first_selected_option

        except Error:
            raise

        else:
            return display_name

    #the whole labels
    def product_labels(self):
        p_label = self._find_elements(self._product_label)
        label_list = []
        for i in p_label:
            try:
                i.is_displayed()
                new_list = i.text
                label_list.append(new_list)

            except AssertionError:
                print ("Some labels are missing")
                raise

        return label_list

    #single one, and u can assign
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

    #whole price
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


    #single price
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


    #the whole descriptions
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

    #single description
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


    #does specific product has "add to cart" displayed
    def product_add_to_cart(self, info):
        p_cart = self._find_elements(self._product_add_to_cart)
        if isinstance(info, int):
            info = int(info) - 1
            return p_cart[info]

        else:
            raise Error("Please check type of info")

    def add_to_cart_label(self, info):
        p_add_to_cart = self._find_elements(self._product_add_to_cart)
        new_info = int(info) - 1

        try:
            p_add_to_cart[new_info].is_displayed()
            return p_add_to_cart[new_info]

        except (IndexError, ValueError, TypeError):

            raise ("Sth wrong")

    def products_add_to_cart_label(self):
        a_cart_labels = self._find_elements(self._product_add_to_cart)
        appear = False
        for i in a_cart_labels:
            try:
                i.is_displayed()
                appear = True

            except AssertionError:
                raise ("Description(s) missing")

        return appear


    def click_add_to_cart(self, info):

        p_add_to_cart = self._find_elements(self._product_add_to_cart)
        new_info = int(info) - 1
        try:

            p_add_to_cart[new_info].click()
            if p_add_to_cart[new_info].is_displayed():
                return p_add_to_cart[new_info]

        except (IndexError, ValueError, TypeError):

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
        k=0
        for i in product_labels:
            k += 1
            img = i.get_attribute('src')
            if img.endswith(".jpg"):
                return True

            else:
                return False


    def specific_product_img(self, num):
        imgs = self._find_elements(self._product_img)
        num = num - 1
        new = imgs[num].get_attribute("src")
        print(new)
        try:
            if new.endswith(".jpg"):
                return imgs[num].is_displayed()

        except Error:
            raise Error("the img does not have jpg format")

    def click_product_img(self, num):
        imgs = self._find_elements(self._product_img)
        num = num - 1
        new = imgs[num].get_attribute("src")
        print(new)

        if new.endswith(".jpg"):
            return imgs[num].click()
        else:
            print("The img is not normal")
            quit()

        #except Error:
         #   raise Error("the img does not have jpg format")


        # product_labels = self._find_elements(self._product_img)
        #
        # try:
        #     if product_labels[num]:
        #     product_labels = self._find_elements(self._product_img)
        #     num = int(num)-1
        #     product_labels[num].click()
        #
        #
        # except Exception:
        #     raise("this img is invalid for clicking")
        #






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










