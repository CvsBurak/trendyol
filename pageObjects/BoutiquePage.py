from selenium.webdriver.common.by import By

from pageObjects.HomePage import HomePage
import random


class BoutiquePage:

    def __init__(self, driver):
        self.driver = driver


    boutique = (By.CLASS_NAME, "component-item")
    fav = (By.CLASS_NAME, "fvrt-btn")

    def randSection(self):
        page = HomePage(self.driver)
        sections = [page.saatSection, page.marketSection, page.kozmetikSection, page.kadinSection,
                        page.evSection, page.erkekSection, page.elektronikSection, page.cocukSection,
                         page.ayakkabiSection]
        return random.choice(sections)()

    def boutiqueClick(self):
        butiques = self.driver.find_elements(*BoutiquePage.boutique)
        rand = random.randint(1, len(butiques))
        return butiques[rand]

    def checkPage(self):
        return self.driver.find_element(*BoutiquePage.fav)