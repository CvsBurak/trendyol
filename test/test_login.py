from utilities.BaseClass import BaseClass
from pageObjects.HomePage import HomePage

from time import sleep


class TestLogin(BaseClass):

    def test_login_page(self):

        home = HomePage(self.driver)
        login = home.loginPageClick()
        sleep(2)
        login.getMail().send_keys()
        login.getPass().send_keys()
        login.loginButton().click()

        sleep(2)
        assert home.isLoggedIn().is_displayed , "Login Failed"
