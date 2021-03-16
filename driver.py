from selenium import webdriver


class WebDriver:
    def __init__(self, browser="Chrome", implicit_wait=1):
        self.browser = browser
        self.implicit_wait = implicit_wait

    def get_driver(self):
        try:
            driver = webdriver.Chrome(options=webdriver.ChromeOptions())
            driver.maximize_window()
            driver.implicitly_wait(self.implicit_wait)
        except Exception as error:
            raise Exception("{} browser launch failed!\nError: `{}`".format(self.browser, error))

        return driver
