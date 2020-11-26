from utilities.BaseClass import BaseClass
from pageObjects.HomePage import HomePage
from TestData.LoginData import LoginData

from time import sleep


class TestLogin(BaseClass):

    def test_login_page(self, getData):
        log = self.getLogger()
        home = HomePage(self.driver)
        log.info("Going to login page")
        login = home.loginPageClick()
        sleep(2)
        log.info("Loging in as " + getData["mail"])
        login.getMail().send_keys(getData["mail"])
        login.getPass().send_keys(getData["password"])
        login.loginButton().click()
        sleep(2)
        assert home.isLoggedIn().is_displayed, "Login Failed"
        self.driver.refresh()


    @pytest.fixture(params=LoginData.login_data)
    def getData(self, request):
        return request.param
