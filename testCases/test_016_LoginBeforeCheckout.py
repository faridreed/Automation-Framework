import pytest
import os
import time
from pageObjects.CheckoutPage import CheckoutPage
from pageObjects.PaymentPage import PaymentPage
from pageObjects.CartPage import CartPage
from pageObjects.HomePage import HomePage
from pageObjects.Login_Reg_Page import Login_Reg_Page
from pageObjects.ProductsPage import ProductsPage
from pageObjects.RegistrationPage import RegistrationPage
from utilities.testProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities.randomString import random_email

class Test_016_LoginBeforeCheckout:
    baseUrl = ReadConfig.getApplicationURL()
    logger = LogGen.getLogger()

    def test_login_before_checkout(self, setup):
        self.logger.info("***test_016_RegisterBeforeCheckout started***")
        self.driver = setup
        self.logger.info("***Launching Application***")
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()

        self.hp = HomePage(self.driver)
        assert self.hp.HomePageExists(), "Home Page is not visible"
        self.hp.click_reg_login()

        self.lp = Login_Reg_Page(self.driver)
        assert self.lp.LoginExists(), "Login text is not visible"
        self.lp.login_email('freddy006@gmail.com')
        self.lp.login_password('freddy777')
        self.lp.click_login_button()

        self.pp = ProductsPage(self.driver)
        assert self.hp.ensure_home(), "Could not reach Home (vignette/ad kept redirecting)"
        self.hp.close_home_ad()
        assert self.hp.LoggedInExists(), "Logged in text is not visible"
        self.hp.scroll_to_target(self.hp.button_first_product_cart_xpath)
        self.hp.click(self.hp.button_first_product_cart_xpath)
        self.pp.click_continue_shopping()
        self.hp.scroll_to_target(self.hp.lnk_cart_xpath)
        self.hp.click_cart()

        self.cart_page = CartPage(self.driver)
        self.cart_page.ShoppingCartExists()
        self.cart_page.click_checkout()

        self.checkout_page = CheckoutPage(self.driver)
        assert self.checkout_page.verify_address1('123 Jacksonville Dr.'), "Address is not correct"
        self.hp.scroll_to_target(self.checkout_page.txt_review_order_xpath)
        assert self.checkout_page.verify_review_order(), "Review Order text is not there"
        self.hp.scroll_to_target(self.checkout_page.txtbox_comment_xpath)
        self.checkout_page.write_comment('Make it quick')
        self.checkout_page.click_place_order()

        if "/payment" not in self.driver.current_url:
            self.driver.get(self.driver.current_url + "/payment")

        time.sleep(2)
        self.payment_page = PaymentPage(self.driver)
        self.payment_page.write_name('Fred')
        self.payment_page.write_card_number('111222333')
        self.payment_page.write_cvc('333')
        self.payment_page.write_exp_date('05', '2033')
        self.payment_page.click_pay()
        assert self.payment_page.OrderPlacedMessageExists(), "Order placed successfully message is not visible"