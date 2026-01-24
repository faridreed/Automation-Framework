import pytest
import os
import time
from selenium.webdriver.common.by import By
from pageObjects.HomePage import HomePage
from pageObjects.ProductsPage import ProductsPage
from pageObjects.CartPage import CartPage
from utilities.testProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_012_AddProductsInCart:
    baseUrl = ReadConfig.getApplicationURL()
    logger = LogGen.getLogger()

    def test_add_product_in_cart(self,setup):
        self.logger.info("***test_012_AddProductsInCart started***")
        self.driver = setup
        self.logger.info("***Launching Application***")
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()

        self.hp = HomePage(self.driver)
        assert self.hp.HomePageExists(), "Home Page is not visible"
        self.hp.click_products()
        self.hp.clean_google_ads()

        if "/products" not in self.driver.current_url:
            # Vignette hijacked navigation, force the correct page
            self.driver.get(self.baseUrl + "/products")
            self.hp.clean_google_ads()

        self.pp = ProductsPage(self.driver)
        self.hp.scroll_to_target(self.pp.button_first_product_cart_xpath)
        self.hp.mouse_hover_click(self.pp.button_first_product_cart_xpath)
        self.pp.click_continue_shopping()
        self.hp.scroll_to_target(self.pp.button_second_product_cart_xpath)
        self.hp.mouse_hover_click(self.pp.button_second_product_cart_xpath)
        self.pp.click_continue_shopping()
        self.products_on_pp = self.pp.get_product_titles()
        self.hp.scroll_to_target(self.hp.lnk_cart_xpath)
        self.hp.click_cart()
        self.cart_page = CartPage(self.driver)
        self.products_in_cart = self.cart_page.cart_product_titles()

        assert self.products_on_pp[:2] == self.products_in_cart[:2],"The products in cart are not the same"


