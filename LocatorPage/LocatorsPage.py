from selenium.webdriver.common.by import By


class InvalidLoginLocatorsPage:
    ENTER_INVALID_EMAIL = (By.ID, "email")
    ENTER_INVALID_PASSWORD = (By.ID, "password")
    CLICK_SUBMIT = (By.ID, "submit")


class ValidLoginLocatorsPage:
    ENTER_VALID_EMAIL = (By.ID, "email")
    ENTER_VALID_PASSWORD = (By.ID, "password")
    CLICK_SUBMIT1 = (By.ID, "submit")


# Ensure  user can add 10 Contact(Contact 1)
class AddNewContact1LocatorsPage:
    CLICK_ADD_NEW_CONTACT1_ICON = (By.ID, "add-contact")


class FillContact1LocatorsPage:
    FILL_CONTACT1_FIRST_NAME = (By.ID, "firstName")
    FILL_CONTACT1_LAST_NAME = (By.ID, "lastName")
    FILL_CONTACT1_BIRTHDATE = (By.ID, "birthdate")
    FILL_CONTACT1_EMAIL = (By.ID, "email")
    FILL_CONTACT1_PHONE = (By.ID, "phone")
    FILL_CONTACT1_STREET1 = (By.ID, "street1")
    FILL_CONTACT1_STREET2 = (By.ID, "street2")
    FILL_CONTACT1_CITY = (By.ID, "city")
    FILL_CONTACT1_STATE = (By.ID, "stateProvince")
    FILL_CONTACT1_POSTALCODE = (By.ID, "postalCode")
    FILL_CONTACT1_COUNTRY = (By.ID, "country")
    FILL_CONTACT1_SUBMIT = (By.ID, "submit")
