
import os
from unittest import TestCase
from api import API
from helper import Helper
from db_manager import DB
from driver import WebDriver
from web_utils.tryhtml_iframe_page import TryHtmlIframePage
from functools import reduce


class TestTask(TestCase):

    def test_01_check_image(self):
        api = API()
        helper = Helper()
        url = "http://apimeme.com/meme?meme=Alarm-Clock&top=Top+text&bottom=Bottom+text"
        expected_image = "{}/static_data/example.jpeg".format(os.path.dirname(os.path.realpath(__file__)))
        expected_image_as_base64 = helper.encode_file_as_base64(expected_image)

        actual_image_as_base64 = api.get_image_as_base64(url)
        self.assertEqual(actual_image_as_base64, expected_image_as_base64, "Actual image does not equal to expected.")

    def test_02_country_where_population_density_less_50(self):
        db = DB()
        population_density = 50
        expected_country = "USA"

        with db:
            actual_country = db.get_country_where_population_density_less_given_value(population_density)
        for country in actual_country:
            self.assertEqual(country[0], expected_country,
                             "Incorrect country name with population density less {}. Actual country: {}. "
                             "Expected country: {}.".format(population_density, country[0], expected_country))

    def test_03_check_population_total_less_2billions(self):
        db = DB()
        expected_total_population = 2e9

        with db:
            populations = db.get_population_list_of_all_country()
        actual_total_population = reduce(lambda x, y: (x[0] + y[0],), populations)

        self.assertLess(actual_total_population[0], expected_total_population,
                        "Population total is greater than 2billions. "
                        "Actual total population: {}".format(actual_total_population[0]))

    def test_04_iframe(self):
        driver = WebDriver().get_driver()
        web_page = TryHtmlIframePage(driver)

        search_string = "Redmond"
        expected_suggestion = "redmond washington"
        expected_first_link = "bing.com/travelguide?q=Redmond"

        web_page.load()
        web_page.replace_given_word_in_editor("w3schools", "bing")
        web_page.click_run_button()
        web_page.switch_to_search_frame()
        web_page.fill_search_input(search_string)
        web_page.show_search_suggestions()
        actual_suggestions = web_page.get_search_suggestions_list()

        self.assertIn(expected_suggestion, actual_suggestions,
                      "Actual suggestions do not contains expected one.\nActual list: `{}`.\nExpected: `{}`."
                      .format(', '.join(actual_suggestions), expected_suggestion))

        web_page.click_given_suggestion(expected_suggestion)
        actual_links = web_page.get_search_result_links_list()

        self.assertEqual(actual_links[0], expected_first_link,
                         "Incorrect first link in the search result.\nActual link: {}.\nExpected link: {}."
                         "\nActual links list: {}".format(actual_links[0], expected_first_link, '\n'.join(actual_links)))

        driver.quit()
