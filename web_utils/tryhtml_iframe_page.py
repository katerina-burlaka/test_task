from web_utils.base_page import BasePage
from time import sleep


class TryHtmlIframePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.run_btn = (self.by.XPATH, "//button[contains(@class, 'w3-button w3-bar-item')]", "Run button")
        self.result_form_iframe = (self.by.XPATH, "//iframe[@name='iframeResult']", "Result form iframe")
        self.search_form_iframe = (self.by.XPATH, "//iframe[contains(@title, 'W3Schools')]", "Search form iframe")
        self.search_input = (self.by.XPATH, "//input[@id='sb_form_q']", "Input for search")
        self.tooltip = (self.by.XPATH, "//span[text()='Maybe later']", "Tooltip")
        self.search_suggestions = (self.by.XPATH, "//ul[@aria-label='Suggestions']/li/div", "Search suggestions")
        self.search_result_links = (self.by.XPATH, "//main[@aria-label='Search Results']//li//cite[text()]", "Search result links")

    def load(self):
        url = "https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_iframe"
        self.go_to_url(url)

    def replace_given_word_in_editor(self, target_value, new_value):
        js_script = "window.editor.setValue(window.editor.getValue().replace('{}','{}'))".format(target_value, new_value)
        self.driver.execute_script(js_script)

    def click_run_button(self):
        self.click_web_element(self.run_btn)

    def switch_to_search_frame(self):
        result_iframe = self.get_web_element(self.result_form_iframe)
        self.driver.switch_to.frame(result_iframe)
        search_iframe = self.get_web_element(self.search_form_iframe)
        self.driver.switch_to.frame(search_iframe)

    def fill_search_input(self, search_string):
        self.wait_for_visibility_of_web_element(self.search_input)
        self.set_web_element_text(self.search_input, search_string, click_enter=True)

    def show_search_suggestions(self):
        self.wait_for_visibility_of_web_element(self.search_input)

        # workaround to cover tooltip issue. sometime it is displayed but sometime is not
        if not self.is_web_element_displayed(self.tooltip):
            sleep(1)

        if self.is_web_element_displayed(self.tooltip):
            js_script = "document.evaluate(\"{}\", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.click()".format(self.tooltip[1])
            self.driver.execute_script(js_script)
            self.wait_for_invisibility_of_web_element(self.tooltip)
        self.click_web_element(self.search_input)

    def get_search_suggestions_list(self):
        suggestions = []
        suggestions_web_elements = self.get_web_elements_list(self.search_suggestions)
        for web_element in suggestions_web_elements:
            suggestions.append(web_element.text)

        return suggestions

    def click_given_suggestion(self, value):
        suggestions_web_elements = self.get_web_elements_list(self.search_suggestions)
        for web_element in suggestions_web_elements:
            if web_element.text == value:
                web_element.click()
                break

    def get_search_result_links_list(self):
        self.wait_for_visibility_of_web_element(self.search_result_links)
        result_links = []
        result_links_web_elements = self.get_web_elements_list(self.search_result_links)
        for web_element in result_links_web_elements:
            result_link = web_element.text
            if result_link:
                result_links.append(result_link)

        return result_links
