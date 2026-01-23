import pytest
import os
import time
from pageObjects.HomePage import HomePage
from pageObjects.Login_Reg_Page import Login_Reg_Page
from pageObjects.RegistrationPage import RegistrationPage
from utilities.testProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_005_RegisterWithExistingEmail:
    baseUrl = ReadConfig.getApplicationURL()
    logger = LogGen.getLogger()

    def test_register_with_existing_email(self,setup):
        self.logger.info("***test_005_RegisterWithExistingEmail started***")
        self.driver = setup
        self.logger.info("***Launching Application***")
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()

        self.hp = HomePage(self.driver)
        assert self.hp.HomePageExists(),"Home Page is not visible"
        self.hp.click_reg_login()

        self.lp = Login_Reg_Page(self.driver)
        assert self.lp.NewUserSignUpExists(),"New User Signup is not visible"
        self.lp.register_name('Freddy')
        self.lp.register_email('freddy777@gmail.com')
        self.lp.click_reg_button()
        assert self.lp.EmailAlreadyExistsVisible(),"Email already exist text is not visible"