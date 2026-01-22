from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


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
    lnk_loggedin_xpath = "//li[10]//a[1]"
    button_delete_acc_xpath = "//a[normalize-space()='Delete Account']"
    txt_account_deleted_xpath = "//b[normalize-space()='Account Deleted!']"
    button_logout_xpath = "//a[normalize-space()='Logout']"


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

    def click_logout(self):
        self.driver.find_element(By.XPATH, self.button_logout_xpath).click()

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

    def LoggedInExists(self):
        try:
            self.driver.find_element(By.XPATH, self.lnk_loggedin_xpath).is_displayed()
        except:
            return False

    def delete_account(self):
        self.driver.find_element(By.XPATH, self.button_delete_acc_xpath).click()

    def account_deleted_confirmation(self):
        try:
            self.driver.find_element(By.XPATH, self.txt_account_deleted_xpath).is_displayed()
        except:
            return False


    def continue_after_deleting(self):
        self.driver.find_element(By.XPATH, "//a[normalize-space()='Continue']").click()

    def ensure_home(self, tries=3):
        HOME = "https://www.automationexercise.com/"
        wait = WebDriverWait(self.driver, 10)

        for _ in range(tries):
            # If vignette fragment appears, don't fight it — just go Home
            if "google_vignette" in self.driver.current_url or "account_created" in self.driver.current_url:
                self.driver.get(HOME)
            else:
                # even if you're somewhere else, you said you need Home next
                self.driver.get(HOME)

            # Wait for Home header to load
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "header#header")))

            # If we’re on Home and not stuck on vignette, we’re good
            if "google_vignette" not in self.driver.current_url and self.driver.current_url.rstrip("/") == HOME.rstrip(
                    "/"):
                return True

        return False

    def close_home_ad(self):
        self.driver.execute_script("""
            // 1) Remove google ad iframes only (very specific)
            document.querySelectorAll('iframe').forEach(f => {
                const src = (f.getAttribute('src') || '').toLowerCase();
                const id  = (f.getAttribute('id')  || '').toLowerCase();

                const isGoogleAd =
                    src.includes('doubleclick') ||
                    src.includes('googleads') ||
                    src.includes('googlesyndication') ||
                    id.startsWith('google_ads_iframe') ||
                    id.startsWith('aswift');

                if (isGoogleAd) {
                    // remove iframe + its aswift container if present
                    const p = f.parentElement;
                    f.remove();
                    if (p && p.id && p.id.toLowerCase().startsWith('aswift_')) p.remove();
                }
            });

            // 2) Remove aswift_* wrappers left behind (also very specific)
            document.querySelectorAll("div[id^='aswift_']").forEach(d => d.remove());

            // 3) Restore scrolling
            document.documentElement.style.overflow = 'auto';
            document.body.style.overflow = 'auto';
        """)




