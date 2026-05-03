# Oscar Avina
# 05/2/2026
# Module 7.2 Assignment
# This is a test for the city_country function

import unittest
from city_functions import city_country

class TestCityCountry(unittest.TestCase): # test the city_country function
  def test_city_country(self):
    city_and_country_var = city_country("Santiago", "Chile")
    self.assertEqual(city_and_country_var, "Santiago, Chile") # testing to see if the test variable is equal to the expected value

if __name__ == "__main__":
  unittest.main()