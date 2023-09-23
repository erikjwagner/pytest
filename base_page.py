from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.switch_to import Alert
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException, NoSuchElementException, StaleElementReferenceException, ElementNotVisibleException
from selenium.webdriver.common.action_chains import ActionChains
import datetime

class BasePage():
    def __init__(self, driver, selector=None, find_element_wait=180, find_elements_wait=10, xtra=False):
        self.driver = driver
        self.selector = selector
        self.find_element_wait = find_element_wait
        self.find_elements_wait = find_elements_wait
        self.xtra = xtra

    def get(self, url):
      return self.driver.get(url)

    def format_date(dateToFormat):
        return datetime.datetime.strftime(dateToFormat, "%m/%d/%Y")

    def wait_text_present(self, text_displayed="", *args):
        """ Checks for text in element """
        by_locator = self.selector
        len_args = len(args)
        if len_args > 0:
            by_locator = f"{by_locator[0]}", f"{by_locator[1].format(*args)}"
        text = "Element"
        if len(by_locator) == 3:
            text = by_locator[2]
        return WebDriverWait(self.driver, self.find_element_wait).until(EC.text_to_be_present_in_element((by_locator[0], by_locator[1]), text_displayed), f"'{text}' not found in element with properties (By.{by_locator[0]}, '{by_locator[1]}')")

    def backspace(self, *args):
        """ Backspaces text from field """
        by_locator = self.selector
        len_args = len(args)
        if len_args > 0:
            by_locator = f"{by_locator[0]}", f"{by_locator[1].format(*args)}"
        text = "Element"
        if len(by_locator) == 3:
            text = by_locator[2]
        element = WebDriverWait(self.driver, self.find_element_wait).until(EC.visibility_of_element_located((by_locator[0], by_locator[1])), text)
        for _ in range(len(element.get_attribute("value"))):
            element.send_keys(Keys.BACKSPACE)

    def wait_enabled(self, *args):
        """ Waits for element to be enabled """
        by_locator = self.selector
        len_args = len(args)
        if len_args > 0:
            by_locator = f"{by_locator[0]}", f"{by_locator[1].format(*args)}"
        text = "Element"
        if len(by_locator) == 3:
            text = by_locator[2]
        WebDriverWait(self.driver, self.find_element_wait).until(cc.wait_for_element_enabled((by_locator[0], by_locator[1])), text)

    def wait_clickable(self, *args):
        """ Checks for element can be clicked """
        by_locator = self.selector
        len_args = len(args)
        if len_args > 0:
            by_locator = f"{by_locator[0]}", f"{by_locator[1].format(*args)}"
        text = "Element"
        if len(by_locator) == 3:
            text = by_locator[2]
        WebDriverWait(self.driver, self.find_element_wait).until(EC.element_to_be_clickable((by_locator[0], by_locator[1])), text)

    def wait_visible(self, *args):
        """ Checks for visibility of element """
        by_locator = self.selector
        len_args = len(args)
        if len_args > 0:
            by_locator = f"{by_locator[0]}", f"{by_locator[1].format(*args)}"
        text = "Element"
        if len(by_locator) == 3:
            text = by_locator[2]
        WebDriverWait(self.driver, self.find_element_wait).until(EC.visibility_of_element_located((by_locator[0], by_locator[1])), text)

    def assert_not_displayed(self, *args):
        """ Checks for element displayed """
        by_locator = self.selector
        len_args = len(args)
        if len_args > 0:
            by_locator = f"{by_locator[0]}", f"{by_locator[1].format(*args)}"
        text = "Element"
        if len(by_locator) == 3:
            text = by_locator[2]
        assert len(self.find_elements()) == 0, "Displayed when shouldn't be"
        # assert not WebDriverWait(self.driver, self.find_element_wait).until(EC.visibility_of_element_located((by_locator[0], by_locator[1]))).is_displayed(), f"{text} is displayed"

    def assert_displayed(self, *args):
        """ Checks for element displayed """
        by_locator = self.selector
        len_args = len(args)
        if len_args > 0:
            by_locator = f"{by_locator[0]}", f"{by_locator[1].format(*args)}"
        text = "Element"
        if len(by_locator) == 3:
            text = by_locator[2]
        if self.xtra:
            print(f"\tAsserting {text} is displayed")
        try:
            assert WebDriverWait(self.driver, self.find_element_wait).until(EC.visibility_of_element_located((by_locator[0], by_locator[1]))).is_displayed(), f"{text} is not displayed"
        except StaleElementReferenceException:
            print("Got a stale element")
            assert WebDriverWait(self.driver, self.find_element_wait).until(EC.visibility_of_element_located((by_locator[0], by_locator[1]))).is_displayed(), f"{text} is not displayed"

    def assert_enabled(self, *args):
        """ Checks for element enabled """
        by_locator = self.selector
        len_args = len(args)
        if len_args > 0:
            by_locator = f"{by_locator[0]}", f"{by_locator[1].format(*args)}"
        text = "Element"
        if len(by_locator) == 3:
            text = by_locator[2]
        assert WebDriverWait(self.driver, self.find_element_wait).until(EC.visibility_of_element_located((by_locator[0], by_locator[1]))).is_enabled(), f"{text} is not enabled"

    def assert_text_displayed(self, expected_text, *args):
        """ Asserts the text element is equal to expected_text """
        by_locator = self.selector
        len_args = len(args)
        if len_args > 0:
            by_locator = f"{by_locator[0]}", f"{by_locator[1].format(*args)}"
        text = "Element"
        if len(by_locator) == 3:
            text = by_locator[2]
        actual_text = WebDriverWait(self.driver, self.find_element_wait).until(EC.visibility_of_element_located((by_locator[0], by_locator[1])), text).text
        assert actual_text == expected_text, f"Expected Text Does Not Match Actual Text for {text}\n\t\tExpected text: '{expected_text}'\n\t\tActual text  : '{actual_text}'"

    def click(self, *args):
        """ Performs click on web element whose locator is passed to it"""
        by_locator = self.selector
        len_args = len(args)
        if len_args > 0:
            by_locator = f"{by_locator[0]}", f"{by_locator[1].format(*args)}"
        text = ""
        if len(by_locator) == 3:
            text = by_locator[2]
        if self.xtra:
            print(f"\tClick {text}")
        return WebDriverWait(self.driver, self.find_element_wait).until(EC.element_to_be_clickable((by_locator[0], by_locator[1])), text).click()

    def send_keys(self, text, *args):
        """ Performs text entry of the passed in text, in a web element whose locator is passed to it"""
        by_locator = self.selector
        len_args = len(args)
        if len_args > 0:
            by_locator = f"{by_locator[0]}", f"{by_locator[1].format(*args)}"
        message = ""
        if len(by_locator) == 3:
            message = by_locator[2]
        if self.xtra:
            print(f"\tSending Keys {message}")
        return WebDriverWait(self.driver, self.find_element_wait).until(EC.visibility_of_element_located((by_locator[0], by_locator[1])), message).send_keys(text)

    def find_elements(self, *args):
        """ Returns list of elements, use with caution, will take as long as implicitly_wait setting """
        by_locator = self.selector
        self.driver.implicitly_wait(self.find_elements_wait)
        len_args = len(args)
        if len_args > 0:
            by_locator = f"{by_locator[0]}", f"{by_locator[1].format(*args)}"
        return self.driver.find_elements(by_locator[0], by_locator[1])

    def find_element(self, *args):
        """ Returns one web element """
        by_locator = self.selector
        len_args = len(args)
        if len_args > 0:
            by_locator = f"{by_locator[0]}", f"{by_locator[1].format(*args)}"
        return WebDriverWait(self.driver, self.find_element_wait).until(EC.visibility_of_element_located((by_locator[0], by_locator[1])))
        # return self.driver.find_element(by_locator[0], by_locator[1])

    # def on_page(self, waitfor=90, *args):
    #     """ Checks for element specified on page """
    #     by_locator = self.selector
    #     len_args = len(args)
    #     if len_args > 0:
    #         by_locator = f"{by_locator[0]}", f"{by_locator[1].format(*args)}"
    #     message = ""
    #     if len(by_locator) == 3:
    #         message = by_locator[2]
    #     return WebDriverWait(self.driver, waitfor).until(EC.visibility_of_element_located((by_locator[0], by_locator[1])), message)

    def get_current_url(self):
        return self.driver.current_url

    def get_switch_to_window(self, tab_name):
        parent_tab = 0
        child_tab = 1
        if tab_name == parent_tab:
            self.driver.switch_to.window(window_name=self.driver.window_handles[parent_tab])
        else:
            self.driver.switch_to.window(window_name=self.driver.window_handles[child_tab])

# from libs.base_page import BasePage
 
 
