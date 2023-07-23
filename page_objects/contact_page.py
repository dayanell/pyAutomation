from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from page_objects.base_page import BasePage


class ContactPage(BasePage):
    __url = "https://www.remedyproduct.com/contact-us"
    __contact_us_header_field = (By.XPATH, "//h4[text()='Contact us']")
    __customer_name_field = (By.ID, "Contact-Name")
    __company_name_field = (By.NAME, "Contact-Name-2")
    __email_field = (By.CSS_SELECTOR, "[placeholder='johnsmith@info.com']")
    __hear_about_us_field = (By.XPATH, "//*[@name='Contact-Email-2']")
    __message_field = (By.CSS_SELECTOR, "#field")
    __send_message_button = (By.CSS_SELECTOR, "[value='Send Message']")

    def __init__(self, driver: WebDriver):
        super().__int__(driver)

    @property
    def expected_url(self):
        return self.__url

    def fill_contact_form(self, username, company, email, about_us, message):
        self._type(self.__customer_name_field, username)
        self._type(self.__company_name_field, company)
        self._type(self.__email_field, email)
        self._type(self.__hear_about_us_field, about_us)
        self._type(self.__message_field, message)

    def contact_header_text(self) -> str:
        self._is_displayed(self.__contact_us_header_field)
        return self._get_text(self.__contact_us_header_field)

    def scroll_page_to_contact_form(self):
        element = self._find(self.__contact_us_header_field)
        self._driver.execute_script("arguments[0].scrollIntoView();", element)
    def is_displayed_send_message_button(self) -> bool:
        return self._is_displayed(self.__send_message_button)
