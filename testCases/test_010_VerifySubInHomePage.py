import pytest
import os
import time
from selenium.webdriver.common.by import By
from pageObjects.HomePage import HomePage
from utilities.testProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_010_VerifySubInHomePage:
    baseUrl = ReadConfig.getApplicationURL()
    logger = LogGen.getLogger()

    def test_verify_sub_in_home_page(self,setup):
        self.logger.info("***test_010_VerifySubInHomePage started***")
        self.driver = setup
        self.logger.info("***Launching Application***")
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()

        self.hp = HomePage(self.driver)
        assert self.hp.HomePageExists(), "Home Page is not visible"
        self.hp.scroll_to_target(self.hp.foooter_xpath)
        assert self.hp.SubscriptionTextExists(),"Subscription text is not visible"
        self.hp.write_subscription_email('freddy777@gmail.com')
        self.hp.click_subcription_button()
        assert self.hp.SubscriptionSuccessAlertExists()