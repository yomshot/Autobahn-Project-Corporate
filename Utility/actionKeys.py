from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import NoSuchElementException
from Utility import helper

class MakeAction(object):

    def __init__(self, driver):
        self.driver = driver

    def wait_until_element_visible(self, by, locator, wait=3):
        by = helper.method_by(by)
        try:
            element = WebDriverWait(self.driver, wait).until(
                EC.visibility_of_element_located((by, locator))
            )
            if element:
                print("Element {0} Found".format(locator))
                return True
            else:
                print("Element {0} NOT Found".format(locator))
                return False
        except TimeoutException:
            print("Element {0} Not Found".format(locator))
            return False

    def wait_until_element_not_visible(self, by, locator, wait=3):
        by = helper.method_by(by)
        try:
            element = WebDriverWait(self.driver, wait).until(
                EC.invisibility_of_element_located((by, locator))
            )
            if element:
                return True
        except TimeoutException as e:
            print(e)
            return False

    def click_element(self, by, locator, wait=5):
        by = helper.method_by(by)
        try:
            element = WebDriverWait(self.driver, wait).until(
                EC.element_to_be_clickable((by, locator))
            )
            element.click()
            print('Click Element {0}'.format(locator))
            return True
        except (NoSuchElementException, WebDriverException, TimeoutException):
            print('Click Element %s is fail' % locator)
            return False

    def find_elements(self, by: str, locator: str, wait=4):
        by = helper.method_by(by)
        try:
            element = WebDriverWait(self.driver, int(wait)).until(
                EC.visibility_of_element_located((by, locator))
            )
            print("Element " + locator + " Found")
            return element
        except TimeoutException:
            print("Find_Elements {0} has reached Timeout Exception".format(locator))
            return None

    def find_element_and_input(self, by: str, locator: str, wait: int, text: str):
        element = self.find_elements(by, locator, wait)
        if element:
            element.send_keys(text)
            return True
        else:
            return False