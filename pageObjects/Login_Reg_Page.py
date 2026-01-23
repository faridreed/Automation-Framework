from selenium.webdriver.common.by import By

class Login_Reg_Page:
    txtbox_reg_name_xpath = "//input[@placeholder='Name']"
    txtbox_reg_email_xpath = "//input[@data-qa='signup-email']"
    btn_reg_xpath = "//button[normalize-space()='Signup']"

    txtbox_login_email_xpath = "//input[@data-qa='login-email']"
    txtbox_login_password_xpath = "//input[@placeholder='Password']"
    btn_login_xpath = "//button[normalize-space()='Login']"

    txt_new_user_signup_xpath = "//h2[normalize-space()='New User Signup!']"
    txt_login_to_account_xpath = "//h2[normalize-space()='Login to your account']"
    txt_incorrect_email_pass_xpath = "//p[normalize-space()='Your email or password is incorrect!']"
    txt_email_exists_xpath = "//p[normalize-space()='Email Address already exist!']"


    def __init__(self, driver):
        self.driver = driver

    def register_name(self, name):
        self.driver.find_element(By.XPATH, self.txtbox_reg_name_xpath).send_keys(name)

    def register_email(self, email):
        self.driver.find_element(By.XPATH, self.txtbox_reg_email_xpath).send_keys(email)

    def click_reg_button(self):
        self.driver.find_element(By.XPATH, self.btn_reg_xpath).click()


    def login_email(self, email):
        self.driver.find_element(By.XPATH, self.txtbox_login_email_xpath).send_keys(email)

    def login_password(self, password):
        self.driver.find_element(By.XPATH, self.txtbox_login_password_xpath).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(By.XPATH, self.btn_login_xpath).click()

    def NewUserSignUpExists(self):
        try:
            return self.driver.find_element(By.XPATH, self.txt_new_user_signup_xpath).is_displayed()
        except:
            return False

    def LoginExists(self):
        try:
            return self.driver.find_element(By.XPATH, self.txt_login_to_account_xpath).is_displayed()
        except:
            return False

    def IncorrectEmailOrPasswordVisible(self):
        try:
            return self.driver.find_element(By.XPATH, self.txt_incorrect_email_pass_xpath).is_displayed()
        except:
            return False

    def EmailAlreadyExistsVisible(self):
        try:
            return self.driver.find_element(By.XPATH, self.txt_email_exists_xpath).is_displayed()
        except:
            return False
