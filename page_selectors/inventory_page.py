from selenium.webdriver.common.by import By
from base_page import BasePage

class InventoryPage():
    def __init__(self, driver, xtra):
        self.driver = driver
        self.xtra = xtra
        self.burger_menu = BasePage(self.driver, self.BURGER_MENU, xtra=xtra)

    BURGER_MENU = (By.ID, "react-burger-menu-btn", "Hamburger Menu")