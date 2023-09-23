from selenium.webdriver.common.by import By
from base_page import BasePage

class HomePage():
    def __init__(self, driver, xtra):
        self.driver = driver
        self.xtra = xtra
        self.user_name = BasePage(self.driver, self.USER_NAME, xtra=xtra)
        self.password = BasePage(self.driver, self.PASSWORD, xtra=xtra)
        self.login_button = BasePage(self.driver, self.LOGIN_BUTTON, xtra=xtra)

    USER_NAME = (By.ID, "user-name", "Username input")
    PASSWORD = (By.ID, "password", "Password input")
    LOGIN_BUTTON = (By.ID, "login-button", "Login button")