import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from page_objects.user_workspace_page import UserWorkSpacePage
from selenium.webdriver.remote.webdriver import WebDriver


class GitHubLoginPage(object):
    """
        Test Adaptation Layer
    """
    def __init__(self, web_driver: WebDriver):
        # Initialize web driver
        self.web_driver = web_driver
        self.username_field = self.web_driver.find_element_by_id("login_field")
        self.password_field = self.web_driver.find_element_by_id("password")
        self.login_button = self.web_driver.find_element_by_name("commit")

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
        return self

    @allure.step("Accepting signup")
    def accept_signup(self):
        try:
            WebDriverWait(self.web_driver, 15).until(expected_conditions.element_to_be_clickable((By.ID, 'js-oauth-authorize-btn'))).click()
        finally:
            return UserWorkSpacePage(self.web_driver)