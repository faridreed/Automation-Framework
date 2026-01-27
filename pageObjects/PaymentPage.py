from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class PaymentPage:

    txtbox_name_xpath = "//input[@name='name_on_card']"
    txtbox_card_number_xpath = "//input[@name='card_number']"
    txtbox_cvc_xpath = "//input[@placeholder='ex. 311']"
    txtbox_exp_month_xpath = "//input[@placeholder='MM']"
    txtbox_exp_year_xpath = "//input[@placeholder='YYYY']"

    button_pay_xpath = "//button[@id='submit']"

    txt_order_success_message = "//div[contains(text(),'Your order has been placed successfully!')]"



    def __init__(self,driver):
        self.driver = driver

    def write_name(self,name):
        self.driver.find_element(By.XPATH, self.txtbox_name_xpath).send_keys(name)

    def write_card_number(self,card_number):
        self.driver.find_element(By.XPATH, self.txtbox_card_number_xpath).send_keys(card_number)

    def write_cvc(self,cvc):
        self.driver.find_element(By.XPATH, self.txtbox_cvc_xpath).send_keys(cvc)

    def write_exp_date(self,month,year):
        self.driver.find_element(By.XPATH, self.txtbox_exp_month_xpath).send_keys(month)
        self.driver.find_element(By.XPATH, self.txtbox_exp_year_xpath).send_keys(year)

    def click_pay(self):
        self.driver.find_element(By.XPATH, self.button_pay_xpath).click()

    def OrderPlacedSuccessMessageExists(self):
        try:
            return self.driver.find_element(By.XPATH, self.txt_order_success_message).is_displayed()
        except:
            return False