import pytest
import os
import time
from pageObjects.HomePage import HomePage
from pageObjects.ContactUsPage import ContactUsPage
from utilities.testProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_006_ContactUsForm:
    baseUrl = ReadConfig.getApplicationURL()
    logger = LogGen.getLogger()

    def test_contact_us(self,setup):
        self.logger.info("***test_006_ContactUsForm started***")
        self.driver = setup
        self.logger.info("***Launching Application***")
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()

        self.hp = HomePage(self.driver)
        assert self.hp.HomePageExists(), "Home page is visible"
        self.logger.info("***Clicking on Contact Us link***")
        self.hp.click_contact()

        self.contact = ContactUsPage(self.driver)
        assert self.contact.GetInTouchExists(),"Get in touch is not visible"
        self.logger.info("***Filling out the form***")
        self.contact.write_name('Freddy')
        self.contact.write_email('freddy777@gmail.com')
        self.contact.write_subject('Automation')
        self.contact.write_message('Hello there')
        self.logger.info("***Uploading a file***")
        self.contact.upload_file(r"C:\Users\freda\PycharmProjects\OpencartV1\sample.TXT")
        self.logger.info("***Submitting the form***")
        self.contact.click_submit()
        self.contact.click_alert()
        assert self.contact.SuccessMessageDisplayed(),"Success message is not visible"

        self.hp.ensure_home()
        self.hp.close_home_ad()
        self.hp.click_home()
        assert self.hp.HomePageExists(),"Home page is visible"




