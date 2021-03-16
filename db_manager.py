import os
import sqlite3


class DB:
    def __init__(self):
        self.db_file = "{}/static_data/PopulationDB.db".format(os.path.dirname(os.path.realpath(__file__)))
        self.connection = None

    def __enter__(self):
        self.connection = sqlite3.connect(self.db_file)

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()

    def get_country_where_population_density_less_given_value(self, value):
        cursor = self.connection.cursor()
        cursor.execute("SELECT country FROM Countries WHERE population / area < {value}".format(value=value))

        return cursor.fetchall()

    def get_population_list_of_all_country(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT population FROM Countries")

        return cursor.fetchall()
