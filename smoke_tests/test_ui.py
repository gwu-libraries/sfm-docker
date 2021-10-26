import unittest
from splinter import Browser
import pyvirtualdisplay


class UiSmokeTest(unittest.TestCase):
    def test_home(self):
        with pyvirtualdisplay.Display():
            browser = Browser()
            browser.visit("http://ui:8080")
            self.assertTrue(browser.find_by_text("Social Feed Manager"))

    def test_login(self):
        with pyvirtualdisplay.Display():
            browser = Browser()
            browser.visit("http://ui:8080/accounts/login/")
            browser.fill("login", "testuser")
            browser.fill("password", "password")
            browser.find_by_css(".btn-primary").click()
            self.assertTrue(browser.is_text_present("Successfully signed in as testuser.", wait_time=1))

    def test_admin_login(self):
        with pyvirtualdisplay.Display():
            browser = Browser()
            browser.visit("http://ui:8080/admin/")
            self.assertTrue(browser.find_by_text("Django administration"))
            browser.fill("username", "sfmadmin")
            browser.fill("password", "password")
            browser.find_by_value("Log in").click()
            self.assertTrue("Welcome" in browser.html)
