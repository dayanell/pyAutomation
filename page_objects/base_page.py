from selenium.common import NoSuchElementException
from selenium.webdriver.remote.webdriver import WebDriver, WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:
    def __int__(self, driver: WebDriver):
        self._driver = driver

    @property
    def current_url(self):
        return self._driver.current_url

    def _open_browser_url(self, url):
        self._driver.get(url)

    def _find(self, locator) -> WebElement:
        return self._driver.find_element(*locator)

    def _type(self, locator, text, timeout=5):
        self._wait_element_visibility(locator, timeout)
        self._find(locator).send_keys(text)

    def _click(self, locator, timeout=5):
        self._wait_element_visibility(locator, timeout)
        self._find(locator).click()

    def _wait_element_visibility(self, locator, timeout=3):
        wait = WebDriverWait(self._driver, timeout)
        wait.until(ec.presence_of_element_located(locator))

    def _is_displayed(self, locator) -> bool:

        try:
            return self._find(locator).is_displayed()
        except NoSuchElementException:
            return False

    def _get_text(self, locator, timeout=5) -> str:
        self._wait_element_visibility(locator, timeout)
        return self._find(locator).text
