# -*- coding: utf-8 -*-
# The above is required due to a non-standard character I can't find somewhere.
# It's embarrassing, but it has to stay. It's probably because I used UTF-8.

import unittest
import uptake
import HTMLTestRunner
from selenium import webdriver

class UptakeNavTest(unittest.TestCase):
    """A pretty basic test for navigating the Uptake homepage."""

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://uptake.com/")

    def test_navigation_test(self):
        """
        This test will determine that navigation between the Home, Products, and
        contacts pages works properly and contains asserted keywords in the titles of
        those pages. An HTML report is then generated at the end of the test suite
        that reports success or failure.
        """
        #Loads the Uptake home page.
        uptake_home = uptake.UptakeHome(self.driver)
        #Checks if the word "Analytics" is in the title.
        assert uptake_home.home_title_matches(), "Unexpected title contents"
        #Navigates to the Products page.
        uptake_home.click_products()
        #Checks if the title of the page containts the word "Products"
        uptake_home.product_title_matches(), "Unexpected title contents"
        #Clicks Contact button
        uptake_home.click_contact()
        #Checks if the title of the page containts "Contact"
        uptake_home.contact_title_matches(), "Unexpected title contents"

    def tearDown(self):
        self.driver.close()

# When running test, output it to an html file to take advantage of the runner.
# Example: python uptaketest.py > Result.html in a terminal or powershell window.

if __name__ == "__main__":
    HTMLTestRunner.main()
