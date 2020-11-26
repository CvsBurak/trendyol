from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    email = (By.XPATH, "//*[@id='login-email']")
    psswd = (By.XPATH, "//*[@id='login-password-input']")
    logButton = (By.XPATH,  "//*[@id='login-register']/div[3]/div[1]/form/button")



    def getMail(self):
        return self.driver.find_element(*LoginPage.email)

    def getPass(self):
        return self.driver.find_element(*LoginPage.psswd)

    def loginButton(self):
        return self.driver.find_element(*LoginPage.logButton)



