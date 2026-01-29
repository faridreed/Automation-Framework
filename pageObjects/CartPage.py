from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class CartPage:

    lst_all_product_titles = "(//h4)/a"
    txt_price_xpath = "//td[@class='price']"
    txt_total_xpath = "//td[@class='total']"
    txt_quantity_xpath = "/html/body/section/div/div[2]/table/tbody/tr/td[4]/button"
    txt_shop_cart_xpath = "//li[@class='active']"
    button_checkout_xpath = "//a[normalize-space()='Proceed To Checkout']"
    button_reg_login_xpath = "//u[normalize-space()='Register / Login']"

    def __init__(self, driver):
        self.driver = driver

    def cart_product_titles(self):
        products = self.driver.find_elements(By.XPATH, self.lst_all_product_titles)
        return [" ".join(product.text.split()) for product in products]

    def verify_quantity(self, expected_quantity, timeout=10):
        qtt = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located((By.XPATH, self.txt_quantity_xpath))
        ).text.strip()

        return qtt == str(expected_quantity)

    def click_checkout(self):
        (WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable
                                              ((By.XPATH, self.button_checkout_xpath ))).click())

    def click_register_login(self):
        self.driver.find_element(By.XPATH, self.button_reg_login_xpath).click()

    def ShoppingCartExists(self):
        try:
            return self.driver.find_element(By.XPATH, self.txt_shop_cart_xpath).is_displayed()
        except:
            return False

    def PriceTextExists(self):
        try:
            return self.driver.find_element(By.XPATH, self.txt_price_xpath).is_displayed()
        except:
            return False

    def QuantityTextExists(self):
        try:
            return self.driver.find_element(By.XPATH, self.txt_quantity_xpath).is_displayed()
        except:
            return False

    def TotalTextExists(self):
        try:
            return self.driver.find_element(By.XPATH, self.txt_total_xpath).is_displayed()
        except:
            return False