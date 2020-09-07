"""
    All the actions that can a user do in the browser
"""

from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from config import assert_true_output


class Element(object):
    """
        Element class
    """

    def __init__(self, conf):
        """
            *** DRIVER IS ONLY DEFINED WHEN A BROWSER INSTANCE IS UP ***
            driver is the driverriver that is defined on config -> FixturesLocal
        """

        self.conf = conf
        self.driver = conf.driver

    def exists(self, target, path_type="xpath", msg="-"):
        """
            Checks that element exists in dom and is visible
        """
        success = True
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        error_message = path_type + " was NOT FOUND or is not visible: '" + target + "' " \
                            "\n- URL: '" + driver.current_url + "'\n" + msg

        try:
            if path_type == "xpath":
                wait.until(conditions.visibility_of_element_located((By.XPATH, target)))

            elif path_type == "css":
                wait.until(conditions.visibility_of_element_located((By.CSS_SELECTOR, target)))

            elif path_type == "id":
                wait.until(conditions.visibility_of_element_located((By.ID, target)))

            elif path_type == "link_text":
                wait.until(conditions.visibility_of_element_located((By.LINK_TEXT, target)))

            elif path_type == "class_name":
                wait.until(conditions.visibility_of_element_located((By.CLASS_NAME, target)))

        except TimeoutException:
            success = False

        finally:
            assert_true_output(self.conf, success, error_message)

    def find_and_click(self, target, path_type="xpath", msg="-"):
        """
            This function waits to present a html element and then clink on it.
        """

        success = True
        driver = self.driver

        error_message = path_type + " was NOT FOUND (or is invisible) TO CLICK: '" + target + \
                        "' - URL: '" + driver.current_url + "'\n" + msg
        self.exists(target, path_type, error_message)

        try:
            if path_type == "xpath":
                self.focus(target)
                driver.find_element_by_xpath(target).click()

            elif path_type == "css":
                driver.find_element_by_css_selector(target).click()

            elif path_type == "id":
                driver.find_element_by_id(target).click()

            elif path_type == "link_text":
                driver.find_element_by_link_text(target).click()

            elif path_type == "class_name":
                driver.find_element_by_name(target).click()

        except TimeoutException:
            success = False

        finally:
            assert_true_output(self.conf, success, error_message)

    def exists_in_dom(self, target, path_type="xpath", msg="-"):
        """
            Checks that element exists in dom. It may be invisible
        """
        success = True
        driver = self.driver

        error_message = path_type + " does NOT EXIST IN DOM (visible or invisible): '" \
                        + target + "' \n- URL: '" + driver.current_url + "'\n" + msg

        if path_type == "xpath":
            if not driver.find_elements_by_xpath(target):
                success = False

        elif path_type == "css":
            if not driver.find_elements_by_css_selector(target):
                success = False

        elif path_type == "id":
            if not driver.find_elements_by_id(target):
                success = False

        elif path_type == "link_text":
            if not driver.find_element_by_link_text(target):
                success = False

        elif path_type == "class_name":
            if not driver.find_elements_by_name(target):
                success = False

        assert_true_output(self.conf, success, error_message)

    def not_displayed(self, target, path_type="xpath", msg="-"):
        """
            Ckecks that element exists in dom but it is NOT VISIBLE
        """
        success = True
        driver = self.driver

        error_message = path_type + " is DISPLAYED: '" + target + \
                        "' - URL: '" + driver.current_url + "'\n" + msg

        driver.implicitly_wait(1)

        try:
            if path_type == "xpath":
                if driver.find_element_by_xpath(target).is_displayed():
                    success = False

            elif path_type == "css":
                if driver.find_element_by_css_selector(target).is_displayed():
                    success = False

            elif path_type == "id":
                if driver.find_element_by_id(target).is_displayed():
                    success = False

            elif path_type == "class_name":
                if driver.find_element_by_name(target).is_displayed():
                    success = False

        except NoSuchElementException:
            success = False
            error_message = path_type + " does NOT EXIST IN DOM (visible or invisible): '" \
                            + target + "' - URL: '" + driver.current_url + "'\n" + msg

        finally:
            driver.implicitly_wait(5)
            assert_true_output(self.conf, success, error_message)

    def not_exists(self, target, path_type="xpath", msg="-"):
        """
            Checks that element does not exist in dom (visible or invisible)
        """
        success = True
        driver = self.driver

        error_message = path_type + " EXISTS IN DOM (visible or invisible): '" + target + \
                        "' - URL: '" + driver.current_url + "'\n" + msg

        driver.implicitly_wait(1)

        if path_type == "xpath":
            found_number = len(driver.find_elements_by_xpath(target))
            if found_number != 0:
                success = False

        elif path_type == "css":
            found_number = len(driver.find_elements_by_css_selector(target))
            if found_number != 0:
                success = False

        elif path_type == "id":
            found_number = len(driver.find_elements_by_id(target))
            if found_number != 0:
                success = False

        elif path_type == "class_name":
            found_number = len(driver.find_elements_by_name(target))
            if found_number != 0:
                success = False

        assert_true_output(self.conf, success, error_message)

    def set_text(self, target, text, path_type="xpath"):
        """
            Set text to a visible element
        """

        driver = self.driver

        self.find_and_click(target, path_type, "Element must exist to set text")

        if path_type == "xpath":
            driver.find_element_by_xpath(target).clear()
            driver.find_element_by_xpath(target).send_keys(text)

        elif path_type == "css":
            driver.find_element_by_css_selector(target).clear()
            driver.find_element_by_css_selector(target).send_keys(text)

        elif path_type == "id":
            driver.find_element_by_id(target).clear()
            driver.find_element_by_id(target).send_keys(text)

        elif path_type == "class_name":
            driver.find_element_by_name(target).clear()
            driver.find_element_by_name(target).send_keys(text)

    def get_attribute(self, target, attr_type, path_type="xpath"):
        """
            Get an attribute from a visible element
            attr_type = "href" or "class" etc
        """

        driver = self.driver
        attribute_value = None

        self.exists(target, path_type, "Element must exist and be visible to get an attribute")

        if path_type == "xpath":
            attribute_value = driver.find_element_by_xpath(target).get_attribute(attr_type)

        elif path_type == "css":
            attribute_value = driver.find_element_by_css_selector(target).get_attribute(attr_type)

        elif path_type == "id":
            attribute_value = driver.find_element_by_id(target).get_attribute(attr_type)

        elif path_type == "class_name":
            attribute_value = driver.find_element_by_name(target).get_attribute(attr_type)

        # assert_true_output(self.conf, success)
        return attribute_value

    def checkbox_is_selected(self, target, path_type="xpath"):
        """
            Returns boolean if checkbox is selected or not
        """

        driver = self.driver
        is_selected = ""
        self.exists(target, path_type, "Element must exist to get text")

        if path_type == "xpath":
            is_selected = driver.find_element_by_xpath(target).is_selected()

        elif path_type == "css":
            is_selected = driver.find_element_by_css_selector(target).is_selected()

        elif path_type == "id":
            is_selected = driver.find_element_by_id(target).is_selected()

        elif path_type == "class_name":
            is_selected = driver.find_element_by_name(target).is_selected()

        return is_selected

    def get_text(self, target, path_type="xpath"):
        """
            Get the text of a visible element
        """

        driver = self.driver
        text_value = None

        self.exists(target, path_type, "Element must exist to get text")

        if path_type == "xpath":
            text_value = driver.find_element_by_xpath(target).text

        elif path_type == "css":
            text_value = driver.find_element_by_css_selector(target).text

        elif path_type == "id":
            text_value = driver.find_element_by_id(target).text

        elif path_type == "class_name":
            text_value = driver.find_element_by_name(target).text

        return text_value

    def count_existed_paths(self, target, path_type="xpath"):
        """
            Returns number of existing paths. If count = 0, returns False
        """

        driver = self.driver
        count = 0

        if path_type == "xpath":
            count = (len(driver.find_elements_by_xpath(target)))

        elif path_type == "css":
            count = len(driver.find_elements_by_css_selector(target))

        elif path_type == "id":
            count = len(driver.find_elements_by_id(target))

        elif path_type == "link_text":
            count = len(driver.find_element_by_link_text(target))

        elif path_type == "class_name":
            count = len(driver.find_elements_by_name(target))

        return count

    def check_elements_count(self, target, count, msg="", path_type="xpath"):
        """
            Asserts that elements quantity = count
        """

        driver = self.driver
        current_count = 0

        if path_type == "xpath":
            current_count = len(driver.find_elements_by_xpath(target))

        elif path_type == "css":
            current_count = len(driver.find_elements_by_css_selector(target))

        elif path_type == "id":
            current_count = len(driver.find_elements_by_id(target))

        elif path_type == "link_text":
            current_count = len(driver.find_element_by_link_text(target))

        elif path_type == "class_name":
            current_count = len(driver.find_elements_by_name(target))

        assert_true_output(self.conf, count == current_count, msg)

    def get_html(self, target, path_type="xpath"):
        """
            Returns the outer html of the element
        """

        element = None
        driver = self.driver

        if path_type == "xpath":
            element = driver.find_element_by_xpath(target)

        elif path_type == "css":
            element = driver.find_element_by_css_selector(target)

        elif path_type == "id":
            element = driver.find_element_by_id(target)

        elif path_type == "class_name":
            element = driver.find_element_by_name(target)

        else:
            assert_true_output(self.conf, False, "Please insert a valid path_type")

        return element.get_attribute("outerHTML")

    def open_page_in_new_tab(self, url):
        """
            :param url: Give the url you want to open in new tab
        """

        body = self.driver.find_element_by_tag_name("body")
        body.send_keys(Keys.CONTROL + 't')

        self.driver.get(str(url))

    def get_element(self, target, path_type="xpath", get_multiple_items=False):
        """
            Returns a webdriver element. At least one must exist
            If get_multiple_items == True, returns an array of all items
        """
        driver = self.driver

        self.exists(target, path_type, "At least 1 element must exist and be visible")
        element = None

        if path_type == "xpath":
            element = driver.find_elements_by_xpath(target)

        elif path_type == "css":
            element = driver.find_elements_by_css_selector(target)

        elif path_type == "id":
            element = driver.find_elements_by_id(target)

        elif path_type == "class_name":
            element = driver.find_elements_by_name(target)

        assert_true_output(self.conf, False, "Unknown path_type <" + path_type + ">")
        element = element if get_multiple_items else element[0]

        return element

    def find_by_xpath(self, xpath):
        """
        presses enter key
        """
        driver = self.driver
        driver.find_element_by_xpath(xpath).send_keys(Keys.ENTER)

    def scroll(self, move="down"):
        """
            Scrolling
        """
        driver = self.driver

        if move == "home":
            driver.find_element_by_xpath('//body').send_keys(Keys.HOME)
        elif move == "up":
            driver.find_element_by_xpath('//body').send_keys(Keys.PAGE_UP)
        elif move == "down":
            driver.find_element_by_xpath('//body').send_keys(Keys.PAGE_DOWN)
        elif move == "left":
            driver.find_element_by_xpath('//body').send_keys(Keys.ARROW_LEFT)
        elif move == "right":
            driver.find_element_by_xpath('//body').send_keys(Keys.ARROW_RIGHT)
        elif move == "end":
            driver.find_element_by_xpath('//body').send_keys(Keys.END)
        elif move == "arrow_down":
            driver.find_element_by_xpath('//body').send_keys(Keys.ARROW_DOWN)
        elif move == "arrow_up":
            driver.find_element_by_xpath('//body').send_keys(Keys.ARROW_UP)
        elif move == "escape":
            driver.find_element_by_xpath('//body').send_keys(Keys.ESCAPE)


    def focus(self, target):
        """
            center the element on browser
            currently supports only xpaths
        """
        driver = self.driver

        position = driver.find_element_by_xpath(target).location["y"] - 200
        driver.execute_script("window.scrollTo(0," + str(position) + ")")

    def hover(self, target):
        """
            use self.focus to be on the same high when click the element
            hover on element
            currently supports only xpaths
        """
        driver = self.driver

        self.exists(target, "xpath")

        self.focus(target)

        element_to_hover = driver.find_element_by_xpath(target)
        hover = ActionChains(driver).move_to_element(element_to_hover)
        hover.perform()
