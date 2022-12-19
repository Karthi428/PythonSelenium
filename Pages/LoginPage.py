from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.BasePage import Basetests


class LoginPage(Basetests):
    Username = (By.XPATH, "//input[@placeholder='Username']")
    Password = (By.XPATH, "//input[@placeholder='Password']")
    LoginButton = (By.XPATH, "//button[normalize-space()='Login']")

    def __init__(self, driver):
        super().__init__(driver)

    def get_title(self, title):
        return self.get_title(title)

    def enter_values(self, email, passw):
        self.do_send_keys(self.Username, email)
        self.do_send_keys(self.Password, passw)
        self.do_click(self.LoginButton)
