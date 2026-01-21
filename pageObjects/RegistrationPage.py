from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class RegistrationPage:
    # Account Information
    txt_enter_account_info_xpath = "//b[normalize-space()='Enter Account Information']"
    button_mr_id = "id_gender1"
    button_mrs_id = "id_gender2"
    txtbox_name_id = "name"
    txtbox_email_id = "email"
    txtbox_password_id = "password"
    dropdown_day_id = "days"
    dropdown_month_id = "months"
    dropdown_year_id = "years"
    button_newsletter_xpath = "//input[@id='newsletter']"
    button_optin_xpath = "//input[@id='optin']"

    # Address Information
    txtbox_firstname_id = "first_name"
    txtbox_lastname_id = "last_name"
    txtbox_company_id = "company"
    txtbox_address1_id = "address1"
    txtbox_address2_id = "address2"
    dropdown_country_id = "country"
    txtbox_state_id = "state"
    txtbox_city_id = "city"
    txtbox_zipcode_id = "zipcode"
    txtbox_mobilenumber_id = "mobile_number"
    button_create_account_xpath = "//button[normalize-space()='Create Account']"

    txtbox_email_subs_id = "susbscribe_email"



    def __init__(self, driver):
        self.driver = driver

    # Account Information

    def select_gender(self,gender):
        if gender == 'Mr.' or 'Mr' or 'Mister':
            self.driver.find_element(By.ID, self.button_mr_id).click()
        if gender == 'Mrs.' or 'Mrs' or 'Mistress':
            self.driver.find_element(By.ID, self.button_mrs_id).click()

    def write_name(self,name):
        self.driver.find_element(By.ID, self.txtbox_name_id).clear()
        self.driver.find_element(By.ID, self.txtbox_name_id).send_keys(name)

    def write_email(self,email):
        self.driver.find_element(By.ID, self.txtbox_email_id).clear()
        self.driver.find_element(By.ID, self.txtbox_email_id).send_keys(email)

    def write_password(self,password):
        self.driver.find_element(By.ID, self.txtbox_password_id).send_keys(password)

    def select_birthday_day(self,day):
        day_dropdown = self.driver.find_element(By.ID, self.dropdown_day_id)
        day_select = Select(day_dropdown)
        day_select.select_by_index(day)

    def select_birthday_month(self,month):
        month_dropdown = self.driver.find_element(By.ID, self.dropdown_month_id)
        month_select = Select(month_dropdown)
        month_select.select_by_visible_text(month)

    def select_birthday_year(self,year):
        year_dropdown = self.driver.find_element(By.ID, self.dropdown_year_id)
        year_select = Select(year_dropdown)
        year_select.select_by_value(year)

    def click_newsletter(self):
        self.driver.find_element(By.XPATH, self.button_newsletter_xpath).click()

    def click_optin(self):
        self.driver.find_element(By.XPATH, self.button_optin_xpath).click()

    # Address Information

    def write_first_name(self,first_name):
        self.driver.find_element(By.ID, self.txtbox_firstname_id).send_keys(first_name)

    def write_last_name(self,last_name):
        self.driver.find_element(By.ID, self.txtbox_lastname_id).send_keys(last_name)

    def write_company(self,company):
        self.driver.find_element(By.ID, self.txtbox_company_id).send_keys(company)

    def write_address1(self,address1):
        self.driver.find_element(By.ID, self.txtbox_address1_id).send_keys(address1)

    def write_address2(self,address2):
        self.driver.find_element(By.ID, self.txtbox_address2_id).send_keys(address2)

    def select_country(self,country):
        country_dropdown = self.driver.find_element(By.ID, self.dropdown_country_id)
        country_select = Select(country_dropdown)
        country_select.select_by_visible_text(country)

    def write_state(self,state):
        self.driver.find_element(By.ID, self.txtbox_state_id).send_keys(state)

    def write_city(self, city):
        self.driver.find_element(By.ID, self.txtbox_city_id).send_keys(city)

    def write_zipcode(self, zipcode):
        self.driver.find_element(By.ID, self.txtbox_zipcode_id).send_keys(zipcode)

    def write_mobile_number(self, mobile_number):
        self.driver.find_element(By.ID, self.txtbox_mobilenumber_id).send_keys(mobile_number)





