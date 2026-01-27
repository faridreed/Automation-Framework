import pytest
import os
import time
from selenium.webdriver.common.by import By
from pageObjects.HomePage import HomePage
from pageObjects.ProductsPage import ProductsPage
from pageObjects.CartPage import CartPage
from utilities.testProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_013_VerifyProductQuantityInCart:
    baseUrl = ReadConfig.getApplicationURL()
    logger = LogGen.getLogger()

    def test_verify_product_quantity_in_cart(self,setup):
        self.logger.info("***test_013_VerifyProductQuantityInCart started***")
        self.driver = setup
        self.logger.info("***Launching Application***")
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()

        self.hp = HomePage(self.driver)
        assert self.hp.HomePageExists(), "Home Page is not visible"
        self.hp.clean_google_ads()
        self.hp.scroll_to_target(self.hp.lnk_first_product_xpath)
        self.hp.click(self.hp.lnk_first_product_xpath)
        self.hp.clean_google_ads()

        if 'product_details/1' not in self.driver.current_url:
            self.driver.get(self.driver.current_url + 'product_details/1')

        self.pp = ProductsPage(self.driver)
        assert self.pp.ProductDetailsExists()
        self.pp.enter_product_quantity('4')
        self.pp.click_add_to_cart()
        self.pp.click_view_cart()

        self.cart_page = CartPage(self.driver)
        assert self.cart_page.verify_quantity('4'),"The correct quantity is not displayed"