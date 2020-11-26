from selenium.webdriver.common.by import By
from pageObjects.BoutiquePage import BoutiquePage

import random

class ProductPage:

    def __init__(self, driver):
        self.driver = driver

    product = (By.CLASS_NAME, "p-card-wrppr")
    product1 = (By.CLASS_NAME, "prdct-cntnr-wrppr")
    product2 = (By.CLASS_NAME, "boutique-product")
    price = (By.CLASS_NAME, "prc-org")
    basket = (By.CLASS_NAME, "add-to-bs")
    succeed = (By.CLASS_NAME, "navigation-icon-basket")
    confirm = (By.CLASS_NAME, "Basket_CheckoutButton")

    def goToBoutique(self):
        page = BoutiquePage(self.driver)
        page.randSection().click()
        page.boutiqueClick().click()

    def goToProduct(self):
        try:
            prodCount = len(self.driver.find_elements(*ProductPage.product))
            prod = self.driver.find_elements(*ProductPage.product)
        except:
            pass
        try:
            prodCount = len(self.driver.find_elements(*ProductPage.product1))
            prod = self.driver.find_elements(*ProductPage.product1)
        except:
            pass
        try:
            prodCount = len(self.driver.find_elements(*ProductPage.product2))
            prod = self.driver.find_elements(*ProductPage.product2)
        except:
            pass

        rand = random.randint(1,prodCount)
        return prod[rand]

    def checkPage(self):
        return self.driver.find_element(*ProductPage.price)

    def addToBasket(self):
        return self.driver.find_element(*ProductPage.basket)

    def checkItemAdded(self):
        return self.driver.find_element(*ProductPage.succeed)

    def confirmItem(self):
        return self.driver.find_element(*ProductPage.confirm)

