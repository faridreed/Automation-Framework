from selenium.webdriver.common.by import By

class ProductsPage:

    txt_allproducts_xpath = "//h2[normalize-space()='All Products']"
    txtbox_search_xpath = "//input[@id='search_product']"
    button_search_xpath = "//button[@id='submit_search']"
    container_products_xpath = "//div[@class='features_items']"
    lst_products_xpath = "(//div[@class='col-sm-4'])"
    lnk_first_product_xpath = "(//a[contains(text(),'View Product')])[1]"
    txt_product_availability_xpath = "//b[normalize-space()='Availability:']"
    txt_product_condition_xpath = "//b[normalize-space()='Condition:']"
    txt_product_brand_xpath = "//b[normalize-space()='Brand:']"

    def __init__(self, driver):
        self.driver = driver

    def click_first_product(self):
        self.driver.find_element(By.XPATH, self.lnk_first_product_xpath).click()

    def ProductsListExists(self):
        elements = self.driver.find_elements(By.XPATH, "//div[@class='col-sm-4']")
        return len(elements) > 0 and elements[0].is_displayed()

    def AllProductsExists(self):
        try:
            return self.driver.find_element(By.XPATH, self.txt_allproducts_xpath).is_displayed()
        except:
            return False

    def ProductDetailsExists(self):
        xpaths = [
            self.txt_product_availability_xpath,
            self.txt_product_condition_xpath,
            self.txt_product_brand_xpath,
        ]

        for xp in xpaths:
            els = self.driver.find_elements(By.XPATH, xp)
            if not els or not els[0].is_displayed():
                return False
        return True


