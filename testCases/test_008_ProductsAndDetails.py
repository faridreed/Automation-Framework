import pytest
import os
import time
from pageObjects.HomePage import HomePage
from pageObjects.ProductsPage import ProductsPage
from utilities.testProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_008_ProductsAndDetails:
    baseUrl = ReadConfig.getApplicationURL()
    logger = LogGen.getLogger()

    def test_products_and_details(self,setup):
        self.logger.info("***test_008_ProductsAndDetails started***")
        self.driver = setup
        self.logger.info("***Launching Application***")
        self.hp = HomePage(self.driver)
        self.driver.get(self.baseUrl)
        self.hp.clean_google_ads()
        self.driver.maximize_window()


        assert self.hp.HomePageExists(),"Home Page is not visible"
        self.hp.click_products()
        self.hp.clean_google_ads()

        if "/products" not in self.driver.current_url:
            # Vignette hijacked navigation, force the correct page
            self.driver.get(self.baseUrl + "/products")
            self.hp.clean_google_ads()

        self.pp = ProductsPage(self.driver)
        assert self.pp.AllProductsExists(),"All products page not loaded"
        assert self.pp.ProductsListExists(),"Products list is not visible"
        self.pp.click_first_product()
        assert self.pp.ProductDetailsExists(),"Product details are not visible"