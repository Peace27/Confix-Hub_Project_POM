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
    addnewcontact1.click_add_new_contact1_icon()


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
    addnewcontact2.click_add_new_contact2_icon()


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


def test_click_add_contact3_icon(login1):
    addnewcontact3 = ClickAddNewContact3ActionsPage(login1.driver)
    addnewcontact3.click_add_new_contact3_icon()


def test_Add_New_Contact3_Details(login1):
    contact3_details = AddNewContact3ActionsPage(login1.driver)
    contact3_details.fill_contact3_firstname("Ayo")
    contact3_details.fill_contact3_lastname("Ade")
    contact3_details.fill_contact3_birthdate("1990-01-01")
    contact3_details.fill_contact3_email("peace3@gmail.com")
    contact3_details.fill_contact3_phone("8022805623")
    contact3_details.fill_contact3_street1("House 3, London Street")
    contact3_details.fill_contact3_street2("House 3, Scotland Street")
    contact3_details.fill_contact3_city("Lekki")
    contact3_details.fill_contact3_state("Lagos")
    contact3_details.fill_contact3_postalcode("01234")
    contact3_details.fill_contact3_country("Nigeria")
    contact3_details.fill_contact3_submit()


def test_click_add_contact4_icon(login1):
    addnewcontact4 = ClickAddNewContact4ActionsPage(login1.driver)
    addnewcontact4.click_add_new_contact4_icon()


def test_Add_New_Contact4_Details(login1):
    contact4_details = AddNewContact4ActionsPage(login1.driver)
    contact4_details.fill_contact4_firstname("Ola")
    contact4_details.fill_contact4_lastname("Ola")
    contact4_details.fill_contact4_birthdate("1991-01-01")
    contact4_details.fill_contact4_email("peace4@gmail.com")
    contact4_details.fill_contact4_phone("8022805624")
    contact4_details.fill_contact4_street1("House 4, London Street")
    contact4_details.fill_contact4_street2("House 4, Scotland Street")
    contact4_details.fill_contact4_city("Lekki")
    contact4_details.fill_contact4_state("Lagos")
    contact4_details.fill_contact4_postalcode("01234")
    contact4_details.fill_contact4_country("Nigeria")
    contact4_details.fill_contact4_submit()


def test_click_add_contact5_icon(login1):
    addnewcontact5 = ClickAddNewContact5ActionsPage(login1.driver)
    addnewcontact5.click_add_new_contact5_icon()


def test_Add_New_Contact5_Details(login1):
    contact5_details = AddNewContact5ActionsPage(login1.driver)
    contact5_details.fill_contact5_firstname("Yemi")
    contact5_details.fill_contact5_lastname("Alade")
    contact5_details.fill_contact5_birthdate("2022-01-01")
    contact5_details.fill_contact5_email("peace5@gmail.com")
    contact5_details.fill_contact5_phone("8022805625")
    contact5_details.fill_contact5_street1("House 5, London Street")
    contact5_details.fill_contact5_street2("House 5, Scotland Street")
    contact5_details.fill_contact5_city("Lekki")
    contact5_details.fill_contact5_state("Lagos")
    contact5_details.fill_contact5_postalcode("01234")
    contact5_details.fill_contact5_country("Nigeria")
    contact5_details.fill_contact5_submit()


def test_click_add_contact6_icon(login1):
    addnewcontact6 = ClickAddNewContact6ActionsPage(login1.driver)
    addnewcontact6.click_add_new_contact6_icon()


def test_Add_New_Contact6_Details(login1):
    contact6_details = AddNewContact6ActionsPage(login1.driver)
    contact6_details.fill_contact6_firstname("Becky")
    contact6_details.fill_contact6_lastname("Ben")
    contact6_details.fill_contact6_birthdate("1995-01-01")
    contact6_details.fill_contact6_email("peace6@gmail.com")
    contact6_details.fill_contact6_phone("8022805626")
    contact6_details.fill_contact6_street1("House 6, London Street")
    contact6_details.fill_contact6_street2("House 6, Scotland Street")
    contact6_details.fill_contact6_city("Lekki")
    contact6_details.fill_contact6_state("Lagos")
    contact6_details.fill_contact6_postalcode("01234")
    contact6_details.fill_contact6_country("Nigeria")
    contact6_details.fill_contact6_submit()


def test_click_add_contact7_icon(login1):
    addnewcontact7 = ClickAddNewContact7ActionsPage(login1.driver)
    addnewcontact7.click_add_new_contact7_icon()


def test_Add_New_Contact7_Details(login1):
    contact7_details = AddNewContact7ActionsPage(login1.driver)
    contact7_details.fill_contact7_firstname("Ble")
    contact7_details.fill_contact7_lastname("Ble")
    contact7_details.fill_contact7_birthdate("1996-01-01")
    contact7_details.fill_contact7_email("peace7@gmail.com")
    contact7_details.fill_contact7_phone("8022805627")
    contact7_details.fill_contact7_street1("House 7, London Street")
    contact7_details.fill_contact7_street2("House 7, Scotland Street")
    contact7_details.fill_contact7_city("Lekki")
    contact7_details.fill_contact7_state("Lagos")
    contact7_details.fill_contact7_postalcode("01234")
    contact7_details.fill_contact7_country("Nigeria")
    contact7_details.fill_contact7_submit()


def test_click_add_contact8_icon(login1):
    addnewcontact8 = ClickAddNewContact8ActionsPage(login1.driver)
    addnewcontact8.click_add_new_contact8_icon()


def test_Add_New_Contact8_Details(login1):
    contact8_details = AddNewContact8ActionsPage(login1.driver)
    contact8_details.fill_contact8_firstname("Ella")
    contact8_details.fill_contact8_lastname("Paul")
    contact8_details.fill_contact8_birthdate("2022-01-01")
    contact8_details.fill_contact8_email("peace8@gmail.com")
    contact8_details.fill_contact8_phone("8022805628")
    contact8_details.fill_contact8_street1("House 8, London Street")
    contact8_details.fill_contact8_street2("House 8, Scotland Street")
    contact8_details.fill_contact8_city("Lekki")
    contact8_details.fill_contact8_state("Lagos")
    contact8_details.fill_contact8_postalcode("01234")
    contact8_details.fill_contact8_country("Nigeria")
    contact8_details.fill_contact8_submit()


def test_click_add_contact9_icon(login1):
    addnewcontact9 = ClickAddNewContact9ActionsPage(login1.driver)
    addnewcontact9.click_add_new_contact9_icon()


def test_Add_New_Contact9_Details(login1):
    contact9_details = AddNewContact9ActionsPage(login1.driver)
    contact9_details.fill_contact9_firstname("Dan")
    contact9_details.fill_contact9_lastname("Dave")
    contact9_details.fill_contact9_birthdate("1999-01-01")
    contact9_details.fill_contact9_email("peace9@gmail.com")
    contact9_details.fill_contact9_phone("8022805629")
    contact9_details.fill_contact9_street1("House 9, London Street")
    contact9_details.fill_contact9_street2("House 9, Scotland Street")
    contact9_details.fill_contact9_city("Lekki")
    contact9_details.fill_contact9_state("Lagos")
    contact9_details.fill_contact9_postalcode("01234")
    contact9_details.fill_contact9_country("Nigeria")
    contact9_details.fill_contact9_submit()


def test_click_add_contact10_icon(login1):
    addnewcontact10 = ClickAddNewContact10ActionsPage(login1.driver)
    addnewcontact10.click_add_new_contact10_icon()


def test_Add_New_Contact10_Details(login1):
    contact10_details = AddNewContact10ActionsPage(login1.driver)
    contact10_details.fill_contact10_firstname("Nat")
    contact10_details.fill_contact10_lastname("Nathan")
    contact10_details.fill_contact10_birthdate("2023-01-01")
    contact10_details.fill_contact10_email("peace10@gmail.com")
    contact10_details.fill_contact10_phone("8022805630")
    contact10_details.fill_contact10_street1("House 10, London Street")
    contact10_details.fill_contact10_street2("House 10, Scotland Street")
    contact10_details.fill_contact10_city("Lekki")
    contact10_details.fill_contact10_state("Lagos")
    contact10_details.fill_contact10_postalcode("01234")
    contact10_details.fill_contact10_country("Nigeria")
    contact10_details.fill_contact10_submit()


def test_click_logout_button(login1):
    clicklogout = ClickLogoutButtonActionPage(login1.driver)
    clicklogout.click_logout_button()
