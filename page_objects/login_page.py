from selenium.webdriver.remote.webdriver import WebDriver
import allure

from page_objects.user_workspace_page import UserWorkSpacePage


class LoginPage(object):
    """
        Test Adaptation Layer
    """
    def __init__(self, web_driver: WebDriver):
        # Initialize web driver
        self.web_driver = web_driver

        self.stackoverflow_logo = self.web_driver.find_element_by_css_selector(".-img._glyph")
        self.google_login_button = self.web_driver.find_element_by_css_selector('[data-provider=google]')
        self.facebook_login_button = self.web_driver.find_element_by_css_selector('[data-provider=facebook]')
        self.username_field = self.web_driver.find_element_by_id("email")
        self.password_field = self.web_driver.find_element_by_id("password")
        self.login_button = self.web_driver.find_element_by_id("submit-button")

    @allure.step("Enter username {1}")
    def enter_login(self, username):
        self.username_field.send_keys(username)
        allure.attach(self.web_driver.get_screenshot_as_png(), attachment_type=allure.attachment_type.PNG)
        return self

    @allure.step("Filling in the password")
    def enter_password(self, password):
        self.password_field.send_keys(password)
        allure.attach(self.web_driver.get_screenshot_as_png(), attachment_type=allure.attachment_type.PNG)
        return self

    @allure.step("Clicking on the Login Button")
    def click_on_login_button(self):
        self.login_button.click()
        allure.attach(self.web_driver.get_screenshot_as_png(), attachment_type=allure.attachment_type.PNG)
        return UserWorkSpacePage(self.web_driver)
