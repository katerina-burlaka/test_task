from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException, NoSuchElementException, StaleElementReferenceException


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 30
        self.wait = WebDriverWait(self.driver, self.timeout, poll_frequency=1)
        self.by = By

    def go_to_url(self, url):
        try:
            self.driver.set_page_load_timeout(time_to_wait=60)
            self.driver.get(url)
        except Exception as error:
            raise Exception("Unable to load the page.\nError: {}".format(error))

    def wait_for_visibility_of_web_element(self, locator):
        try:
            web_element = self.wait.until(EC.visibility_of_element_located((locator[0], locator[1])))
            return web_element
        except TimeoutException:
            raise Exception("The web element is not present or not displayed within {} seconds.".format(self.timeout))

    def wait_for_invisibility_of_web_element(self, locator):
        try:
            web_element = self.wait.until(EC.invisibility_of_element_located((locator[0], locator[1])))
            return web_element
        except TimeoutException:
            raise Exception("The web element is present within {} seconds.".format(self.timeout))

    def get_web_element(self, locator):
        web_element = self.driver.find_element(locator[0], locator[1])

        return web_element

    def get_web_elements_list(self, locator):
        web_elements = self.driver.find_elements(locator[0], locator[1])

        return web_elements

    def click_web_element(self, locator):
        web_element = self.get_web_element(locator)
        web_element.click()

        return web_element

    def set_web_element_text(self, locator, text, click_enter=False):
        web_element = self.get_web_element(locator)
        web_element.clear()
        web_element.send_keys(text)
        if click_enter:
            web_element.send_keys(Keys.ENTER)

    def get_web_element_text(self, locator):
        return self.get_web_element(locator).text

    def is_web_element_displayed(self, locator):
        try:
            web_element = self.get_web_element(locator)
            return web_element.is_displayed()
        except (NoSuchElementException, StaleElementReferenceException):
            return False
