from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class TestCasesPage:
    txt_tcases_xpath = "//b[normalize-space()='Test Cases']"

    def __init__(self,driver):
        self.driver = driver

    def TestCasesExists(self):
        try:
            return self.driver.find_element(By.XPATH, self.txt_tcases_xpath).is_displayed()
        except:
            return False