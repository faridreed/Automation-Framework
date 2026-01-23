from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ContactUsPage:
    txt_contact_us_xpath = "//h2[normalize-space()='Contact Us']"
    txt_get_in_touch_xpath = "//h2[normalize-space()='Get In Touch']"
    txtbox_name_xpath = "//input[@placeholder='Name']"
    txtbox_email_xpath = "//input[@placeholder='Email']"
    txtbox_subject_xpath = "//input[@placeholder='Subject']"
    txtbox_message_xpath = "//input[@placeholder='Subject']"
    button_browse_xpath = "//input[@name='upload_file']"
    button_submit_xpath = "//input[@name='submit']"
    txt_success_xpath = "//div[@class='status alert alert-success']"

    def __init__(self,driver):
        self.driver = driver

    def GetInTouchExists(self):
        try:
            return self.driver.find_element(By.XPATH, self.txt_get_in_touch_xpath).is_displayed()
        except:
            return False

    def ContactUsExists(self):
        try:
            return self.driver.find_element(By.XPATH, self.txt_contact_us_xpath).is_displayed()
        except:
            return False

    def write_name(self,name):
        self.driver.find_element(By.XPATH, self.txtbox_name_xpath).send_keys(name)

    def write_email(self,email):
        self.driver.find_element(By.XPATH, self.txtbox_email_xpath).send_keys(email)

    def write_subject(self,subject):
        self.driver.find_element(By.XPATH, self.txtbox_subject_xpath).send_keys(subject)

    def write_message(self,message):
        self.driver.find_element(By.XPATH, self.txtbox_message_xpath).send_keys(message)

    def upload_file(self,path):
        self.driver.find_element(By.XPATH, self.button_browse_xpath).send_keys(path)

    def click_submit(self):
        self.driver.find_element(By.XPATH, self.button_submit_xpath).click()

    def click_alert(self):
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        self.driver.switch_to.alert.accept()

    def SuccessMessageDisplayed(self):
        try:
           return self.driver.find_element(By.XPATH, self.txt_success_xpath).is_displayed()
        except:
            return False


