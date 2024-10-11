import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from ActionPage.ActionsPage import InvalidLoginActionsPage, ValidLoginActionsPage, ClickAddNewContact1ActionsPage, \
    AddNewContact1ActionsPage, AddNewContact2ActionsPage, ClickAddNewContact2ActionsPage, \
    ClickAddNewContact3ActionsPage, AddNewContact3ActionsPage, AddNewContact4ActionsPage, AddNewContact5ActionsPage, \
    ClickAddNewContact6ActionsPage, AddNewContact6ActionsPage, ClickAddNewContact7ActionsPage, \
    AddNewContact7ActionsPage, ClickAddNewContact8ActionsPage, AddNewContact8ActionsPage, \
    ClickAddNewContact9ActionsPage, AddNewContact9ActionsPage, ClickAddNewContact10ActionsPage, \
    AddNewContact10ActionsPage, ClickAddNewContact4ActionsPage, ClickAddNewContact5ActionsPage, \
    ClickLogoutButtonActionPage
from Config.config import Config


@pytest.fixture(scope="module")
def driver_setup():
    chrome_options = Options()
    # Uncomment the line below to run in headless mode
    chrome_options.add_argument("--headless")  # Run Edge in headless mode
    chrome_options.add_argument("--disable-gpu")  # Optional: Disable GPU acceleration
    driver = webdriver.Edge(options=chrome_options)
    driver.implicitly_wait(20)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope="module")
def login(driver_setup):
    driver = driver_setup
    login_page = InvalidLoginActionsPage(driver)  # call the login class
    login_page.open_url(Config.BASE_URL)  # call the url
    return login_page


@pytest.fixture(scope="module")
def login1(driver_setup):
    driver = driver_setup
    login_page = ValidLoginActionsPage(driver)  # call the login class
    login_page.open_url1(Config.BASE_URL1)  # call the url
    return login_page


def test_invalid_Login_Credentials(login):
    login.enter_invalid_email(Config.ENTER_INVALID_EMAIL)
    login.enter_invalid_password(Config.ENTER_INVALID_PASSWORD)
    login.click_submit()


def test_valid_Login_Credentials(login1):
    login1.enter_valid_email(Config.ENTER_VALID_EMAIL)
    login1.enter_valid_password(Config.ENTER_VALID_PASSWORD)
    login1.click_submit1()


def test_click_add_contact1_icon(login1):
    addnewcontact1 = ClickAddNewContact1ActionsPage(login1.driver)
    addnewcontact1.click_add_new_contact1_icon()


def test_Add_New_Contact1_Details(login1):
    contact1_details = AddNewContact1ActionsPage(login1.driver)
    contact1_details.fill_contact1_firstname(Config.FILL_CONTACT1_FIRST_NAME)
    contact1_details.fill_contact1_lastname(Config.FILL_CONTACT1_LAST_NAME)
    contact1_details.fill_contact1_birthdate(Config.FILL_CONTACT1_BIRTHDATE)
    contact1_details.fill_contact1_email(Config.FILL_CONTACT1_EMAIL)
    contact1_details.fill_contact1_phone(Config.FILL_CONTACT1_PHONE)
    contact1_details.fill_contact1_street1(Config.FILL_CONTACT1_STREET1)
    contact1_details.fill_contact1_street2(Config.FILL_CONTACT1_STREET2)
    contact1_details.fill_contact1_city(Config.FILL_CONTACT1_CITY)
    contact1_details.fill_contact1_state(Config.FILL_CONTACT1_STATE)
    contact1_details.fill_contact1_postalcode(Config.FILL_CONTACT1_POSTALCODE)
    contact1_details.fill_contact1_country(Config.FILL_CONTACT1_COUNTRY)
    contact1_details.fill_contact1_submit()


def test_click_add_contact2_icon(login1):
    addnewcontact2 = ClickAddNewContact2ActionsPage(login1.driver)
    addnewcontact2.click_add_new_contact2_icon()


def test_Add_New_Contact2_Details(login1):
    contact2_details = AddNewContact2ActionsPage(login1.driver)
    contact2_details.fill_contact2_firstname(Config.FILL_CONTACT2_FIRST_NAME)
    contact2_details.fill_contact2_lastname(Config.FILL_CONTACT2_LAST_NAME)
    contact2_details.fill_contact2_birthdate(Config.FILL_CONTACT2_BIRTHDATE)
    contact2_details.fill_contact2_email(Config.FILL_CONTACT2_EMAIL)
    contact2_details.fill_contact2_phone(Config.FILL_CONTACT2_PHONE)
    contact2_details.fill_contact2_street1(Config.FILL_CONTACT2_STREET1)
    contact2_details.fill_contact2_street2(Config.FILL_CONTACT2_STREET2)
    contact2_details.fill_contact2_city(Config.FILL_CONTACT2_CITY)
    contact2_details.fill_contact2_state(Config.FILL_CONTACT2_STATE)
    contact2_details.fill_contact2_postalcode(Config.FILL_CONTACT2_POSTALCODE)
    contact2_details.fill_contact2_country(Config.FILL_CONTACT2_COUNTRY)
    contact2_details.fill_contact2_submit()


def test_click_add_contact3_icon(login1):
    addnewcontact3 = ClickAddNewContact3ActionsPage(login1.driver)
    addnewcontact3.click_add_new_contact3_icon()


def test_Add_New_Contact3_Details(login1):
    contact3_details = AddNewContact3ActionsPage(login1.driver)
    contact3_details.fill_contact3_firstname(Config.FILL_CONTACT3_FIRST_NAME)
    contact3_details.fill_contact3_lastname(Config.FILL_CONTACT3_LAST_NAME)
    contact3_details.fill_contact3_birthdate(Config.FILL_CONTACT3_BIRTHDATE)
    contact3_details.fill_contact3_email(Config.FILL_CONTACT3_EMAIL)
    contact3_details.fill_contact3_phone(Config.FILL_CONTACT3_PHONE)
    contact3_details.fill_contact3_street1(Config.FILL_CONTACT3_STREET1)
    contact3_details.fill_contact3_street2(Config.FILL_CONTACT3_STREET2)
    contact3_details.fill_contact3_city(Config.FILL_CONTACT3_CITY)
    contact3_details.fill_contact3_state(Config.FILL_CONTACT3_STATE)
    contact3_details.fill_contact3_postalcode(Config.FILL_CONTACT3_POSTALCODE)
    contact3_details.fill_contact3_country(Config.FILL_CONTACT3_COUNTRY)
    contact3_details.fill_contact3_submit()


def test_click_add_contact4_icon(login1):
    addnewcontact4 = ClickAddNewContact4ActionsPage(login1.driver)
    addnewcontact4.click_add_new_contact4_icon()


def test_Add_New_Contact4_Details(login1):
    contact4_details = AddNewContact4ActionsPage(login1.driver)
    contact4_details.fill_contact4_firstname(Config.FILL_CONTACT4_FIRST_NAME)
    contact4_details.fill_contact4_lastname(Config.FILL_CONTACT4_LAST_NAME)
    contact4_details.fill_contact4_birthdate(Config.FILL_CONTACT4_BIRTHDATE)
    contact4_details.fill_contact4_email(Config.FILL_CONTACT4_EMAIL)
    contact4_details.fill_contact4_phone(Config.FILL_CONTACT4_PHONE)
    contact4_details.fill_contact4_street1(Config.FILL_CONTACT4_STREET1)
    contact4_details.fill_contact4_street2(Config.FILL_CONTACT4_STREET2)
    contact4_details.fill_contact4_city(Config.FILL_CONTACT4_CITY)
    contact4_details.fill_contact4_state(Config.FILL_CONTACT4_STATE)
    contact4_details.fill_contact4_postalcode(Config.FILL_CONTACT4_POSTALCODE)
    contact4_details.fill_contact4_country(Config.FILL_CONTACT4_COUNTRY)
    contact4_details.fill_contact4_submit()


def test_click_add_contact5_icon(login1):
    addnewcontact5 = ClickAddNewContact5ActionsPage(login1.driver)
    addnewcontact5.click_add_new_contact5_icon()


def test_Add_New_Contact5_Details(login1):
    contact5_details = AddNewContact5ActionsPage(login1.driver)
    contact5_details.fill_contact5_firstname(Config.FILL_CONTACT5_FIRST_NAME)
    contact5_details.fill_contact5_lastname(Config.FILL_CONTACT5_LAST_NAME)
    contact5_details.fill_contact5_birthdate(Config.FILL_CONTACT5_BIRTHDATE)
    contact5_details.fill_contact5_email(Config.FILL_CONTACT5_EMAIL)
    contact5_details.fill_contact5_phone(Config.FILL_CONTACT5_PHONE)
    contact5_details.fill_contact5_street1(Config.FILL_CONTACT5_STREET1)
    contact5_details.fill_contact5_street2(Config.FILL_CONTACT5_STREET2)
    contact5_details.fill_contact5_city(Config.FILL_CONTACT5_CITY)
    contact5_details.fill_contact5_state(Config.FILL_CONTACT5_STATE)
    contact5_details.fill_contact5_postalcode(Config.FILL_CONTACT5_POSTALCODE)
    contact5_details.fill_contact5_country(Config.FILL_CONTACT5_COUNTRY)
    contact5_details.fill_contact5_submit()


def test_click_add_contact6_icon(login1):
    addnewcontact6 = ClickAddNewContact6ActionsPage(login1.driver)
    addnewcontact6.click_add_new_contact6_icon()


def test_Add_New_Contact6_Details(login1):
    contact6_details = AddNewContact6ActionsPage(login1.driver)
    contact6_details.fill_contact6_firstname(Config.FILL_CONTACT6_FIRST_NAME)
    contact6_details.fill_contact6_lastname(Config.FILL_CONTACT6_LAST_NAME)
    contact6_details.fill_contact6_birthdate(Config.FILL_CONTACT6_BIRTHDATE)
    contact6_details.fill_contact6_email(Config.FILL_CONTACT6_EMAIL)
    contact6_details.fill_contact6_phone(Config.FILL_CONTACT6_PHONE)
    contact6_details.fill_contact6_street1(Config.FILL_CONTACT6_STREET1)
    contact6_details.fill_contact6_street2(Config.FILL_CONTACT6_STREET2)
    contact6_details.fill_contact6_city(Config.FILL_CONTACT6_CITY)
    contact6_details.fill_contact6_state(Config.FILL_CONTACT6_STATE)
    contact6_details.fill_contact6_postalcode(Config.FILL_CONTACT6_POSTALCODE)
    contact6_details.fill_contact6_country(Config.FILL_CONTACT6_COUNTRY)
    contact6_details.fill_contact6_submit()


def test_click_add_contact7_icon(login1):
    addnewcontact7 = ClickAddNewContact7ActionsPage(login1.driver)
    addnewcontact7.click_add_new_contact7_icon()


def test_Add_New_Contact7_Details(login1):
    contact7_details = AddNewContact7ActionsPage(login1.driver)
    contact7_details.fill_contact7_firstname(Config.FILL_CONTACT7_FIRST_NAME)
    contact7_details.fill_contact7_lastname(Config.FILL_CONTACT7_LAST_NAME)
    contact7_details.fill_contact7_birthdate(Config.FILL_CONTACT7_BIRTHDATE)
    contact7_details.fill_contact7_email(Config.FILL_CONTACT7_EMAIL)
    contact7_details.fill_contact7_phone(Config.FILL_CONTACT7_PHONE)
    contact7_details.fill_contact7_street1(Config.FILL_CONTACT7_STREET1)
    contact7_details.fill_contact7_street2(Config.FILL_CONTACT7_STREET2)
    contact7_details.fill_contact7_city(Config.FILL_CONTACT7_CITY)
    contact7_details.fill_contact7_state(Config.FILL_CONTACT7_STATE)
    contact7_details.fill_contact7_postalcode(Config.FILL_CONTACT7_POSTALCODE)
    contact7_details.fill_contact7_country(Config.FILL_CONTACT7_COUNTRY)
    contact7_details.fill_contact7_submit()


def test_click_add_contact8_icon(login1):
    addnewcontact8 = ClickAddNewContact8ActionsPage(login1.driver)
    addnewcontact8.click_add_new_contact8_icon()


def test_Add_New_Contact8_Details(login1):
    contact8_details = AddNewContact8ActionsPage(login1.driver)
    contact8_details.fill_contact8_firstname(Config.FILL_CONTACT8_FIRST_NAME)
    contact8_details.fill_contact8_lastname(Config.FILL_CONTACT8_LAST_NAME)
    contact8_details.fill_contact8_birthdate(Config.FILL_CONTACT8_BIRTHDATE)
    contact8_details.fill_contact8_email(Config.FILL_CONTACT8_EMAIL)
    contact8_details.fill_contact8_phone(Config.FILL_CONTACT8_PHONE)
    contact8_details.fill_contact8_street1(Config.FILL_CONTACT8_STREET1)
    contact8_details.fill_contact8_street2(Config.FILL_CONTACT8_STREET2)
    contact8_details.fill_contact8_city(Config.FILL_CONTACT8_CITY)
    contact8_details.fill_contact8_state(Config.FILL_CONTACT8_STATE)
    contact8_details.fill_contact8_postalcode(Config.FILL_CONTACT8_POSTALCODE)
    contact8_details.fill_contact8_country(Config.FILL_CONTACT8_COUNTRY)
    contact8_details.fill_contact8_submit()


def test_click_add_contact9_icon(login1):
    addnewcontact9 = ClickAddNewContact9ActionsPage(login1.driver)
    addnewcontact9.click_add_new_contact9_icon()


def test_Add_New_Contact9_Details(login1):
    contact9_details = AddNewContact9ActionsPage(login1.driver)
    contact9_details.fill_contact9_firstname(Config.FILL_CONTACT9_FIRST_NAME)
    contact9_details.fill_contact9_lastname(Config.FILL_CONTACT9_LAST_NAME)
    contact9_details.fill_contact9_birthdate(Config.FILL_CONTACT9_BIRTHDATE)
    contact9_details.fill_contact9_email(Config.FILL_CONTACT9_EMAIL)
    contact9_details.fill_contact9_phone(Config.FILL_CONTACT9_PHONE)
    contact9_details.fill_contact9_street1(Config.FILL_CONTACT9_STREET1)
    contact9_details.fill_contact9_street2(Config.FILL_CONTACT9_STREET2)
    contact9_details.fill_contact9_city(Config.FILL_CONTACT9_CITY)
    contact9_details.fill_contact9_state(Config.FILL_CONTACT9_STATE)
    contact9_details.fill_contact9_postalcode(Config.FILL_CONTACT9_POSTALCODE)
    contact9_details.fill_contact9_country(Config.FILL_CONTACT9_COUNTRY)
    contact9_details.fill_contact9_submit()


def test_click_add_contact10_icon(login1):
    addnewcontact10 = ClickAddNewContact10ActionsPage(login1.driver)
    addnewcontact10.click_add_new_contact10_icon()


def test_Add_New_Contact10_Details(login1):
    contact10_details = AddNewContact10ActionsPage(login1.driver)
    contact10_details.fill_contact10_firstname(Config.FILL_CONTACT10_FIRST_NAME)
    contact10_details.fill_contact10_lastname(Config.FILL_CONTACT10_LAST_NAME)
    contact10_details.fill_contact10_birthdate(Config.FILL_CONTACT10_BIRTHDATE)
    contact10_details.fill_contact10_email(Config.FILL_CONTACT10_EMAIL)
    contact10_details.fill_contact10_phone(Config.FILL_CONTACT10_PHONE)
    contact10_details.fill_contact10_street1(Config.FILL_CONTACT10_STREET1)
    contact10_details.fill_contact10_street2(Config.FILL_CONTACT10_STREET2)
    contact10_details.fill_contact10_city(Config.FILL_CONTACT10_CITY)
    contact10_details.fill_contact10_state(Config.FILL_CONTACT10_STATE)
    contact10_details.fill_contact10_postalcode(Config.FILL_CONTACT10_POSTALCODE)
    contact10_details.fill_contact10_country(Config.FILL_CONTACT10_COUNTRY)
    contact10_details.fill_contact10_submit()


def test_click_logout_button(login1):
    clicklogout = ClickLogoutButtonActionPage(login1.driver)
    clicklogout.click_logout_button()

