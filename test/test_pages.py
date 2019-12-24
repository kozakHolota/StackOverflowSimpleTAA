import allure
import pytest

class TestPages(object):
    """
    Test Definition Layer
    """
    @allure.title("Verify that StackOverflow main page shows correctly")
    @pytest.mark.regression
    @pytest.mark.test_main_page
    def test_main_page(self, main_page, username, password, github_username, github_password):
        assert main_page.stackoverflow_logo.is_displayed(), "StackOverflow Logo is not shown"
        assert main_page.login_link.is_displayed(), "Link to login for is not shown"
        assert main_page.sign_up_button.is_displayed(), "Sign Up button is not shown on the page"

    @allure.title("Verify that StackOverflow logins with correct credentials")
    @pytest.mark.regression
    @pytest.mark.test_login_process
    def test_login_process(self, main_page, username, password, github_username, github_password):
        login_page = main_page.click_on_login_link()

        assert login_page.stackoverflow_logo.is_displayed(), "StackOverflow Logo is not shown"
        assert login_page.google_login_button.is_displayed(), "Google signin button is not shown"
        assert login_page.facebook_login_button.is_displayed(), "Facebook signin button is not shown"
        assert login_page.username_field.is_displayed(), "Username input field is not shown"
        assert login_page.password_field.is_displayed(), "Password field is not shown"
        assert login_page.login_button.is_displayed(), "Login submit button is not shown"

        workspace_page = login_page.enter_login(username)\
            .enter_password(password)\
            .click_on_login_button()
        assert workspace_page.stackoverflow_logo.is_displayed(), "StackOverflow Logo is not shown"
        assert workspace_page.profile_button.is_displayed(), "Profile button is not displayed"
        assert workspace_page.inbox_button.is_displayed(), "Inbox button is not shown"
        assert workspace_page.achivements_button.is_displayed(), "Achivements button is not shown"
        assert workspace_page.help_button.is_displayed(), "Help button is not shown"
        assert workspace_page.user_menu.is_displayed(), "User menu is not shown"

    @allure.title("Verify that StackOverflow signup page shows correctly")
    @pytest.mark.regression
    @pytest.mark.test_signup_test
    def test_signup_test(self, main_page, username, password, github_username, github_password):
        signup_page = main_page.click_on_sign_up_button()
        assert signup_page.stackoverflow_logo.is_displayed(), "StackOverflow Logo is not shown"
        assert signup_page.google_login_button.is_displayed(), "Google signin button is not shown"
        assert signup_page.facebook_login_button.is_displayed(), "Facebook signin button is not shown"
        assert signup_page.username_field.is_displayed(), "Username input field is not shown"
        assert signup_page.password_field.is_displayed(), "Password field is not shown"
        assert signup_page.signup_button.is_displayed(), "Signup submit button is not shown"

    @allure.title("Verify that signup from GitHub with the correct credentials leads to the workspace page")
    @pytest.mark.regression
    @pytest.mark.test_github_signup
    def test_github_signup(self, main_page, username, password, github_username, github_password):
        github_login_page = main_page.click_on_sign_up_button().click_github_signup()

        assert github_login_page.username_field.is_displayed(), "Username input field is not shown"
        assert github_login_page.password_field.is_displayed(), "Password field is not shown"
        assert github_login_page.login_button.is_displayed(), "Login submit button is not shown"

        workspace_page = github_login_page.enter_login(github_username).enter_password(github_password).click_on_login_button().accept_signup()

        assert workspace_page.stackoverflow_logo.is_displayed(), "StackOverflow Logo is not shown"
        assert workspace_page.profile_button.is_displayed(), "Profile button is not displayed"
        assert workspace_page.inbox_button.is_displayed(), "Inbox button is not shown"
        assert workspace_page.achivements_button.is_displayed(), "Achivements button is not shown"
        assert workspace_page.help_button.is_displayed(), "Help button is not shown"
        assert workspace_page.user_menu.is_displayed(), "User menu is not shown"

    @allure.title("Verify that StackOverFlow search finds patterns which is present on the page")
    @pytest.mark.regression
    @pytest.mark.test_search_existing
    def test_search_existing(self, main_page, username, password, github_username, github_password):
        search_pattern = "SQL query"
        search_results = main_page\
            .click_on_login_link()\
            .enter_login(username)\
            .enter_password(password)\
            .click_on_login_button()\
            .search(search_pattern)\
            .search_results

        assert len(search_results), f"Search results for query '{search_pattern}' are not shown"