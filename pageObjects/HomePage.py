from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pageObjects.LoginPage import LoginPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    page = (By.CLASS_NAME, "active")
    kadin = (By.XPATH, "//*[@id='navigation-wrapper']/nav/ul/li[1]/a")
    erkek = (By.XPATH, "//*[@id='navigation-wrapper']/nav/ul/li[2]/a")
    cocuk = (By.XPATH, "//*[@id='navigation-wrapper']/nav/ul/li[3]/a")
    ev = (By.XPATH, "//*[@id='navigation-wrapper']/nav/ul/li[4]/a")
    market = (By.XPATH, "//*[@id='navigation-wrapper']/nav/ul/li[5]/a")
    kozmetik = (By.XPATH, "//*[@id='navigation-wrapper']/nav/ul/li[6]/a")
    ayakkabi = (By.XPATH, "//*[@id='navigation-wrapper']/nav/ul/li[7]/a")
    saat = (By.XPATH, "//*[@id='navigation-wrapper']/nav/ul/li[8]/a")
    elektronik = (By.XPATH, "//*[@id='navigation-wrapper']/nav/ul/li[9]/a")
    login = (By.CLASS_NAME, "login-container")
    logedIn = (By.ID, "logged-in-container")

    def isLoggedIn(self):
        return self.driver.find_element(*HomePage.logedIn)

    def loginPageClick(self):
        self.driver.find_element(*HomePage.login).click()
        loginPage = LoginPage(self.driver)
        return loginPage

    def pageName(self):
        return self.driver.find_element(*HomePage.page)

    def kadinSection(self):
        return self.driver.find_element(*HomePage.kadin)

    def erkekSection(self):
        return self.driver.find_element(*HomePage.erkek)

    def cocukSection(self):
        return self.driver.find_element(*HomePage.cocuk)

    def evSection(self):
        return self.driver.find_element(*HomePage.ev)

    def marketSection(self):
        return self.driver.find_element(*HomePage.market)

    def kozmetikSection(self):
        return self.driver.find_element(*HomePage.kozmetik)

    def ayakkabiSection(self):
        return self.driver.find_element(*HomePage.ayakkabi)

    def saatSection(self):
        return self.driver.find_element(*HomePage.saat)

    def elektronikSection(self):
        return self.driver.find_element(*HomePage.elektronik)
