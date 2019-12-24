import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class UserWorkSpacePage(object):
    """
        Test Adaptation Layer
    """
    def __init__(self, web_driver: WebDriver):
        # Initialize web driver
        self.web_driver = web_driver

        self.profile_button = WebDriverWait(self.web_driver, 25)\
            .until(
            expected_conditions.visibility_of_element_located((By.CLASS_NAME, "my-profile"))
        )
        self.stackoverflow_logo = self.web_driver.find_element_by_css_selector(".-img._glyph")
        self.inbox_button = self.web_driver.find_element_by_class_name("js-inbox-button")
        self.achivements_button = self.web_driver.find_element_by_class_name("js-achievements-button")
        self.help_button = self.web_driver.find_element_by_class_name("js-help-button")
        self.user_menu = self.web_driver.find_element_by_class_name("js-site-switcher-button")
        self.search_field = self.web_driver.find_element_by_name("q")

    @property
    def search_results(self):
        return self.web_driver.find_elements_by_css_selector(".search-result")

    @allure.step("Searching for the next pattern: {1}")
    def search(self, request):
        self.search_field.send_keys(request)
        ActionChains(self.web_driver).send_keys(Keys.ENTER).perform()
        return self