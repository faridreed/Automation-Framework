import os
import datetime
import os.path
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.core import driver
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.service import Service as FirefoxService


@pytest.fixture
def setup(request, browser):
    headless = request.config.getoption("--headless")

    if browser == "chrome":
        opts = ChromeOptions()
        if headless:
            opts.add_argument("--headless=new")
        driver = webdriver.Chrome(options=opts)

    elif browser == "edge":
        opts = EdgeOptions()
        if headless:
            opts.add_argument("--headless=new")
        driver = webdriver.Edge(options=opts)

    else:
        opts = FirefoxOptions()
        if headless:
            opts.add_argument("-headless")
        driver = webdriver.Firefox(options=opts)

    driver.maximize_window()
    yield driver
    driver.quit()

def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="firefox",
        help="Browser to run tests on: chrome, edge, firefox"
    )
    parser.addoption(
        "--headless",
        action="store_true",
        default=False,
        help="Run browsers in headless mode"
    )



@pytest.fixture
def browser(request):            #Returning the Browser value to Setup method
    return request.config.getoption("--browser")

##### Generating HTML Reports #####

def pytest_configure(config):
    # Set report output path
    reports_dir = os.path.join(os.getcwd(), "reports")
    os.makedirs(reports_dir, exist_ok=True)

    filename = datetime.datetime.now().strftime("%d-%m-%Y_%H-%M-%S") + ".html"
    config.option.htmlpath = os.path.join(reports_dir, filename)

    # Modify HTML environment metadata
    html = getattr(config, "_html", None)

    if html:
        # Remove unwanted metadata
        html.environment = [
            item for item in html.environment
            if item[0] not in ("JAVA_HOME", "Plugins")
        ]

        # Add custom metadata
        html.environment.append(("Project Name", "Opencart"))
        html.environment.append(("Module", "Customer Registration"))
        html.environment.append(("Tester", "Farid"))


# # Hook for adding environment info to HTML Report
# def pytest_configure(config):
#     config._metadata['Project Name'] = 'Opencart'
#     config._metadata['Module Name'] = 'Customer Registration'
#     config._metadata['Tester'] = 'Farid'
#
# # Hook for Delete/Modify info to HTML Report
# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
#     metadata.pop('JAVA_HOME', None)
#     metadata.pop('Plugins', None)
#
# # Specifying report folder location and save report with timestamp
# @pytest.hookimpl(tryfirst=True)
# def pytest_configure(config):
#     config.option.htmlpath = os.path.abspath(os.curdir) + "\\reports\\" + datetime.datetime.now().strftime("%d-%m-%Y %H-%M-%S") + ".html"
#
