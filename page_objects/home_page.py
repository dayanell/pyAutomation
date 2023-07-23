from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from page_objects.base_page import BasePage


class HomePage(BasePage):
    __url = "https://www.remedyproduct.com/"
    __contact_button = (By.XPATH, "//div[text()='Contact Us']")

    def __init__(self, driver: WebDriver):
        super().__int__(driver)

    def open_browser(self):
        self._open_browser_url(self.__url)

    def click_contact_us(self):
        self._click(self.__contact_button)

