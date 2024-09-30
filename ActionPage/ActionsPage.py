import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from LocatorPage.LocatorsPage import InvalidLoginLocatorsPage


class InvalidLoginActionPage:
    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):
        self.driver.get(url)

    def enter_email(self, email):
        enter_email = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(InvalidLoginLocatorsPage.ENTER_EMAIL))
        enter_email.send_keys(email)
        time.sleep(2)

    def enter_password(self, password):
        enter_password = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(InvalidLoginLocatorsPage.ENTER_PASSWORD))
        enter_password.send_keys(password)
        time.sleep(2)

    def click_submit(self):
        click_submit = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(InvalidLoginLocatorsPage.CLICK_SUBMIT))
        click_submit.click()
        time.sleep(2)
