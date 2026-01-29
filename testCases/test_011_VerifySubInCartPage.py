import pytest
import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from pageObjects.HomePage import HomePage
from utilities.testProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_011_VerifySubInCartPage:
    baseUrl = ReadConfig.getApplicationURL()
    logger = LogGen.getLogger()

    def test_verify_sub_in_cart_page(self,setup):
        self.logger.info("***test_011_VerifySubInCartPage started***")
        self.driver = setup
        self.logger.info("***Launching Application***")
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()

        self.hp = HomePage(self.driver)
        assert self.hp.HomePageExists(), "Home Page is not visible"
        self.hp.click_cart()
        self.hp.scroll_to_bottom()
        assert self.hp.SubscriptionTextExists()
        self.hp.write_subscription_email('freddy006@gmail.com')
        self.hp.click_subcription_button()
        assert self.hp.SubscriptionSuccessAlertExists(), "Subscription Alert is not visible"


