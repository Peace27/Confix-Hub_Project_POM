import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from ActionPage.ActionsPage import InvalidLoginActionsPage, ValidLoginActionsPage, ClickAddNewContact1ActionsPage, \
    AddNewContact1ActionsPage, AddNewContact2ActionsPage, ClickAddNewContact2ActionsPage


@pytest.fixture(scope="module")
def driver_setup():
    chrome_options = Options()
    # Uncomment the line below to run in headless mode
    # chrome_options.add_argument("--headless")  # Run Chrome in headless mode
    # chrome_options.add_argument("--disable-gpu")  # Optional: Disable GPU acceleration
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(20)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope="module")
def login(driver_setup):
    driver = driver_setup
    login_page = InvalidLoginActionsPage(driver)  # call the login class
    login_page.open_url("https://thinking-tester-contact-list.herokuapp.com/")  # call the url
    return login_page


@pytest.fixture(scope="module")
def login1(driver_setup):
    driver = driver_setup
    login_page = ValidLoginActionsPage(driver)  # call the login class
    login_page.open_url1("https://thinking-tester-contact-list.herokuapp.com/")  # call the url
    return login_page


def test_invalid_Login_Credentials(login):
    login.enter_invalid_email("peace@gmail.com")
    login.enter_invalid_password("Admin123")
    login.click_submit()


def test_valid_Login_Credentials(login1):
    login1.enter_valid_email("peace01@gmail.com")
    login1.enter_valid_password("Admin123")
    login1.click_submit1()


def test_click_add_contact1_icon(login1):
    addnewcontact1 = ClickAddNewContact1ActionsPage(login1.driver)
    addnewcontact1.click_add_new_contact1_icon("")


def test_Add_New_Contact1_Details(login1):
    contact1_details = AddNewContact1ActionsPage(login1.driver)
    contact1_details.fill_contact1_firstname("Shane")
    contact1_details.fill_contact1_lastname("Jakes")
    contact1_details.fill_contact1_birthdate("2020-01-01")
    contact1_details.fill_contact1_email("peace1@gmail.com")
    contact1_details.fill_contact1_phone("8022805621")
    contact1_details.fill_contact1_street1("House 1, London Street")
    contact1_details.fill_contact1_street2("House 1, Scotland Street")
    contact1_details.fill_contact1_city("Ikeja")
    contact1_details.fill_contact1_state("Lagos")
    contact1_details.fill_contact1_postalcode("01234")
    contact1_details.fill_contact1_country("Nigeria")
    contact1_details.fill_contact1_submit()


def test_click_add_contact2_icon(login1):
    addnewcontact2 = ClickAddNewContact2ActionsPage(login1.driver)
    addnewcontact2.click_add_new_contact2_icon("")


def test_Add_New_Contact2_Details(login1):
    contact2_details = AddNewContact2ActionsPage(login1.driver)
    contact2_details.fill_contact2_firstname("Jack")
    contact2_details.fill_contact2_lastname("Chan")
    contact2_details.fill_contact2_birthdate("2021-01-01")
    contact2_details.fill_contact2_email("peace2@gmail.com")
    contact2_details.fill_contact2_phone("8022805622")
    contact2_details.fill_contact2_street1("House 2, London Street")
    contact2_details.fill_contact2_street2("House 2, Scotland Street")
    contact2_details.fill_contact2_city("Lekki")
    contact2_details.fill_contact2_state("Lagos")
    contact2_details.fill_contact2_postalcode("01234")
    contact2_details.fill_contact2_country("Nigeria")
    contact2_details.fill_contact2_submit()

#
# def test_Add_New_Contact1_Details(login1):
#     contact1_details = AddNewContact1ActionsPage(login1.driver)
#     contact1_details.fill_contact1_firstname("Shane")
#     contact1_details.fill_contact1_lastname("Jakes")
#     contact1_details.fill_contact1_birthdate("2020-01-01")
#     contact1_details.fill_contact1_email("peace1@gmail.com")
#     contact1_details.fill_contact1_phone("8022805621")
#     contact1_details.fill_contact1_street1("House 1, London Street")
#     contact1_details.fill_contact1_street2("House 1, Scotland Street")
#     contact1_details.fill_contact1_city("Ikeja")
#     contact1_details.fill_contact1_state("Lagos")
#     contact1_details.fill_contact1_postalcode("01234")
#     contact1_details.fill_contact1_country("Nigeria")
#     contact1_details.fill_contact1_submit()
#
#
# def test_Add_New_Contact1_Details(login1):
#     contact1_details = AddNewContact1ActionsPage(login1.driver)
#     contact1_details.fill_contact1_firstname("Shane")
#     contact1_details.fill_contact1_lastname("Jakes")
#     contact1_details.fill_contact1_birthdate("2020-01-01")
#     contact1_details.fill_contact1_email("peace1@gmail.com")
#     contact1_details.fill_contact1_phone("8022805621")
#     contact1_details.fill_contact1_street1("House 1, London Street")
#     contact1_details.fill_contact1_street2("House 1, Scotland Street")
#     contact1_details.fill_contact1_city("Ikeja")
#     contact1_details.fill_contact1_state("Lagos")
#     contact1_details.fill_contact1_postalcode("01234")
#     contact1_details.fill_contact1_country("Nigeria")
#     contact1_details.fill_contact1_submit()
#
#
# def test_Add_New_Contact1_Details(login1):
#     contact1_details = AddNewContact1ActionsPage(login1.driver)
#     contact1_details.fill_contact1_firstname("Shane")
#     contact1_details.fill_contact1_lastname("Jakes")
#     contact1_details.fill_contact1_birthdate("2020-01-01")
#     contact1_details.fill_contact1_email("peace1@gmail.com")
#     contact1_details.fill_contact1_phone("8022805621")
#     contact1_details.fill_contact1_street1("House 1, London Street")
#     contact1_details.fill_contact1_street2("House 1, Scotland Street")
#     contact1_details.fill_contact1_city("Ikeja")
#     contact1_details.fill_contact1_state("Lagos")
#     contact1_details.fill_contact1_postalcode("01234")
#     contact1_details.fill_contact1_country("Nigeria")
#     contact1_details.fill_contact1_submit()

def test_click_add_contact2_icon(login1):
    addnewcontact2 = ClickAddNewContact2ActionsPage(login1.driver)
    addnewcontact2.click_add_new_contact2_icon("")


def test_Add_New_Contact2_Details(login1):
    contact2_details = AddNewContact2ActionsPage(login1.driver)
    contact2_details.fill_contact2_firstname("Jack")
    contact2_details.fill_contact2_lastname("Chan")
    contact2_details.fill_contact2_birthdate("2021-01-01")
    contact2_details.fill_contact2_email("peace2@gmail.com")
    contact2_details.fill_contact2_phone("8022805622")
    contact2_details.fill_contact2_street1("House 2, London Street")
    contact2_details.fill_contact2_street2("House 2, Scotland Street")
    contact2_details.fill_contact2_city("Lekki")
    contact2_details.fill_contact2_state("Lagos")
    contact2_details.fill_contact2_postalcode("01234")
    contact2_details.fill_contact2_country("Nigeria")
    contact2_details.fill_contact2_submit()

def test_click_add_contact2_icon(login1):
    addnewcontact2 = ClickAddNewContact2ActionsPage(login1.driver)
    addnewcontact2.click_add_new_contact2_icon("")


def test_Add_New_Contact2_Details(login1):
    contact2_details = AddNewContact2ActionsPage(login1.driver)
    contact2_details.fill_contact2_firstname("Jack")
    contact2_details.fill_contact2_lastname("Chan")
    contact2_details.fill_contact2_birthdate("2021-01-01")
    contact2_details.fill_contact2_email("peace2@gmail.com")
    contact2_details.fill_contact2_phone("8022805622")
    contact2_details.fill_contact2_street1("House 2, London Street")
    contact2_details.fill_contact2_street2("House 2, Scotland Street")
    contact2_details.fill_contact2_city("Lekki")
    contact2_details.fill_contact2_state("Lagos")
    contact2_details.fill_contact2_postalcode("01234")
    contact2_details.fill_contact2_country("Nigeria")
    contact2_details.fill_contact2_submit()

def test_click_add_contact2_icon(login1):
    addnewcontact2 = ClickAddNewContact2ActionsPage(login1.driver)
    addnewcontact2.click_add_new_contact2_icon("")


def test_Add_New_Contact2_Details(login1):
    contact2_details = AddNewContact2ActionsPage(login1.driver)
    contact2_details.fill_contact2_firstname("Jack")
    contact2_details.fill_contact2_lastname("Chan")
    contact2_details.fill_contact2_birthdate("2021-01-01")
    contact2_details.fill_contact2_email("peace2@gmail.com")
    contact2_details.fill_contact2_phone("8022805622")
    contact2_details.fill_contact2_street1("House 2, London Street")
    contact2_details.fill_contact2_street2("House 2, Scotland Street")
    contact2_details.fill_contact2_city("Lekki")
    contact2_details.fill_contact2_state("Lagos")
    contact2_details.fill_contact2_postalcode("01234")
    contact2_details.fill_contact2_country("Nigeria")
    contact2_details.fill_contact2_submit()

def test_click_add_contact2_icon(login1):
    addnewcontact2 = ClickAddNewContact2ActionsPage(login1.driver)
    addnewcontact2.click_add_new_contact2_icon("")


def test_Add_New_Contact2_Details(login1):
    contact2_details = AddNewContact2ActionsPage(login1.driver)
    contact2_details.fill_contact2_firstname("Jack")
    contact2_details.fill_contact2_lastname("Chan")
    contact2_details.fill_contact2_birthdate("2021-01-01")
    contact2_details.fill_contact2_email("peace2@gmail.com")
    contact2_details.fill_contact2_phone("8022805622")
    contact2_details.fill_contact2_street1("House 2, London Street")
    contact2_details.fill_contact2_street2("House 2, Scotland Street")
    contact2_details.fill_contact2_city("Lekki")
    contact2_details.fill_contact2_state("Lagos")
    contact2_details.fill_contact2_postalcode("01234")
    contact2_details.fill_contact2_country("Nigeria")
    contact2_details.fill_contact2_submit()

def test_click_add_contact2_icon(login1):
    addnewcontact2 = ClickAddNewContact2ActionsPage(login1.driver)
    addnewcontact2.click_add_new_contact2_icon("")


def test_Add_New_Contact2_Details(login1):
    contact2_details = AddNewContact2ActionsPage(login1.driver)
    contact2_details.fill_contact2_firstname("Jack")
    contact2_details.fill_contact2_lastname("Chan")
    contact2_details.fill_contact2_birthdate("2021-01-01")
    contact2_details.fill_contact2_email("peace2@gmail.com")
    contact2_details.fill_contact2_phone("8022805622")
    contact2_details.fill_contact2_street1("House 2, London Street")
    contact2_details.fill_contact2_street2("House 2, Scotland Street")
    contact2_details.fill_contact2_city("Lekki")
    contact2_details.fill_contact2_state("Lagos")
    contact2_details.fill_contact2_postalcode("01234")
    contact2_details.fill_contact2_country("Nigeria")
    contact2_details.fill_contact2_submit()
