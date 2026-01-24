from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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
    txt_searched_products_xpath = "//h2[normalize-space()='Searched Products']"
    txt_searched_products_lst_xpath = "(//div[@class='single-products'])"
    button_first_product_cart_xpath = "(//a[contains(@class,'add-to-cart')])[1]"
    button_second_product_cart_xpath = "(//div[contains(@class,'productinfo')])[2]//a[contains(@class,'add-to-cart')]"
    lst_all_product_titles_xpath = "(//div[@class='productinfo text-center'])/p"


    def __init__(self, driver):
        self.driver = driver

    def search_box(self, search):
        searchbox =  self.driver.find_element(By.XPATH, self.txtbox_search_xpath)
        searchbox.click()
        searchbox.send_keys(search)
        self.driver.find_element(By.XPATH, self.button_search_xpath).click()

    def click_first_product(self):
        self.driver.find_element(By.XPATH, self.lnk_first_product_xpath).click()

    def click_continue_shopping(self, timeout=10):
        wait = WebDriverWait(self.driver, timeout)

        try:
            # 1) Wait for the cart modal itself to be visible
            wait.until(EC.visibility_of_element_located((By.ID, "cartModal")))

            # 2) Click "Continue Shopping" inside that modal
            btn = wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//div[@id='cartModal']//button[normalize-space()='Continue Shopping']")
            ))
            btn.click()

            # 3) Wait for modal to close (prevents next click being blocked)
            wait.until(EC.invisibility_of_element_located((By.ID, "cartModal")))

        except TimeoutException:
            # Modal didn't appear OR button wasn't clickable.
            # Don't hard-fail here; raise a clearer error.
            raise AssertionError("Cart modal did not appear or 'Continue Shopping' was not clickable.")

    def get_product_titles(self):
        products = self.driver.find_elements(By.XPATH, "//div[@class='productinfo text-center']/p")
        return [" ".join(product.text.split()) for product in products]

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

    def SearchedProductsExists(self):
        try:
            return self.driver.find_element(By.XPATH, self.txt_searched_products_xpath).is_displayed()
        except:
            return False

    def SearchedProductsListExists(self):
        products_lst = self.driver.find_elements(By.XPATH, self.txt_searched_products_lst_xpath)
        return len(products_lst) > 0



