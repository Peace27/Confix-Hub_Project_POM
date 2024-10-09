import time

from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

from LocatorPage.LocatorsPage import InvalidLoginLocatorsPage, ValidLoginLocatorsPage, ClickAddNewContact1LocatorsPage, \
    AddNewContact1LocatorsPage, ClickAddNewContact2LocatorsPage, AddNewContact2LocatorsPage, \
    ClickAddNewContact3LocatorsPage, AddNewContact3LocatorsPage, ClickAddNewContact4LocatorsPage, \
    AddNewContact4LocatorsPage, ClickAddNewContact5LocatorsPage, AddNewContact5LocatorsPage, \
    ClickAddNewContact6LocatorsPage, AddNewContact6LocatorsPage, ClickAddNewContact7LocatorsPage, \
    AddNewContact7LocatorsPage, ClickAddNewContact8LocatorsPage, AddNewContact8LocatorsPage, \
    ClickAddNewContact9LocatorsPage, AddNewContact9LocatorsPage, ClickAddNewContact10LocatorsPage, \
    AddNewContact10LocatorsPage, LogoutButtonLocationPage


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

    def open_url1(self, url1):
        self.driver.get(url1)

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

    def click_add_new_contact1_icon(self):
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

    def fill_contact1_birthdate(self, birthdate):
        fill_contact1_birthdate = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact1LocatorsPage.FILL_CONTACT1_BIRTHDATE))
        fill_contact1_birthdate.send_keys(birthdate)
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

    def click_add_new_contact2_icon(self):
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

    def fill_contact2_birthdate(self, birthdate):
        fill_contact2_birthdate = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact2LocatorsPage.FILL_CONTACT2_BIRTHDATE))
        fill_contact2_birthdate.send_keys(birthdate)
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

    def click_add_new_contact3_icon(self):
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

    def fill_contact3_birthdate(self, birthdate):
        fill_contact3_birthdate = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact3LocatorsPage.FILL_CONTACT3_BIRTHDATE))
        fill_contact3_birthdate.send_keys(birthdate)
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

    def click_add_new_contact4_icon(self):
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

    def fill_contact4_birthdate(self, birthdate):
        fill_contact4_birthdate = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact4LocatorsPage.FILL_CONTACT4_BIRTHDATE))
        fill_contact4_birthdate.send_keys(birthdate)
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

    def fill_contact4_street1(self, street1):
        fill_contact4_street1 = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact4LocatorsPage.FILL_CONTACT4_STREET1))
        fill_contact4_street1.send_keys(street1)
        time.sleep(2)

    def fill_contact4_street2(self, street2):
        fill_contact4_street2 = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact4LocatorsPage.FILL_CONTACT4_STREET2))
        fill_contact4_street2.send_keys(street2)
        time.sleep(2)

    def fill_contact4_city(self, city):
        fill_contact4_city = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact4LocatorsPage.FILL_CONTACT4_CITY))
        fill_contact4_city.send_keys(city)
        time.sleep(2)

    def fill_contact4_state(self, state):
        fill_contact4_state = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact4LocatorsPage.FILL_CONTACT4_STATE))
        fill_contact4_state.send_keys(state)
        time.sleep(2)

    def fill_contact4_postalcode(self, postalcode):
        fill_contact4_postalcode = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact4LocatorsPage.FILL_CONTACT4_POSTALCODE))
        fill_contact4_postalcode.send_keys(postalcode)
        time.sleep(2)

    def fill_contact4_country(self, country):
        fill_contact4_country = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact4LocatorsPage.FILL_CONTACT4_COUNTRY))
        fill_contact4_country.send_keys(country)
        time.sleep(2)

    def fill_contact4_submit(self):
        fill_contact4_submit = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact4LocatorsPage.FILL_CONTACT4_SUBMIT))
        fill_contact4_submit.click()
        time.sleep(2)


class ClickAddNewContact5ActionsPage:
    def __init__(self, driver):
        self.driver = driver

    def click_add_new_contact5_icon(self):
        click_add_new_contact5_icon = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(ClickAddNewContact5LocatorsPage.CLICK_ADD_NEW_CONTACT5_ICON))
        click_add_new_contact5_icon.click()
        time.sleep(2)


class AddNewContact5ActionsPage:
    def __init__(self, driver):
        self.driver = driver

    def fill_contact5_firstname(self, firstname):
        fill_contact5_first_name = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact5LocatorsPage.FILL_CONTACT5_FIRST_NAME))
        fill_contact5_first_name.send_keys(firstname)
        time.sleep(2)

    def fill_contact5_lastname(self, lastname):
        fill_contact5_lastname = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact5LocatorsPage.FILL_CONTACT5_LAST_NAME))
        fill_contact5_lastname.send_keys(lastname)
        time.sleep(2)

    def fill_contact5_birthdate(self, birthdate):
        fill_contact5_birthdate = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact5LocatorsPage.FILL_CONTACT5_BIRTHDATE))
        fill_contact5_birthdate.send_keys(birthdate)
        time.sleep(2)

    def fill_contact5_email(self, email):
        fill_contact5_email = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact5LocatorsPage.FILL_CONTACT5_EMAIL))
        fill_contact5_email.send_keys(email)
        time.sleep(2)

    def fill_contact5_phone(self, phone):
        fill_contact5_phone = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact5LocatorsPage.FILL_CONTACT5_PHONE))
        fill_contact5_phone.send_keys(phone)
        time.sleep(2)

    def fill_contact5_street1(self, street1):
        fill_contact5_street1 = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact5LocatorsPage.FILL_CONTACT5_STREET1))
        fill_contact5_street1.send_keys(street1)
        time.sleep(2)

    def fill_contact5_street2(self, street2):
        fill_contact5_street2 = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact5LocatorsPage.FILL_CONTACT5_STREET2))
        fill_contact5_street2.send_keys(street2)
        time.sleep(2)

    def fill_contact5_city(self, city):
        fill_contact5_city = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact5LocatorsPage.FILL_CONTACT5_CITY))
        fill_contact5_city.send_keys(city)
        time.sleep(2)

    def fill_contact5_state(self, state):
        fill_contact5_state = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact5LocatorsPage.FILL_CONTACT5_STATE))
        fill_contact5_state.send_keys(state)
        time.sleep(2)

    def fill_contact5_postalcode(self, postalcode):
        fill_contact5_postalcode = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact5LocatorsPage.FILL_CONTACT5_POSTALCODE))
        fill_contact5_postalcode.send_keys(postalcode)
        time.sleep(2)

    def fill_contact5_country(self, country):
        fill_contact5_country = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact5LocatorsPage.FILL_CONTACT5_COUNTRY))
        fill_contact5_country.send_keys(country)
        time.sleep(2)

    def fill_contact5_submit(self):
        fill_contact5_submit = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact5LocatorsPage.FILL_CONTACT5_SUBMIT))
        fill_contact5_submit.click()
        time.sleep(2)


class ClickAddNewContact6ActionsPage:
    def __init__(self, driver):
        self.driver = driver

    def click_add_new_contact6_icon(self):
        click_add_new_contact6_icon = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(ClickAddNewContact6LocatorsPage.CLICK_ADD_NEW_CONTACT6_ICON))
        click_add_new_contact6_icon.click()
        time.sleep(2)


class AddNewContact6ActionsPage:
    def __init__(self, driver):
        self.driver = driver

    def fill_contact6_firstname(self, firstname):
        fill_contact6_first_name = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact6LocatorsPage.FILL_CONTACT6_FIRST_NAME))
        fill_contact6_first_name.send_keys(firstname)
        time.sleep(2)

    def fill_contact6_lastname(self, lastname):
        fill_contact6_lastname = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact6LocatorsPage.FILL_CONTACT6_LAST_NAME))
        fill_contact6_lastname.send_keys(lastname)
        time.sleep(2)

    def fill_contact6_birthdate(self, birthdate):
        fill_contact6_birthdate = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact6LocatorsPage.FILL_CONTACT6_BIRTHDATE))
        fill_contact6_birthdate.send_keys(birthdate)
        time.sleep(2)

    def fill_contact6_email(self, email):
        fill_contact6_email = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact6LocatorsPage.FILL_CONTACT6_EMAIL))
        fill_contact6_email.send_keys(email)
        time.sleep(2)

    def fill_contact6_phone(self, phone):
        fill_contact6_phone = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact6LocatorsPage.FILL_CONTACT6_PHONE))
        fill_contact6_phone.send_keys(phone)
        time.sleep(2)

    def fill_contact6_street1(self, street1):
        fill_contact6_street1 = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact6LocatorsPage.FILL_CONTACT6_STREET1))
        fill_contact6_street1.send_keys(street1)
        time.sleep(2)

    def fill_contact6_street2(self, street2):
        fill_contact6_street2 = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact6LocatorsPage.FILL_CONTACT6_STREET2))
        fill_contact6_street2.send_keys(street2)
        time.sleep(2)

    def fill_contact6_city(self, city):
        fill_contact6_city = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact6LocatorsPage.FILL_CONTACT6_CITY))
        fill_contact6_city.send_keys(city)
        time.sleep(2)

    def fill_contact6_state(self, state):
        fill_contact6_state = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact6LocatorsPage.FILL_CONTACT6_STATE))
        fill_contact6_state.send_keys(state)
        time.sleep(2)

    def fill_contact6_postalcode(self, postalcode):
        fill_contact6_postalcode = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact6LocatorsPage.FILL_CONTACT6_POSTALCODE))
        fill_contact6_postalcode.send_keys(postalcode)
        time.sleep(2)

    def fill_contact6_country(self, country):
        fill_contact6_country = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact6LocatorsPage.FILL_CONTACT6_COUNTRY))
        fill_contact6_country.send_keys(country)
        time.sleep(2)

    def fill_contact6_submit(self):
        fill_contact6_submit = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact6LocatorsPage.FILL_CONTACT6_SUBMIT))
        fill_contact6_submit.click()
        time.sleep(2)


class ClickAddNewContact7ActionsPage:
    def __init__(self, driver):
        self.driver = driver

    def click_add_new_contact7_icon(self):
        click_add_new_contact7_icon = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(ClickAddNewContact7LocatorsPage.CLICK_ADD_NEW_CONTACT7_ICON))
        click_add_new_contact7_icon.click()
        time.sleep(2)


class AddNewContact7ActionsPage:
    def __init__(self, driver):
        self.driver = driver

    def fill_contact7_firstname(self, firstname):
        fill_contact7_first_name = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact7LocatorsPage.FILL_CONTACT7_FIRST_NAME))
        fill_contact7_first_name.send_keys(firstname)
        time.sleep(2)

    def fill_contact7_lastname(self, lastname):
        fill_contact7_lastname = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact7LocatorsPage.FILL_CONTACT7_LAST_NAME))
        fill_contact7_lastname.send_keys(lastname)
        time.sleep(2)

    def fill_contact7_birthdate(self, birthdate):
        fill_contact7_birthdate = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact7LocatorsPage.FILL_CONTACT7_BIRTHDATE))
        fill_contact7_birthdate.send_keys(birthdate)
        time.sleep(2)

    def fill_contact7_email(self, email):
        fill_contact7_email = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact7LocatorsPage.FILL_CONTACT7_EMAIL))
        fill_contact7_email.send_keys(email)
        time.sleep(2)

    def fill_contact7_phone(self, phone):
        fill_contact7_phone = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact7LocatorsPage.FILL_CONTACT7_PHONE))
        fill_contact7_phone.send_keys(phone)
        time.sleep(2)

    def fill_contact7_street1(self, street1):
        fill_contact7_street1 = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact7LocatorsPage.FILL_CONTACT7_STREET1))
        fill_contact7_street1.send_keys(street1)
        time.sleep(2)

    def fill_contact7_street2(self, street2):
        fill_contact7_street2 = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact7LocatorsPage.FILL_CONTACT7_STREET2))
        fill_contact7_street2.send_keys(street2)
        time.sleep(2)

    def fill_contact7_city(self, city):
        fill_contact7_city = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact7LocatorsPage.FILL_CONTACT7_CITY))
        fill_contact7_city.send_keys(city)
        time.sleep(2)

    def fill_contact7_state(self, state):
        fill_contact7_state = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact7LocatorsPage.FILL_CONTACT7_STATE))
        fill_contact7_state.send_keys(state)
        time.sleep(2)

    def fill_contact7_postalcode(self, postalcode):
        fill_contact7_postalcode = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact7LocatorsPage.FILL_CONTACT7_POSTALCODE))
        fill_contact7_postalcode.send_keys(postalcode)
        time.sleep(2)

    def fill_contact7_country(self, country):
        fill_contact7_country = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact7LocatorsPage.FILL_CONTACT7_COUNTRY))
        fill_contact7_country.send_keys(country)
        time.sleep(2)

    def fill_contact7_submit(self):
        fill_contact7_submit = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact7LocatorsPage.FILL_CONTACT7_SUBMIT))
        fill_contact7_submit.click()
        time.sleep(2)


class ClickAddNewContact8ActionsPage:
    def __init__(self, driver):
        self.driver = driver

    def click_add_new_contact8_icon(self):
        click_add_new_contact8_icon = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(ClickAddNewContact8LocatorsPage.CLICK_ADD_NEW_CONTACT8_ICON))
        click_add_new_contact8_icon.click()
        time.sleep(2)


class AddNewContact8ActionsPage:
    def __init__(self, driver):
        self.driver = driver

    def fill_contact8_firstname(self, firstname):
        fill_contact8_first_name = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact8LocatorsPage.FILL_CONTACT8_FIRST_NAME))
        fill_contact8_first_name.send_keys(firstname)
        time.sleep(2)

    def fill_contact8_lastname(self, lastname):
        fill_contact8_lastname = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact8LocatorsPage.FILL_CONTACT8_LAST_NAME))
        fill_contact8_lastname.send_keys(lastname)
        time.sleep(2)

    def fill_contact8_birthdate(self, birthdate):
        fill_contact8_birthdate = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact8LocatorsPage.FILL_CONTACT8_BIRTHDATE))
        fill_contact8_birthdate.send_keys(birthdate)
        time.sleep(2)

    def fill_contact8_email(self, email):
        fill_contact8_email = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact8LocatorsPage.FILL_CONTACT8_EMAIL))
        fill_contact8_email.send_keys(email)
        time.sleep(2)

    def fill_contact8_phone(self, phone):
        fill_contact8_phone = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact8LocatorsPage.FILL_CONTACT8_PHONE))
        fill_contact8_phone.send_keys(phone)
        time.sleep(2)

    def fill_contact8_street1(self, street1):
        fill_contact8_street1 = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact8LocatorsPage.FILL_CONTACT8_STREET1))
        fill_contact8_street1.send_keys(street1)
        time.sleep(2)

    def fill_contact8_street2(self, street2):
        fill_contact8_street2 = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact8LocatorsPage.FILL_CONTACT8_STREET2))
        fill_contact8_street2.send_keys(street2)
        time.sleep(2)

    def fill_contact8_city(self, city):
        fill_contact8_city = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact8LocatorsPage.FILL_CONTACT8_CITY))
        fill_contact8_city.send_keys(city)
        time.sleep(2)

    def fill_contact8_state(self, state):
        fill_contact8_state = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact8LocatorsPage.FILL_CONTACT8_STATE))
        fill_contact8_state.send_keys(state)
        time.sleep(2)

    def fill_contact8_postalcode(self, postalcode):
        fill_contact8_postalcode = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact8LocatorsPage.FILL_CONTACT8_POSTALCODE))
        fill_contact8_postalcode.send_keys(postalcode)
        time.sleep(2)

    def fill_contact8_country(self, country):
        fill_contact8_country = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact8LocatorsPage.FILL_CONTACT8_COUNTRY))
        fill_contact8_country.send_keys(country)
        time.sleep(2)

    def fill_contact8_submit(self):
        fill_contact8_submit = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact8LocatorsPage.FILL_CONTACT8_SUBMIT))
        fill_contact8_submit.click()
        time.sleep(2)


class ClickAddNewContact9ActionsPage:
    def __init__(self, driver):
        self.driver = driver

    def click_add_new_contact9_icon(self):
        click_add_new_contact9_icon = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(ClickAddNewContact9LocatorsPage.CLICK_ADD_NEW_CONTACT9_ICON))
        click_add_new_contact9_icon.click()
        time.sleep(2)


class AddNewContact9ActionsPage:
    def __init__(self, driver):
        self.driver = driver

    def fill_contact9_firstname(self, firstname):
        fill_contact9_first_name = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact9LocatorsPage.FILL_CONTACT9_FIRST_NAME))
        fill_contact9_first_name.send_keys(firstname)
        time.sleep(2)

    def fill_contact9_lastname(self, lastname):
        fill_contact9_lastname = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact9LocatorsPage.FILL_CONTACT9_LAST_NAME))
        fill_contact9_lastname.send_keys(lastname)
        time.sleep(2)

    def fill_contact9_birthdate(self, birthdate):
        fill_contact9_birthdate = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact9LocatorsPage.FILL_CONTACT9_BIRTHDATE))
        fill_contact9_birthdate.send_keys(birthdate)
        time.sleep(2)

    def fill_contact9_email(self, email):
        fill_contact9_email = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact9LocatorsPage.FILL_CONTACT9_EMAIL))
        fill_contact9_email.send_keys(email)
        time.sleep(2)

    def fill_contact9_phone(self, phone):
        fill_contact9_phone = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact9LocatorsPage.FILL_CONTACT9_PHONE))
        fill_contact9_phone.send_keys(phone)
        time.sleep(2)

    def fill_contact9_street1(self, street1):
        fill_contact9_street1 = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact9LocatorsPage.FILL_CONTACT9_STREET1))
        fill_contact9_street1.send_keys(street1)
        time.sleep(2)

    def fill_contact9_street2(self, street2):
        fill_contact9_street2 = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact9LocatorsPage.FILL_CONTACT9_STREET2))
        fill_contact9_street2.send_keys(street2)
        time.sleep(2)

    def fill_contact9_city(self, city):
        fill_contact9_city = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact9LocatorsPage.FILL_CONTACT9_CITY))
        fill_contact9_city.send_keys(city)
        time.sleep(2)

    def fill_contact9_state(self, state):
        fill_contact9_state = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact9LocatorsPage.FILL_CONTACT9_STATE))
        fill_contact9_state.send_keys(state)
        time.sleep(2)

    def fill_contact9_postalcode(self, postalcode):
        fill_contact9_postalcode = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact9LocatorsPage.FILL_CONTACT9_POSTALCODE))
        fill_contact9_postalcode.send_keys(postalcode)
        time.sleep(2)

    def fill_contact9_country(self, country):
        fill_contact9_country = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact9LocatorsPage.FILL_CONTACT9_COUNTRY))
        fill_contact9_country.send_keys(country)
        time.sleep(2)

    def fill_contact9_submit(self):
        fill_contact9_submit = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact9LocatorsPage.FILL_CONTACT9_SUBMIT))
        fill_contact9_submit.click()
        time.sleep(2)


class ClickAddNewContact10ActionsPage:
    def __init__(self, driver):
        self.driver = driver

    def click_add_new_contact10_icon(self):
        click_add_new_contact10_icon = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(ClickAddNewContact10LocatorsPage.CLICK_ADD_NEW_CONTACT10_ICON))
        click_add_new_contact10_icon.click()
        time.sleep(2)


class AddNewContact10ActionsPage:
    def __init__(self, driver):
        self.driver = driver

    def fill_contact10_firstname(self, firstname):
        fill_contact10_first_name = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact10LocatorsPage.FILL_CONTACT10_FIRST_NAME))
        fill_contact10_first_name.send_keys(firstname)
        time.sleep(2)

    def fill_contact10_lastname(self, lastname):
        fill_contact10_lastname = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact10LocatorsPage.FILL_CONTACT10_LAST_NAME))
        fill_contact10_lastname.send_keys(lastname)
        time.sleep(2)

    def fill_contact10_birthdate(self, birthdate):
        fill_contact10_birthdate = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact10LocatorsPage.FILL_CONTACT10_BIRTHDATE))
        fill_contact10_birthdate.send_keys(birthdate)
        time.sleep(2)

    def fill_contact10_email(self, email):
        fill_contact10_email = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact10LocatorsPage.FILL_CONTACT10_EMAIL))
        fill_contact10_email.send_keys(email)
        time.sleep(2)

    def fill_contact10_phone(self, phone):
        fill_contact10_phone = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact10LocatorsPage.FILL_CONTACT10_PHONE))
        fill_contact10_phone.send_keys(phone)
        time.sleep(2)

    def fill_contact10_street1(self, street1):
        fill_contact10_street1 = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact10LocatorsPage.FILL_CONTACT10_STREET1))
        fill_contact10_street1.send_keys(street1)
        time.sleep(2)

    def fill_contact10_street2(self, street2):
        fill_contact10_street2 = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact10LocatorsPage.FILL_CONTACT10_STREET2))
        fill_contact10_street2.send_keys(street2)
        time.sleep(2)

    def fill_contact10_city(self, city):
        fill_contact10_city = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact10LocatorsPage.FILL_CONTACT10_CITY))
        fill_contact10_city.send_keys(city)
        time.sleep(2)

    def fill_contact10_state(self, state):
        fill_contact10_state = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact10LocatorsPage.FILL_CONTACT10_STATE))
        fill_contact10_state.send_keys(state)
        time.sleep(2)

    def fill_contact10_postalcode(self, postalcode):
        fill_contact10_postalcode = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact10LocatorsPage.FILL_CONTACT10_POSTALCODE))
        fill_contact10_postalcode.send_keys(postalcode)
        time.sleep(2)

    def fill_contact10_country(self, country):
        fill_contact10_country = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact10LocatorsPage.FILL_CONTACT10_COUNTRY))
        fill_contact10_country.send_keys(country)
        time.sleep(2)

    def fill_contact10_submit(self):
        fill_contact10_submit = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewContact10LocatorsPage.FILL_CONTACT10_SUBMIT))
        fill_contact10_submit.click()
        time.sleep(2)


class ClickLogoutButtonActionPage:

    def __init__(self, driver):
        self.driver = driver

    def click_logout_button(self):
        click_logout_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(LogoutButtonLocationPage.CLICK_LOGOUT_BUTTON))
        click_logout_button.click()
        time.sleep(2)
