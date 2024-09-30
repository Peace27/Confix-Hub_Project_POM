import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from ActionPage.ActionsPage import InvalidLoginActionPage


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
    login_page = InvalidLoginActionPage(driver)  # call the login class
    login_page.open_url("https://thinking-tester-contact-list.herokuapp.com/")  # call the url
    return login_page


def test_invalid_Login_Credentials(login):
    login.enter_email("peace@gmail.com")
    login.enter_password("Admin123")
    login.click_submit()
