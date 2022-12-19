import pytest

from Config.config import TestData
from Pages.LoginPage import LoginPage
from Tests.test_Base import BaseTest


class Test_Login(BaseTest):

    def test_title(self):
        self.loginpage = LoginPage(self.driver)
        title = self.loginpage.get_title(TestData.Login_title)
        assert title == TestData.Login_title

    def test_login(self):
        self.loginpage = LoginPage(self.driver)
        self.loginpage.enter_values(TestData.USERNAME, TestData.PASSWORD)
