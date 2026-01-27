from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class CheckoutPage:

    txt_delivery_address1_xpath = "/html/body/section/div/div[3]/div/div[1]/ul/li[4]"
    txt_review_order_xpath = "//h2[normalize-space()='Review Your Order']"

    txtbox_comment_xpath = "//textarea[@name='message']"

    button_place_order_xpath = "//a[normalize-space()='Place Order']"

    def __init__(self,driver):
        self.driver = driver

    def write_comment(self,comment):
        self.driver.find_element(By.XPATH, self.txtbox_comment_xpath).send_keys(comment)

    def click_place_order(self):
        self.driver.find_element(By.XPATH, self.button_place_order_xpath).click()

    def verify_address1(self,address):
        address1 = self.driver.find_element(By.XPATH, self.txt_delivery_address1_xpath).text
        return address1.strip() == address.strip()

    def verify_review_order(self):
        el = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.txt_review_order_xpath)))
        try:
            return el.is_displayed()
        except:
            return False

