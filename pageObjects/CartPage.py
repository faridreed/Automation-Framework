from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class CartPage:

    lst_all_product_titles = "(//h4)/a"
    txt_price_xpath = "//td[@class='price']"
    txt_quantity_xpath = "//td[@class='quantity']"
    txt_total_xpath = "//td[@class='total']"

    def __init__(self, driver):
        self.driver = driver

    def cart_product_titles(self):
        products = self.driver.find_elements(By.XPATH, self.lst_all_product_titles)
        return [" ".join(product.text.split()) for product in products]

    def PriceTextExists(self):
        try:
            self.driver.find_element(By.XPATH, self.txt_price_xpath).is_displayed()
        except:
            return False

    def QuantityTextExists(self):
        try:
            self.driver.find_element(By.XPATH, self.txt_quantity_xpath).is_displayed()
        except:
            return False

    def TotalTextExists(self):
        try:
            self.driver.find_element(By.XPATH, self.txt_total_xpath).is_displayed()
        except:
            return False