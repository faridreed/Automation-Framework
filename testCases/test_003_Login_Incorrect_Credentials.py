import pytest
import os
import time
from pageObjects.HomePage import HomePage
from pageObjects.Login_Reg_Page import Login_Reg_Page
from pageObjects.RegistrationPage import RegistrationPage
from utilities.testProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_003_Incorrect_Login:
    baseUrl = ReadConfig.getApplicationURL()
    logger = LogGen.getLogger()

    def test_incorrect_login(self,setup):
        self.logger.info("***test_001_AccountRegistration started***")
        self.driver = setup
        self.logger.info("***Launching Application***")
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()

        self.hp = HomePage(self.driver)
        self.logger.info("***Checking that Home Page exists***")
        self.hp.HomePageExists()
        self.logger.info("***Clicking on Login button***")
        self.hp.click_reg_login()

        self.lp = Login_Reg_Page(self.driver)
        self.lp.LoginExists()
        self.logger.info("***Entering wrong Email***")
        self.lp.login_email('fsdfsdd@gmail.com')
        self.logger.info("***Entering wrong Password***")
        self.lp.login_password('sdfsdfg')
        self.lp.click_login_button()
        self.logger.info("***Checking if incorrent email or password text is displayed***")
        self.lp.IncorrectEmailOrPasswordVisible()