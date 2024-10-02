import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from LocatorPage.LocatorsPage import InvalidLoginLocatorsPage, ValidLoginLocatorsPage, AddNewContact1LocatorsPage, \
    FillContact1LocatorsPage


class InvalidLoginActionsPage:
    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):
        self.driver.get(url)

    def enter_invalid_email(self, invalid_email):
        enter_invalid_email = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(InvalidLoginLocatorsPage.ENTER_INVALID_EMAIL))
        enter_invalid_email.send_keys(invalid_email)
        time.sleep(2)

    def enter_invalid_password(self, invalid_password):
        enter_invalid_password = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(InvalidLoginLocatorsPage.ENTER_INVALID_PASSWORD))
        enter_invalid_password.send_keys(invalid_password)
        time.sleep(2)

    def click_submit(self):
        click_submit = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(InvalidLoginLocatorsPage.CLICK_SUBMIT))
        click_submit.click()
        time.sleep(2)


class ValidLoginActionsPage:
    def __init__(self, driver):
        self.driver = driver

    def open_url1(self, url):
        self.driver.get(url)

    def enter_valid_email(self, email):
        enter_valid_email = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(ValidLoginLocatorsPage.ENTER_VALID_EMAIL))
        enter_valid_email.send_keys(email)
        time.sleep(2)

    def enter_valid_password(self, password):
        enter_valid_password = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(ValidLoginLocatorsPage.ENTER_VALID_PASSWORD))
        enter_valid_password.send_keys(password)
        time.sleep(2)

    def click_submit1(self):
        click_submit1 = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(ValidLoginLocatorsPage.CLICK_SUBMIT1))
        click_submit1.click()
        time.sleep(2)


class AddNewContact1ActionsPage:
    def __init__(self, driver):
        self.driver = driver

    def click_add_new_contact1_icon(self, addnewcontact1):
        click_add_new_contact1_icon = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact1LocatorsPage.CLICK_ADD_NEW_CONTACT1_ICON))
        click_add_new_contact1_icon.send_keys(addnewcontact1)
        time.sleep(2)


class FillContact1ActionsPage:
    def __init__(self, driver):
        self.driver = driver

    def fill_contact1_first_name(self, first_name):
        fill_contact1_first_name = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(FillContact1LocatorsPage.FILL_CONTACT1_FIRST_NAME))
        fill_contact1_first_name.send_keys(first_name)
        time.sleep(2)

    def fill_contact1_lastname(self, lastname):
        fill_contact1_lastname = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(FillContact1LocatorsPage.FILL_CONTACT1_LAST_NAME))
        fill_contact1_lastname.send_keys(lastname)
        time.sleep(2)

    def fill_contact1_birthdate(self, birthday):
        fill_contact1_birthdate = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(FillContact1LocatorsPage.FILL_CONTACT1_BIRTHDATE))
        fill_contact1_birthdate.send_keys(birthday)
        time.sleep(2)

    def fill_contact1_email(self, email):
        fill_contact1_email = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(FillContact1LocatorsPage.FILL_CONTACT1_EMAIL))
        fill_contact1_email.send_keys(email)
        time.sleep(2)

    def fill_contact1_phone(self, phone):
        fill_contact1_phone = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(FillContact1LocatorsPage.FILL_CONTACT1_PHONE))
        fill_contact1_phone.send_keys(phone)
        time.sleep(2)

    def fill_contact1_street1(self, street1):
        fill_contact1_street1 = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(FillContact1LocatorsPage.FILL_CONTACT1_STREET1))
        fill_contact1_street1.send_keys(street1)
        time.sleep(2)

    def fill_contact1_street2(self, street2):
        fill_contact1_street2 = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(FillContact1LocatorsPage.FILL_CONTACT1_STREET2))
        fill_contact1_street2.send_keys(street2)
        time.sleep(2)

    def fill_contact1_city(self, city):
        fill_contact1_city = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(FillContact1LocatorsPage.FILL_CONTACT1_CITY))
        fill_contact1_city.send_keys(city)
        time.sleep(2)

    def fill_contact1_state(self, state):
        fill_contact1_state = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(FillContact1LocatorsPage.FILL_CONTACT1_STATE))
        fill_contact1_state.send_keys(state)
        time.sleep(2)

    def fill_contact1_postalcode(self, postalcode):
        fill_contact1_postalcode = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(FillContact1LocatorsPage.FILL_CONTACT1_POSTALCODE))
        fill_contact1_postalcode.send_keys(postalcode)
        time.sleep(2)

    def fill_contact1_country(self, country):
        fill_contact1_country = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(FillContact1LocatorsPage.FILL_CONTACT1_COUNTRY))
        fill_contact1_country.send_keys(country)
        time.sleep(2)

    def fill_contact1_submit(self):
        fill_contact1_submit = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(FillContact1LocatorsPage.FILL_CONTACT1_SUBMIT))
        fill_contact1_submit.click()
        time.sleep(2)
