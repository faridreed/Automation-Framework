import pytest
import os
import time
from selenium.webdriver.common.by import By
from pageObjects.HomePage import HomePage
from pageObjects.ProductsPage import ProductsPage
from utilities.testProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_009_SearchProduct:
    baseUrl = ReadConfig.getApplicationURL()
    logger = LogGen.getLogger()

    def test_search_product(self,setup):
        self.logger.info("***test_009_SearchProduct started***")
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
        self.pp.search_box('women')
        assert self.pp.SearchedProductsExists(),"Searched products are not there"
        assert self.pp.SearchedProductsListExists(),"Search Products list is not there"
        product_titles = self.driver.find_elements(By.XPATH, "//div[@class='productinfo text-center']/p")
        # for product in product_titles:
        #     assert 'men' in product.text.casefold()
        assert all("women" in product.text.casefold().split()
                   for product in product_titles),"Not all products are for men"
