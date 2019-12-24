import importlib
from functools import wraps

import pytest
import yaml
from page_objects.main_page import MainPage

"""
Test Execution Layer
"""


class Config(object):
    webdrivers = {}
    browsers = []
    current_browser = None
    brw = None


def pytest_addoption(parser):
    parser.addoption("--conf",
                     action='store',
                     help="Path to the environment configuration")


@pytest.fixture(scope='session', autouse=True)
def init_drivers(request):
    config = None
    with open(request.config.getoption("--conf")) as yaml_file:
        config = yaml.load(yaml_file)

    Config.browsers = config["browsers"]

    def _get_browser(browser_name):
        mng_name = ""
        if browser_name == "Chrome":
            mng_name = "ChromeDriverManager"
        elif browser_name == "Firefox":
            mng_name = "GeckoDriverManager"
        elif browser_name == "Ie":
            mng_name = "IEDriverManager"

        Config.webdrivers[browser_name] = {
            "webdriver": getattr(importlib.import_module("selenium.webdriver"), browser_name),
            "wedriver_manager": getattr(importlib.import_module(f"webdriver_manager.{browser_name.lower()}"),
                                        mng_name)}

    for br in Config.browsers:
        _get_browser(br)


def get_browser():
    for i in Config.browsers:
        yield i


def get_main_page(browser):
    print(Config.webdrivers)
    Config.current_browser = Config.webdrivers[browser]["webdriver"](
        executable_path=Config.webdrivers[browser]["wedriver_manager"]().install())
    return MainPage(Config.current_browser)

@pytest.fixture
def main_page(request):
    next_brw = None
    if not Config.brw:
        Config.brw = get_browser()

    try:
        next_brw = Config.brw.__next__()
    except StopIteration:
        Config.brw = get_browser()
        next_brw = Config.brw.__next__()

    def fin():
        if Config.current_browser and getattr(Config.current_browser, "quit"):
            Config.current_browser.quit()

    request.addfinalizer(fin)

    return get_main_page(next_brw)


def pytest_generate_tests(metafunc):
    config = None
    with open(metafunc.config.getoption("--conf")) as yaml_file:
        config = yaml.load(yaml_file)
    params = tuple(map(lambda browser: (config["login"],
                                        config["password"],
                                        config["github_login"],
                                        config["github_password"]),
                       config["browsers"]
                       )
                   )

    metafunc.parametrize("username, password, github_username, github_password", params)
