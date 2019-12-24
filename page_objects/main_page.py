from selenium.webdriver.remote.webdriver import WebDriver
import allure
from page_objects.login_page import LoginPage
from page_objects.signup_page import SignUpPage


class MainPage(object):
    """
    Test Adaptation Layer
    """
    def __init__(self, web_driver: WebDriver):
        # Initialize web driver
        self.web_driver = web_driver
        self.web_driver.maximize_window()
        self.web_driver.get("https://stackoverflow.com")

        # Instantiating web elements
        self.stackoverflow_logo = self.web_driver.find_element_by_css_selector(".-img._glyph")
        self.login_link = self.web_driver.find_element_by_css_selector(".login-link.s-btn[href*=login]")
        self.sign_up_button = self.web_driver.find_element_by_css_selector(".login-link.s-btn[href*=signup]")


    @allure.step("Click on the Sign Up button")
    def click_on_sign_up_button(self):
        self.sign_up_button.click()
        allure.attach(self.web_driver.get_screenshot_as_png(), attachment_type=allure.attachment_type.PNG)
        return SignUpPage(self.web_driver)

    @allure.step("Click on the Sign In button")
    def click_on_login_link(self):
        self.login_link.click()
        allure.attach(self.web_driver.get_screenshot_as_png(), attachment_type=allure.attachment_type.PNG)
        return LoginPage(self.web_driver)