from utilities.BaseClass import BaseClass
from pageObjects.HomePage import HomePage
from TestData.LoginData import LoginData

from time import sleep


class TestLogin(BaseClass):

    def test_login_page(self):

        home = HomePage(self.driver)
        login = home.loginPageClick()
        sleep(2)
        login.getMail().send_keys(getData["mail"])
        login.getPass().send_keys(getData["password"])
        login.loginButton().click()

        sleep(2)
        assert home.isLoggedIn().is_displayed , "Login Failed"
    
    @pytest.fixture(params=LoginData.login_data)
    def getData(self, request):
        return request.param
