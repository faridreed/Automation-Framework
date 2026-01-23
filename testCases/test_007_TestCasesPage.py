import pytest
import os
import time
from pageObjects.HomePage import HomePage
from pageObjects.TestCasesPage import TestCasesPage
from utilities.testProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_007_TestCasesPage:
    baseUrl = ReadConfig.getApplicationURL()
    logger = LogGen.getLogger()

    def test_correct_login(self,setup):
        self.logger.info("***test_007_TestCasesPage started***")
        self.driver = setup
        self.logger.info("***Launching Application***")

        self.hp = HomePage(self.driver)
        self.driver.get(self.baseUrl)
        self.hp.clean_google_ads()
        self.driver.maximize_window()


        assert self.hp.HomePageExists(),"Home Page does not exits"
        self.hp.click_tcases()
        self.hp.clean_google_ads()

        if "/test_cases" not in self.driver.current_url:
            # Vignette hijacked navigation, force the correct page
            self.driver.get(self.baseUrl + "/test_cases")
            self.hp.clean_google_ads()


        self.tcases = TestCasesPage(self.driver)
        assert self.tcases.TestCasesExists(),"Test cases text does not exist"