import pytest
import os
import time
from pageObjects.HomePage import HomePage
from pageObjects.Login_Reg_Page import Login_Reg_Page
from pageObjects.RegistrationPage import RegistrationPage
from utilities.testProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_002_Correct_Login:
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
        self.lp.LoginExists()
        self.lp.login_email('freddy777@gmail.com')
        self.lp.login_password('freddy777')
        self.lp.click_login_button()

        self.hp.LoggedInExists()
        self.hp.delete_account()
        self.hp.account_deleted_confirmation()

