# -*- coding: utf-8 -*-
# The above is required due to a non-standard character I can't find somewhere.
# It's embarrassing, but it has to stay. It's probably because I used UTF-8.


class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver


class UptakeHome(BasePage):

    def home_title_matches(self):
        """Verifies that the hardcoded text "Analytics" appears in page title"""
        return "Analytics" in self.driver.title

    def click_products(self):
        """Triggers navigation to Products page"""
        # I tried to add another layer of Page Objects here, but I also really
        # wanted to use XPATHing and couldn't get it isolate the XPATH locator
        # in a dedicated file.
        element = self.driver.find_element_by_xpath("/html/body/header/div[1]/nav/a[2]")
        element.click()

    def product_title_matches(self):
        """Verifies that the hardcoded text "Products" appears in page title"""
        return "Products" in self.driver.title

    def click_contact(self):
        """Triggers navigation to Contact page"""
        element = self.driver.find_element_by_xpath("/html/body/div[1]/div/button")
        element.click()

    def contact_title_matches(self):
        """Verifies that the hardcoded text "Contact" appears in page title"""
        return "Contact" in self.driver.title
