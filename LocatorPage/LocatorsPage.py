from selenium.webdriver.common.by import By


class InvalidLoginLocatorsPage:
    ENTER_EMAIL = (By.ID, "email")
    ENTER_PASSWORD = (By.ID, "password")
    CLICK_SUBMIT = (By.ID, "submit")
