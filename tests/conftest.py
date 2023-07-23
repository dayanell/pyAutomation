import time
from datetime import datetime
from selenium import webdriver
import pytest
import os

# Default value for web_driver
web_driver = None


@pytest.fixture
def driver(request):
    global web_driver
    browser = request.config.getoption("--browser")
    if browser == "chrome":
        web_driver = webdriver.Chrome()
    elif browser == "firefox":
        web_driver = webdriver.Firefox()
    else:
        raise TypeError(f"The browser '{browser}' is not supported. Please select either 'chrome' or 'firefox'.")

    web_driver.maximize_window()
    yield web_driver
    web_driver.quit()


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="my option: chrome or firefox"
    )


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == 'call' and rep.failed:
        now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        driver = item.funcargs.get('driver')  # Get the 'driver' fixture instance from the test function arguments
        if driver:
            # Define the screenshot directory path inside 'reports' directory
            screenshots_dir = os.path.join(os.path.dirname(__file__), "reports", "../reports/screenshots")
            if not os.path.exists(screenshots_dir):
                os.makedirs(screenshots_dir)

            # Save the screenshot at the point of failure
            file_name = f"fail_{now}.png"
            file_path = os.path.join(screenshots_dir, file_name)
            driver.save_screenshot(file_path)

            # Update the file path to be relative to the 'reports' directory in the HTML report
            relative_file_path = os.path.relpath(file_path, start=os.path.join(os.path.dirname(__file__), "reports"))

            pytest_html = item.config.pluginmanager.getplugin('html')
            html = f'<div><img src="{relative_file_path}" alt="screenshot" style="width:304px;height:228px;" ' \
                   f'onclick="window.open(this.src)" align="right"/></div>'
            extra = getattr(rep, 'extra', [])
            extra.append(pytest_html.extras.html(html))
            rep.extra = extra


def _capture_screenshot(name: str):
    global web_driver
    time.sleep(10)
    web_driver.get_screenshot_as_file(name)
