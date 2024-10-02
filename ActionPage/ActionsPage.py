import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from LocatorPage.LocatorsPage import InvalidLoginLocatorsPage, ValidLoginLocatorsPage, ClickAddNewContact1LocatorsPage, \
    AddNewContact1LocatorsPage, ClickAddNewContact2LocatorsPage, AddNewContact2LocatorsPage, \
    ClickAddNewContact3LocatorsPage, AddNewContact3LocatorsPage, ClickAddNewContact4LocatorsPage, \
    AddNewContact4LocatorsPage


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


class ClickAddNewContact1ActionsPage:
    def __init__(self, driver):
        self.driver = driver

    def click_add_new_contact1_icon(self, addnewcontact1):
        click_add_new_contact1_icon = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(ClickAddNewContact1LocatorsPage.CLICK_ADD_NEW_CONTACT1_ICON))
        click_add_new_contact1_icon.click()
        time.sleep(2)


class AddNewContact1ActionsPage:
    def __init__(self, driver):
        self.driver = driver

    def fill_contact1_firstname(self, firstname):
        fill_contact1_first_name = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact1LocatorsPage.FILL_CONTACT1_FIRST_NAME))
        fill_contact1_first_name.send_keys(firstname)
        time.sleep(2)

    def fill_contact1_lastname(self, lastname):
        fill_contact1_lastname = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact1LocatorsPage.FILL_CONTACT1_LAST_NAME))
        fill_contact1_lastname.send_keys(lastname)
        time.sleep(2)

    def fill_contact1_birthdate(self, birthday):
        fill_contact1_birthdate = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact1LocatorsPage.FILL_CONTACT1_BIRTHDATE))
        fill_contact1_birthdate.send_keys(birthday)
        time.sleep(2)

    def fill_contact1_email(self, email):
        fill_contact1_email = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact1LocatorsPage.FILL_CONTACT1_EMAIL))
        fill_contact1_email.send_keys(email)
        time.sleep(2)

    def fill_contact1_phone(self, phone):
        fill_contact1_phone = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact1LocatorsPage.FILL_CONTACT1_PHONE))
        fill_contact1_phone.send_keys(phone)
        time.sleep(2)

    def fill_contact1_street1(self, street1):
        fill_contact1_street1 = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact1LocatorsPage.FILL_CONTACT1_STREET1))
        fill_contact1_street1.send_keys(street1)
        time.sleep(2)

    def fill_contact1_street2(self, street2):
        fill_contact1_street2 = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact1LocatorsPage.FILL_CONTACT1_STREET2))
        fill_contact1_street2.send_keys(street2)
        time.sleep(2)

    def fill_contact1_city(self, city):
        fill_contact1_city = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact1LocatorsPage.FILL_CONTACT1_CITY))
        fill_contact1_city.send_keys(city)
        time.sleep(2)

    def fill_contact1_state(self, state):
        fill_contact1_state = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact1LocatorsPage.FILL_CONTACT1_STATE))
        fill_contact1_state.send_keys(state)
        time.sleep(2)

    def fill_contact1_postalcode(self, postalcode):
        fill_contact1_postalcode = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact1LocatorsPage.FILL_CONTACT1_POSTALCODE))
        fill_contact1_postalcode.send_keys(postalcode)
        time.sleep(2)

    def fill_contact1_country(self, country):
        fill_contact1_country = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact1LocatorsPage.FILL_CONTACT1_COUNTRY))
        fill_contact1_country.send_keys(country)
        time.sleep(2)

    def fill_contact1_submit(self):
        fill_contact1_submit = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact1LocatorsPage.FILL_CONTACT1_SUBMIT))
        fill_contact1_submit.click()
        time.sleep(2)


class ClickAddNewContact2ActionsPage:
    def __init__(self, driver):
        self.driver = driver

    def click_add_new_contact2_icon(self, addnewcontact1):
        click_add_new_contact2_icon = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(ClickAddNewContact2LocatorsPage.CLICK_ADD_NEW_CONTACT2_ICON))
        click_add_new_contact2_icon.click()
        time.sleep(2)


class AddNewContact2ActionsPage:
    def __init__(self, driver):
        self.driver = driver

    def fill_contact2_firstname(self, firstname):
        fill_contact2_first_name = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact2LocatorsPage.FILL_CONTACT2_FIRST_NAME))
        fill_contact2_first_name.send_keys(firstname)
        time.sleep(2)

    def fill_contact2_lastname(self, lastname):
        fill_contact2_lastname = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact2LocatorsPage.FILL_CONTACT2_LAST_NAME))
        fill_contact2_lastname.send_keys(lastname)
        time.sleep(2)

    def fill_contact2_birthdate(self, birthday):
        fill_contact2_birthdate = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact2LocatorsPage.FILL_CONTACT2_BIRTHDATE))
        fill_contact2_birthdate.send_keys(birthday)
        time.sleep(2)

    def fill_contact2_email(self, email):
        fill_contact2_email = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact2LocatorsPage.FILL_CONTACT2_EMAIL))
        fill_contact2_email.send_keys(email)
        time.sleep(2)

    def fill_contact2_phone(self, phone):
        fill_contact2_phone = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact2LocatorsPage.FILL_CONTACT2_PHONE))
        fill_contact2_phone.send_keys(phone)
        time.sleep(2)

    def fill_contact2_street1(self, street1):
        fill_contact2_street1 = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact2LocatorsPage.FILL_CONTACT2_STREET1))
        fill_contact2_street1.send_keys(street1)
        time.sleep(2)

    def fill_contact2_street2(self, street2):
        fill_contact2_street2 = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact2LocatorsPage.FILL_CONTACT2_STREET2))
        fill_contact2_street2.send_keys(street2)
        time.sleep(2)

    def fill_contact2_city(self, city):
        fill_contact2_city = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact2LocatorsPage.FILL_CONTACT2_CITY))
        fill_contact2_city.send_keys(city)
        time.sleep(2)

    def fill_contact2_state(self, state):
        fill_contact2_state = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact2LocatorsPage.FILL_CONTACT2_STATE))
        fill_contact2_state.send_keys(state)
        time.sleep(2)

    def fill_contact2_postalcode(self, postalcode):
        fill_contact2_postalcode = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact2LocatorsPage.FILL_CONTACT2_POSTALCODE))
        fill_contact2_postalcode.send_keys(postalcode)
        time.sleep(2)

    def fill_contact2_country(self, country):
        fill_contact2_country = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact2LocatorsPage.FILL_CONTACT2_COUNTRY))
        fill_contact2_country.send_keys(country)
        time.sleep(2)

    def fill_contact2_submit(self):
        fill_contact2_submit = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact2LocatorsPage.FILL_CONTACT2_SUBMIT))
        fill_contact2_submit.click()
        time.sleep(2)


class ClickAddNewContact3ActionsPage:
    def __init__(self, driver):
        self.driver = driver

    def click_add_new_contact3_icon(self, addnewcontact3):
        click_add_new_contact3_icon = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(ClickAddNewContact3LocatorsPage.CLICK_ADD_NEW_CONTACT3_ICON))
        click_add_new_contact3_icon.click()
        time.sleep(2)


class AddNewContact3ActionsPage:
    def __init__(self, driver):
        self.driver = driver

    def fill_contact3_firstname(self, firstname):
        fill_contact3_first_name = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact3LocatorsPage.FILL_CONTACT3_FIRST_NAME))
        fill_contact3_first_name.send_keys(firstname)
        time.sleep(2)

    def fill_contact3_lastname(self, lastname):
        fill_contact3_lastname = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact3LocatorsPage.FILL_CONTACT3_LAST_NAME))
        fill_contact3_lastname.send_keys(lastname)
        time.sleep(2)

    def fill_contact3_birthdate(self, birthday):
        fill_contact3_birthdate = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact3LocatorsPage.FILL_CONTACT3_BIRTHDATE))
        fill_contact3_birthdate.send_keys(birthday)
        time.sleep(2)

    def fill_contact3_email(self, email):
        fill_contact3_email = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact3LocatorsPage.FILL_CONTACT3_EMAIL))
        fill_contact3_email.send_keys(email)
        time.sleep(2)

    def fill_contact3_phone(self, phone):
        fill_contact3_phone = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact3LocatorsPage.FILL_CONTACT3_PHONE))
        fill_contact3_phone.send_keys(phone)
        time.sleep(2)

    def fill_contact3_street1(self, street1):
        fill_contact3_street1 = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact3LocatorsPage.FILL_CONTACT3_STREET1))
        fill_contact3_street1.send_keys(street1)
        time.sleep(2)

    def fill_contact3_street2(self, street2):
        fill_contact3_street2 = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact3LocatorsPage.FILL_CONTACT3_STREET2))
        fill_contact3_street2.send_keys(street2)
        time.sleep(2)

    def fill_contact3_city(self, city):
        fill_contact3_city = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact3LocatorsPage.FILL_CONTACT3_CITY))
        fill_contact3_city.send_keys(city)
        time.sleep(2)

    def fill_contact3_state(self, state):
        fill_contact3_state = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact3LocatorsPage.FILL_CONTACT3_STATE))
        fill_contact3_state.send_keys(state)
        time.sleep(2)

    def fill_contact3_postalcode(self, postalcode):
        fill_contact3_postalcode = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact3LocatorsPage.FILL_CONTACT3_POSTALCODE))
        fill_contact3_postalcode.send_keys(postalcode)
        time.sleep(2)

    def fill_contact3_country(self, country):
        fill_contact3_country = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact3LocatorsPage.FILL_CONTACT3_COUNTRY))
        fill_contact3_country.send_keys(country)
        time.sleep(2)

    def fill_contact3_submit(self):
        fill_contact3_submit = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact3LocatorsPage.FILL_CONTACT3_SUBMIT))
        fill_contact3_submit.click()
        time.sleep(2)


class ClickAddNewContact4ActionsPage:
    def __init__(self, driver):
        self.driver = driver

    def click_add_new_contact4_icon(self, addnewcontact1):
        click_add_new_contact4_icon = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(ClickAddNewContact4LocatorsPage.CLICK_ADD_NEW_CONTACT4_ICON))
        click_add_new_contact4_icon.click()
        time.sleep(2)


class AddNewContact4ActionsPage:
    def __init__(self, driver):
        self.driver = driver

    def fill_contact4_firstname(self, firstname):
        fill_contact4_first_name = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact4LocatorsPage.FILL_CONTACT4_FIRST_NAME))
        fill_contact4_first_name.send_keys(firstname)
        time.sleep(2)

    def fill_contact4_lastname(self, lastname):
        fill_contact4_lastname = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact4LocatorsPage.FILL_CONTACT4_LAST_NAME))
        fill_contact4_lastname.send_keys(lastname)
        time.sleep(2)

    def fill_contact4_birthdate(self, birthday):
        fill_contact4_birthdate = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact4LocatorsPage.FILL_CONTACT4_BIRTHDATE))
        fill_contact4_birthdate.send_keys(birthday)
        time.sleep(2)

    def fill_contact4_email(self, email):
        fill_contact4_email = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact4LocatorsPage.FILL_CONTACT4_EMAIL))
        fill_contact4_email.send_keys(email)
        time.sleep(2)

    def fill_contact4_phone(self, phone):
        fill_contact4_phone = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact4LocatorsPage.FILL_CONTACT4_PHONE))
        fill_contact4_phone.send_keys(phone)
        time.sleep(2)

    def fill_contact2_street1(self, street1):
        fill_contact2_street1 = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact2LocatorsPage.FILL_CONTACT2_STREET1))
        fill_contact2_street1.send_keys(street1)
        time.sleep(2)

    def fill_contact2_street2(self, street2):
        fill_contact2_street2 = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact2LocatorsPage.FILL_CONTACT2_STREET2))
        fill_contact2_street2.send_keys(street2)
        time.sleep(2)

    def fill_contact2_city(self, city):
        fill_contact2_city = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact2LocatorsPage.FILL_CONTACT2_CITY))
        fill_contact2_city.send_keys(city)
        time.sleep(2)

    def fill_contact2_state(self, state):
        fill_contact2_state = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact2LocatorsPage.FILL_CONTACT2_STATE))
        fill_contact2_state.send_keys(state)
        time.sleep(2)

    def fill_contact2_postalcode(self, postalcode):
        fill_contact2_postalcode = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact2LocatorsPage.FILL_CONTACT2_POSTALCODE))
        fill_contact2_postalcode.send_keys(postalcode)
        time.sleep(2)

    def fill_contact2_country(self, country):
        fill_contact2_country = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact2LocatorsPage.FILL_CONTACT2_COUNTRY))
        fill_contact2_country.send_keys(country)
        time.sleep(2)

    def fill_contact2_submit(self):
        fill_contact2_submit = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact2LocatorsPage.FILL_CONTACT2_SUBMIT))
        fill_contact2_submit.click()
        time.sleep(2)


class ClickAddNewContact2ActionsPage:
    def __init__(self, driver):
        self.driver = driver

    def click_add_new_contact2_icon(self, addnewcontact1):
        click_add_new_contact2_icon = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(ClickAddNewContact2LocatorsPage.CLICK_ADD_NEW_CONTACT2_ICON))
        click_add_new_contact2_icon.click()
        time.sleep(2)


class AddNewContact2ActionsPage:
    def __init__(self, driver):
        self.driver = driver

    def fill_contact2_firstname(self, firstname):
        fill_contact2_first_name = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact2LocatorsPage.FILL_CONTACT2_FIRST_NAME))
        fill_contact2_first_name.send_keys(firstname)
        time.sleep(2)

    def fill_contact2_lastname(self, lastname):
        fill_contact2_lastname = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact2LocatorsPage.FILL_CONTACT2_LAST_NAME))
        fill_contact2_lastname.send_keys(lastname)
        time.sleep(2)

    def fill_contact2_birthdate(self, birthday):
        fill_contact2_birthdate = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact2LocatorsPage.FILL_CONTACT2_BIRTHDATE))
        fill_contact2_birthdate.send_keys(birthday)
        time.sleep(2)

    def fill_contact2_email(self, email):
        fill_contact2_email = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact2LocatorsPage.FILL_CONTACT2_EMAIL))
        fill_contact2_email.send_keys(email)
        time.sleep(2)

    def fill_contact2_phone(self, phone):
        fill_contact2_phone = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact2LocatorsPage.FILL_CONTACT2_PHONE))
        fill_contact2_phone.send_keys(phone)
        time.sleep(2)

    def fill_contact2_street1(self, street1):
        fill_contact2_street1 = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact2LocatorsPage.FILL_CONTACT2_STREET1))
        fill_contact2_street1.send_keys(street1)
        time.sleep(2)

    def fill_contact2_street2(self, street2):
        fill_contact2_street2 = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact2LocatorsPage.FILL_CONTACT2_STREET2))
        fill_contact2_street2.send_keys(street2)
        time.sleep(2)

    def fill_contact2_city(self, city):
        fill_contact2_city = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact2LocatorsPage.FILL_CONTACT2_CITY))
        fill_contact2_city.send_keys(city)
        time.sleep(2)

    def fill_contact2_state(self, state):
        fill_contact2_state = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact2LocatorsPage.FILL_CONTACT2_STATE))
        fill_contact2_state.send_keys(state)
        time.sleep(2)

    def fill_contact2_postalcode(self, postalcode):
        fill_contact2_postalcode = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact2LocatorsPage.FILL_CONTACT2_POSTALCODE))
        fill_contact2_postalcode.send_keys(postalcode)
        time.sleep(2)

    def fill_contact2_country(self, country):
        fill_contact2_country = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact2LocatorsPage.FILL_CONTACT2_COUNTRY))
        fill_contact2_country.send_keys(country)
        time.sleep(2)

    def fill_contact2_submit(self):
        fill_contact2_submit = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact2LocatorsPage.FILL_CONTACT2_SUBMIT))
        fill_contact2_submit.click()
        time.sleep(2)


class ClickAddNewContact2ActionsPage:
    def __init__(self, driver):
        self.driver = driver

    def click_add_new_contact2_icon(self, addnewcontact1):
        click_add_new_contact2_icon = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(ClickAddNewContact2LocatorsPage.CLICK_ADD_NEW_CONTACT2_ICON))
        click_add_new_contact2_icon.click()
        time.sleep(2)


class AddNewContact2ActionsPage:
    def __init__(self, driver):
        self.driver = driver

    def fill_contact2_firstname(self, firstname):
        fill_contact2_first_name = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact2LocatorsPage.FILL_CONTACT2_FIRST_NAME))
        fill_contact2_first_name.send_keys(firstname)
        time.sleep(2)

    def fill_contact2_lastname(self, lastname):
        fill_contact2_lastname = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact2LocatorsPage.FILL_CONTACT2_LAST_NAME))
        fill_contact2_lastname.send_keys(lastname)
        time.sleep(2)

    def fill_contact2_birthdate(self, birthday):
        fill_contact2_birthdate = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact2LocatorsPage.FILL_CONTACT2_BIRTHDATE))
        fill_contact2_birthdate.send_keys(birthday)
        time.sleep(2)

    def fill_contact2_email(self, email):
        fill_contact2_email = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact2LocatorsPage.FILL_CONTACT2_EMAIL))
        fill_contact2_email.send_keys(email)
        time.sleep(2)

    def fill_contact2_phone(self, phone):
        fill_contact2_phone = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact2LocatorsPage.FILL_CONTACT2_PHONE))
        fill_contact2_phone.send_keys(phone)
        time.sleep(2)

    def fill_contact2_street1(self, street1):
        fill_contact2_street1 = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact2LocatorsPage.FILL_CONTACT2_STREET1))
        fill_contact2_street1.send_keys(street1)
        time.sleep(2)

    def fill_contact2_street2(self, street2):
        fill_contact2_street2 = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact2LocatorsPage.FILL_CONTACT2_STREET2))
        fill_contact2_street2.send_keys(street2)
        time.sleep(2)

    def fill_contact2_city(self, city):
        fill_contact2_city = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact2LocatorsPage.FILL_CONTACT2_CITY))
        fill_contact2_city.send_keys(city)
        time.sleep(2)

    def fill_contact2_state(self, state):
        fill_contact2_state = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact2LocatorsPage.FILL_CONTACT2_STATE))
        fill_contact2_state.send_keys(state)
        time.sleep(2)

    def fill_contact2_postalcode(self, postalcode):
        fill_contact2_postalcode = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact2LocatorsPage.FILL_CONTACT2_POSTALCODE))
        fill_contact2_postalcode.send_keys(postalcode)
        time.sleep(2)

    def fill_contact2_country(self, country):
        fill_contact2_country = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact2LocatorsPage.FILL_CONTACT2_COUNTRY))
        fill_contact2_country.send_keys(country)
        time.sleep(2)

    def fill_contact2_submit(self):
        fill_contact2_submit = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact2LocatorsPage.FILL_CONTACT2_SUBMIT))
        fill_contact2_submit.click()
        time.sleep(2)


class ClickAddNewContact2ActionsPage:
    def __init__(self, driver):
        self.driver = driver

    def click_add_new_contact2_icon(self, addnewcontact1):
        click_add_new_contact2_icon = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(ClickAddNewContact2LocatorsPage.CLICK_ADD_NEW_CONTACT2_ICON))
        click_add_new_contact2_icon.click()
        time.sleep(2)


class AddNewContact2ActionsPage:
    def __init__(self, driver):
        self.driver = driver

    def fill_contact2_firstname(self, firstname):
        fill_contact2_first_name = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact2LocatorsPage.FILL_CONTACT2_FIRST_NAME))
        fill_contact2_first_name.send_keys(firstname)
        time.sleep(2)

    def fill_contact2_lastname(self, lastname):
        fill_contact2_lastname = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact2LocatorsPage.FILL_CONTACT2_LAST_NAME))
        fill_contact2_lastname.send_keys(lastname)
        time.sleep(2)

    def fill_contact2_birthdate(self, birthday):
        fill_contact2_birthdate = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact2LocatorsPage.FILL_CONTACT2_BIRTHDATE))
        fill_contact2_birthdate.send_keys(birthday)
        time.sleep(2)

    def fill_contact2_email(self, email):
        fill_contact2_email = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact2LocatorsPage.FILL_CONTACT2_EMAIL))
        fill_contact2_email.send_keys(email)
        time.sleep(2)

    def fill_contact2_phone(self, phone):
        fill_contact2_phone = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact2LocatorsPage.FILL_CONTACT2_PHONE))
        fill_contact2_phone.send_keys(phone)
        time.sleep(2)

    def fill_contact2_street1(self, street1):
        fill_contact2_street1 = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact2LocatorsPage.FILL_CONTACT2_STREET1))
        fill_contact2_street1.send_keys(street1)
        time.sleep(2)

    def fill_contact2_street2(self, street2):
        fill_contact2_street2 = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact2LocatorsPage.FILL_CONTACT2_STREET2))
        fill_contact2_street2.send_keys(street2)
        time.sleep(2)

    def fill_contact2_city(self, city):
        fill_contact2_city = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact2LocatorsPage.FILL_CONTACT2_CITY))
        fill_contact2_city.send_keys(city)
        time.sleep(2)

    def fill_contact2_state(self, state):
        fill_contact2_state = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact2LocatorsPage.FILL_CONTACT2_STATE))
        fill_contact2_state.send_keys(state)
        time.sleep(2)

    def fill_contact2_postalcode(self, postalcode):
        fill_contact2_postalcode = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact2LocatorsPage.FILL_CONTACT2_POSTALCODE))
        fill_contact2_postalcode.send_keys(postalcode)
        time.sleep(2)

    def fill_contact2_country(self, country):
        fill_contact2_country = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact2LocatorsPage.FILL_CONTACT2_COUNTRY))
        fill_contact2_country.send_keys(country)
        time.sleep(2)

    def fill_contact2_submit(self):
        fill_contact2_submit = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact2LocatorsPage.FILL_CONTACT2_SUBMIT))
        fill_contact2_submit.click()
        time.sleep(2)


class ClickAddNewContact2ActionsPage:
    def __init__(self, driver):
        self.driver = driver

    def click_add_new_contact2_icon(self, addnewcontact1):
        click_add_new_contact2_icon = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(ClickAddNewContact2LocatorsPage.CLICK_ADD_NEW_CONTACT2_ICON))
        click_add_new_contact2_icon.click()
        time.sleep(2)


class AddNewContact2ActionsPage:
    def __init__(self, driver):
        self.driver = driver

    def fill_contact2_firstname(self, firstname):
        fill_contact2_first_name = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact2LocatorsPage.FILL_CONTACT2_FIRST_NAME))
        fill_contact2_first_name.send_keys(firstname)
        time.sleep(2)

    def fill_contact2_lastname(self, lastname):
        fill_contact2_lastname = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact2LocatorsPage.FILL_CONTACT2_LAST_NAME))
        fill_contact2_lastname.send_keys(lastname)
        time.sleep(2)

    def fill_contact2_birthdate(self, birthday):
        fill_contact2_birthdate = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact2LocatorsPage.FILL_CONTACT2_BIRTHDATE))
        fill_contact2_birthdate.send_keys(birthday)
        time.sleep(2)

    def fill_contact2_email(self, email):
        fill_contact2_email = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact2LocatorsPage.FILL_CONTACT2_EMAIL))
        fill_contact2_email.send_keys(email)
        time.sleep(2)

    def fill_contact2_phone(self, phone):
        fill_contact2_phone = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact2LocatorsPage.FILL_CONTACT2_PHONE))
        fill_contact2_phone.send_keys(phone)
        time.sleep(2)

    def fill_contact2_street1(self, street1):
        fill_contact2_street1 = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact2LocatorsPage.FILL_CONTACT2_STREET1))
        fill_contact2_street1.send_keys(street1)
        time.sleep(2)

    def fill_contact2_street2(self, street2):
        fill_contact2_street2 = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact2LocatorsPage.FILL_CONTACT2_STREET2))
        fill_contact2_street2.send_keys(street2)
        time.sleep(2)

    def fill_contact2_city(self, city):
        fill_contact2_city = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact2LocatorsPage.FILL_CONTACT2_CITY))
        fill_contact2_city.send_keys(city)
        time.sleep(2)

    def fill_contact2_state(self, state):
        fill_contact2_state = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact2LocatorsPage.FILL_CONTACT2_STATE))
        fill_contact2_state.send_keys(state)
        time.sleep(2)

    def fill_contact2_postalcode(self, postalcode):
        fill_contact2_postalcode = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact2LocatorsPage.FILL_CONTACT2_POSTALCODE))
        fill_contact2_postalcode.send_keys(postalcode)
        time.sleep(2)

    def fill_contact2_country(self, country):
        fill_contact2_country = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact2LocatorsPage.FILL_CONTACT2_COUNTRY))
        fill_contact2_country.send_keys(country)
        time.sleep(2)

    def fill_contact2_submit(self):
        fill_contact2_submit = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact2LocatorsPage.FILL_CONTACT2_SUBMIT))
        fill_contact2_submit.click()
        time.sleep(2)


class ClickAddNewContact2ActionsPage:
    def __init__(self, driver):
        self.driver = driver

    def click_add_new_contact2_icon(self, addnewcontact1):
        click_add_new_contact2_icon = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(ClickAddNewContact2LocatorsPage.CLICK_ADD_NEW_CONTACT2_ICON))
        click_add_new_contact2_icon.click()
        time.sleep(2)


class AddNewContact2ActionsPage:
    def __init__(self, driver):
        self.driver = driver

    def fill_contact2_firstname(self, firstname):
        fill_contact2_first_name = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact2LocatorsPage.FILL_CONTACT2_FIRST_NAME))
        fill_contact2_first_name.send_keys(firstname)
        time.sleep(2)

    def fill_contact2_lastname(self, lastname):
        fill_contact2_lastname = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact2LocatorsPage.FILL_CONTACT2_LAST_NAME))
        fill_contact2_lastname.send_keys(lastname)
        time.sleep(2)

    def fill_contact2_birthdate(self, birthday):
        fill_contact2_birthdate = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact2LocatorsPage.FILL_CONTACT2_BIRTHDATE))
        fill_contact2_birthdate.send_keys(birthday)
        time.sleep(2)

    def fill_contact2_email(self, email):
        fill_contact2_email = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact2LocatorsPage.FILL_CONTACT2_EMAIL))
        fill_contact2_email.send_keys(email)
        time.sleep(2)

    def fill_contact2_phone(self, phone):
        fill_contact2_phone = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact2LocatorsPage.FILL_CONTACT2_PHONE))
        fill_contact2_phone.send_keys(phone)
        time.sleep(2)

    def fill_contact2_street1(self, street1):
        fill_contact2_street1 = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact2LocatorsPage.FILL_CONTACT2_STREET1))
        fill_contact2_street1.send_keys(street1)
        time.sleep(2)

    def fill_contact2_street2(self, street2):
        fill_contact2_street2 = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact2LocatorsPage.FILL_CONTACT2_STREET2))
        fill_contact2_street2.send_keys(street2)
        time.sleep(2)

    def fill_contact2_city(self, city):
        fill_contact2_city = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact2LocatorsPage.FILL_CONTACT2_CITY))
        fill_contact2_city.send_keys(city)
        time.sleep(2)

    def fill_contact2_state(self, state):
        fill_contact2_state = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact2LocatorsPage.FILL_CONTACT2_STATE))
        fill_contact2_state.send_keys(state)
        time.sleep(2)

    def fill_contact2_postalcode(self, postalcode):
        fill_contact2_postalcode = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact2LocatorsPage.FILL_CONTACT2_POSTALCODE))
        fill_contact2_postalcode.send_keys(postalcode)
        time.sleep(2)

    def fill_contact2_country(self, country):
        fill_contact2_country = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact2LocatorsPage.FILL_CONTACT2_COUNTRY))
        fill_contact2_country.send_keys(country)
        time.sleep(2)

    def fill_contact2_submit(self):
        fill_contact2_submit = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact2LocatorsPage.FILL_CONTACT2_SUBMIT))
        fill_contact2_submit.click()
        time.sleep(2)


class ClickAddNewContact2ActionsPage:
    def __init__(self, driver):
        self.driver = driver

    def click_add_new_contact2_icon(self, addnewcontact1):
        click_add_new_contact2_icon = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(ClickAddNewContact2LocatorsPage.CLICK_ADD_NEW_CONTACT2_ICON))
        click_add_new_contact2_icon.click()
        time.sleep(2)


class AddNewContact2ActionsPage:
    def __init__(self, driver):
        self.driver = driver

    def fill_contact2_firstname(self, firstname):
        fill_contact2_first_name = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact2LocatorsPage.FILL_CONTACT2_FIRST_NAME))
        fill_contact2_first_name.send_keys(firstname)
        time.sleep(2)

    def fill_contact2_lastname(self, lastname):
        fill_contact2_lastname = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact2LocatorsPage.FILL_CONTACT2_LAST_NAME))
        fill_contact2_lastname.send_keys(lastname)
        time.sleep(2)

    def fill_contact2_birthdate(self, birthday):
        fill_contact2_birthdate = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact2LocatorsPage.FILL_CONTACT2_BIRTHDATE))
        fill_contact2_birthdate.send_keys(birthday)
        time.sleep(2)

    def fill_contact2_email(self, email):
        fill_contact2_email = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact2LocatorsPage.FILL_CONTACT2_EMAIL))
        fill_contact2_email.send_keys(email)
        time.sleep(2)

    def fill_contact2_phone(self, phone):
        fill_contact2_phone = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact2LocatorsPage.FILL_CONTACT2_PHONE))
        fill_contact2_phone.send_keys(phone)
        time.sleep(2)

    def fill_contact2_street1(self, street1):
        fill_contact2_street1 = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact2LocatorsPage.FILL_CONTACT2_STREET1))
        fill_contact2_street1.send_keys(street1)
        time.sleep(2)

    def fill_contact2_street2(self, street2):
        fill_contact2_street2 = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact2LocatorsPage.FILL_CONTACT2_STREET2))
        fill_contact2_street2.send_keys(street2)
        time.sleep(2)

    def fill_contact2_city(self, city):
        fill_contact2_city = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact2LocatorsPage.FILL_CONTACT2_CITY))
        fill_contact2_city.send_keys(city)
        time.sleep(2)

    def fill_contact2_state(self, state):
        fill_contact2_state = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact2LocatorsPage.FILL_CONTACT2_STATE))
        fill_contact2_state.send_keys(state)
        time.sleep(2)

    def fill_contact2_postalcode(self, postalcode):
        fill_contact2_postalcode = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact2LocatorsPage.FILL_CONTACT2_POSTALCODE))
        fill_contact2_postalcode.send_keys(postalcode)
        time.sleep(2)

    def fill_contact2_country(self, country):
        fill_contact2_country = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact2LocatorsPage.FILL_CONTACT2_COUNTRY))
        fill_contact2_country.send_keys(country)
        time.sleep(2)

    def fill_contact2_submit(self):
        fill_contact2_submit = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact2LocatorsPage.FILL_CONTACT2_SUBMIT))
        fill_contact2_submit.click()
        time.sleep(2)
