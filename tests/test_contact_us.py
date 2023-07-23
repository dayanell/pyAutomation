import pytest
from page_objects.contact_page import ContactPage
from page_objects.home_page import HomePage
from tests.test_base import TestBase


class TestContactFormScenarios:

    @pytest.mark.smoke
    @pytest.mark.contact_form
    @pytest.mark.parametrize("name, company, email, hear_about, message",
                             [("John Doe", "Remedy Customer", "johndoe@remedy.sample", "LinkedIn",
                               "I am writing this message to express my deepest gratitude and heartfelt appreciation "
                               "for the incredible work your team has done"),
                              ("Jane Doe", "Remedy Client", "janedoe@remedy.sample", "Google",
                               "The level of professionalism, reliability, and expertise your company displays is "
                               "truly admirable")])
    def test_successful_contact_form_submission(self, driver, name, company, email, hear_about, message):
        home_page = HomePage(driver)
        contact_page = ContactPage(driver)
        test_base = TestBase()
        logger = test_base.get_logger()

        # Test steps
        home_page.open_browser()
        logger.info("Test case starting...")
        home_page.click_contact_us()
        contact_page.scroll_page_to_contact_form()
        assert contact_page.contact_header_text() == "Contact us", logger.error("Header text does not match 'Contact us'")
        assert contact_page.current_url == contact_page.expected_url, logger.error("The current url is incorrect")
        contact_page.fill_contact_form(name, company, email, hear_about, message)
        assert contact_page.is_displayed_send_message_button() == True, logger.error("Button Send Message is not Displayed")

    @pytest.mark.contact_form
    def test_contact_form_with_invalid_inputs(self, driver):
        home_page = HomePage(driver)
        contact_page = ContactPage(driver)
        test_base = TestBase()
        logger = test_base.get_logger()

        # Test steps
        home_page.open_browser()
        logger.info("Test case starting...")
        home_page.click_contact_us()
        contact_page.scroll_page_to_contact_form()
        assert contact_page.contact_header_text() == "Contact us", logger.error("Header text does not match 'Contact us'")
        assert contact_page.current_url == contact_page.expected_url, logger.error("The current url is incorrect")
        assert contact_page.is_displayed_send_message_button() == False, logger.error("Button Send Message is not Displayed")
        # Fill the form with invalid inputs


        # Creating a list for the negative path validations but is not completed
        # assert contact_page.is_name_error_displayed(), logger.error("Name error message is not displayed")
        # assert contact_page.is_company_error_displayed(), logger.error("Company error message is not displayed")
        # assert contact_page.is_email_error_displayed(), logger.error("Email error message is not displayed")
        # assert contact_page.is_hear_about_error_displayed(), logger.error("Hear About error message is not displayed")
        # assert contact_page.is_message_error_displayed(), logger.error("Message error message is not displayed")
        # assert not contact_page.is_send_message_button_enabled(), logger.error("Send Message button is enabled with invalid inputs")
