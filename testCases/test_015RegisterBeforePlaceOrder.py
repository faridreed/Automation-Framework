import pytest
import os
import time
from pageObjects.CheckoutPage import CheckoutPage
from pageObjects.PaymentPage import PaymentPage
from pageObjects.CartPage import CartPage
from pageObjects.HomePage import HomePage
from pageObjects.Login_Reg_Page import Login_Reg_Page
from pageObjects.RegistrationPage import RegistrationPage
from utilities.testProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities.randomString import random_email

class Test_015_RegisterBeforePlaceOrder:
    baseUrl = ReadConfig.getApplicationURL()
    logger = LogGen.getLogger()

    def test_register_before_order(self, setup):
        self.logger.info("***test_015_RegisterBeforePlaceOrder started***")
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
        self.lp.register_email(random_email())
        self.lp.click_reg_button()


        self.rp = RegistrationPage(self.driver)
        self.rp.select_gender('Mr.')
        self.rp.write_name('Fred')
        self.rp.write_password('freddy777')
        self.rp.select_birthday_day('26')
        self.rp.select_birthday_month('March')
        self.rp.select_birthday_year('1990')
        self.rp.click_newsletter()
        self.rp.click_optin()
        self.rp.write_first_name('Fred')
        self.rp.write_last_name('Jackson')
        self.rp.write_company('Google')
        self.rp.write_address1('123 Jacksonville Dr.')
        self.rp.write_address2('456 Jacksonville Dr.')
        self.rp.select_country('United States')
        self.rp.write_state('Texas')
        self.rp.write_city('Baku')
        self.rp.write_zipcode('1001')
        self.rp.write_mobile_number('9855885842')
        self.rp.click_create_account()
        self.rp.click_continue()

        assert self.hp.ensure_home(), "Could not reach Home (vignette/ad kept redirecting)"
        self.hp.close_home_ad()
        assert self.hp.LoggedInExists(), "Logged in text is not there"
        self.hp.scroll_to_target(self.hp.button_first_product_cart_xpath)
        self.hp.click(self.hp.button_first_product_cart_xpath)
        self.hp.click_cart()

        self.cart_page = CartPage(self.driver)
        assert self.cart_page.ShoppingCartExists(),"Shopping cart is not visible"
        self.cart_page.click_checkout()

        self.checkout_page = CheckoutPage(self.driver)
        assert self.checkout_page.verify_address1('123 Jacksonville Dr.'), "Address is not correct"
        self.hp.scroll_to_target(self.checkout_page.txt_review_order_xpath)
        assert self.checkout_page.verify_review_order(), "Review Order text is not there"
        self.hp.scroll_to_target(self.checkout_page.txtbox_comment_xpath)
        self.checkout_page.write_comment('Make it quick')
        self.checkout_page.click_place_order()

        self.payment_page = PaymentPage(self.driver)
        self.payment_page.write_name('Fred')
        self.payment_page.write_card_number('111222333')
        self.payment_page.write_cvc('333')
        self.payment_page.write_exp_date('05', '2033')
        self.payment_page.click_pay()
        self.payment_page.OrderPlacedSuccessMessageExists(), "Order placed successfully message is not visible"

        self.hp.delete_account()
        assert self.hp.account_deleted_confirmation(), "Account not deleted"
        self.hp.continue_after_deleting()