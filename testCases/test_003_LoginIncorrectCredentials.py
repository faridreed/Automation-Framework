import pytest
import os
import time
from pageObjects.HomePage import HomePage
from pageObjects.Login_Reg_Page import Login_Reg_Page
from pageObjects.RegistrationPage import RegistrationPage
from utilities.testProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_003_IncorrectLogin:
    baseUrl = ReadConfig.getApplicationURL()
    logger = LogGen.getLogger()

    def test_incorrect_login(self,setup):
        self.logger.info("***test_003_IncorrectLogin started***")
        self.driver = setup
        self.logger.info("***Launching Application***")
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()

        self.hp = HomePage(self.driver)
        self.logger.info("***Checking that Home Page exists***")
        assert self.hp.HomePageExists(),"Home page is not visible"
        self.logger.info("***Clicking on Login button***")
        self.hp.click_reg_login()

        self.lp = Login_Reg_Page(self.driver)
        assert self.lp.LoginExists(),"Login text is not visible"
        self.logger.info("***Entering wrong Email***")
        self.lp.login_email('fsdfsdd@gmail.com')
        self.logger.info("***Entering wrong Password***")
        self.lp.login_password('sdfsdfg')
        self.lp.click_login_button()
        self.logger.info("***Checking if incorrent email or password text is displayed***")
        assert self.lp.IncorrectEmailOrPasswordVisible(),"Incorrect email or password text is not visible"