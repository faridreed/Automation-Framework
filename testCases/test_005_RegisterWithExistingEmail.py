import pytest
import os
import time
from pageObjects.HomePage import HomePage
from pageObjects.Login_Reg_Page import Login_Reg_Page
from pageObjects.RegistrationPage import RegistrationPage
from utilities.testProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_005_Register_With_Existing_Email:
    baseUrl = ReadConfig.getApplicationURL()
    logger = LogGen.getLogger()

    def test_correct_login(self,setup):
        self.logger.info("***test_001_AccountRegistration started***")
        self.driver = setup
        self.logger.info("***Launching Application***")
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()

        self.hp = HomePage(self.driver)
        self.hp.HomePageExists()
        self.hp.click_reg_login()

        self.lp = Login_Reg_Page(self.driver)
        self.lp.NewUserSignUpExists()
        self.lp.register_name('Freddy')
        self.lp.register_email('freddy777@gmail.com')
        self.lp.click_reg_button()
        self.lp.EmailAlreadyExistsVisible()