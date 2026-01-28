import pytest
import os
import time
from pageObjects.HomePage import HomePage
from pageObjects.Login_Reg_Page import Login_Reg_Page
from utilities.testProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_002_Correct_Login:
    baseUrl = ReadConfig.getApplicationURL()
    logger = LogGen.getLogger()

    def test_correct_login(self,setup):
        self.logger.info("***test_002_CorrectLogin started***")
        self.driver = setup
        self.logger.info("***Launching Application***")
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()

        self.hp = HomePage(self.driver)
        assert self.hp.HomePageExists(),"Home page is not visible"
        self.hp.click_reg_login()

        self.lp = Login_Reg_Page(self.driver)
        assert self.lp.LoginExists(),"Login text is not visible"
        self.lp.login_email('freddy0004@gmail.com')
        self.lp.login_password('freddy777')
        self.lp.click_login_button()

        assert self.hp.LoggedInExists(),"Logged in text is not visible"
        self.hp.ensure_home()
        self.hp.delete_account()

        if "/delete_account" not in self.driver.current_url:
            self.driver.get(self.driver.current_url + "/delete_account")

        time.sleep(2)

        assert self.hp.account_deleted_confirmation(),"Account not deleted"

