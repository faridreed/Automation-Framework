from selenium.webdriver.common.by import By

class HomePage:
    lnk_home_xpath = "//a[normalize-space()='Home']"
    lnk_products_xpath = "//a[@href='/products']"
    lnk_cart_xpath = "//a[@href='/view_cart']"
    lnk_reg_login_xpath = "//a[normalize-space()='Signup / Login']"
    lnk_tcases_xpath = "//a[contains(text(),'Test Cases')]"
    lnk_apitest_xpath = "//a[normalize-space()='API Testing']"
    lnk_video_tut_xpath = "//a[normalize-space()='Video Tutorials']"
    lnk_contact_xpath = "//a[normalize-space()='Contact us']"
    txt_confirmation_xpath = "//h1[normalize-space()='AutomationExercise']"

    def __init__(self, driver):
        self.driver = driver

    def click_home(self):
        self.driver.find_element(By.XPATH, self.lnk_home_xpath).click()
    def click_products(self):
        self.driver.find_element(By.XPATH, self.lnk_products_xpath).click()
    def click_cart(self):
        self.driver.find_element(By.XPATH, self.lnk_cart_xpath).click()
    def click_reg_login(self):
        self.driver.find_element(By.XPATH, self.lnk_reg_login_xpath).click()
    def click_tcases(self):
        self.driver.find_element(By.XPATH, self.lnk_tcases_xpath).click()
    def click_apitest(self):
        self.driver.find_element(By.XPATH, self.lnk_apitest_xpath).click()
    def click_video_tut(self):
        self.driver.find_element(By.XPATH, self.lnk_video_tut_xpath).click()
    def click_contact(self):
        self.driver.find_element(By.XPATH, self.lnk_contact_xpath).click()
    def HomePageExists(self):
       try:
           self.driver.find_element(By.XPATH, self.txt_confirmation_xpath).is_displayed()
       except:
           return False



