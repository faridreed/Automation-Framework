import pytest
import os
import time
from pageObjects.HomePage import HomePage
from pageObjects.Login_Reg_Page import Login_Reg_Page
from pageObjects.RegistrationPage import RegistrationPage
from utilities.testProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_004_Logout_User:
    baseUrl = ReadConfig.getApplicationURL()
    logger = LogGen.getLogger()

    def test_logout_user(self,setup):
        self.logger.info("***test_004_LogoutUser started***")
        self.driver = setup
        self.logger.info("***Launching Application***")
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()

        self.hp = HomePage(self.driver)
        assert self.hp.HomePageExists(),"Home Page is not visible"
        self.hp.click_reg_login()

        self.lp = Login_Reg_Page(self.driver)
        assert self.lp.LoginExists(),"Login text is not visible"
        self.lp.login_email('freddy777@gmail.com')
        self.lp.login_password('freddy777')
        self.lp.click_login_button()

        assert self.hp.LoggedInExists(),"Logged in text is not visible"
        self.hp.click_logout()
        assert self.lp.LoginExists(),"Login text is not visible"