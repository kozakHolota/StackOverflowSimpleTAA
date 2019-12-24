import allure
from selenium.webdriver.remote.webdriver import WebDriver

from page_objects.github_login_page import GitHubLoginPage


class SignUpPage(object):
    """
        Test Adaptation Layer
    """
    def __init__(self, web_driver: WebDriver):
        # Initialize web driver
        self.web_driver = web_driver
        self.stackoverflow_logo = self.web_driver.find_element_by_css_selector(".-img._glyph")
        self.google_login_button = self.web_driver.find_element_by_css_selector('[data-provider=google]')
        self.facebook_login_button = self.web_driver.find_element_by_css_selector('[data-provider=facebook]')
        self.github_login_button = self.web_driver.find_element_by_css_selector('[data-provider=github]')
        self.display_name = self.web_driver.find_element_by_id("display-name")
        self.product_updates = self.web_driver.find_element_by_id("opt-in")
        self.username_field = self.web_driver.find_element_by_id("email")
        self.password_field = self.web_driver.find_element_by_id("password")
        self.signup_button = self.web_driver.find_element_by_id("submit-button")

    @allure.step("Signing up from GitHub")
    def click_github_signup(self):
        self.github_login_button.click()
        return GitHubLoginPage(self.web_driver)