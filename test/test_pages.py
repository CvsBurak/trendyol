from time import sleep
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
from selenium.webdriver.firefox.options import Options
from utilities.BaseClass import BaseClass
from pageObjects.HomePage import HomePage


class TestOne(BaseClass):

    def test_kadin(self):
        home = HomePage(self.driver)
        log = self.getLogger()
        log.info("Now going to KADIN's page")
        home.kadinSection().click()
        page = home.pageName().text
        log.info("Now you are in " + page)
        assert page in "KADIN", "You are in the wrong page"
        sleep(1)

    def test_erkek(self):
        home = HomePage(self.driver)
        log = self.getLogger()
        log.info("Now going to ERKEK's page")
        home.erkekSection().click()
        page = home.pageName().text
        log.info("Now you are in " + page)
        assert page in "ERKEK", "You are in the wrong page"
        sleep(1)

    def test_cocuk(self):
        home = HomePage(self.driver)
        log = self.getLogger()
        log.info("Now going to COCUK's page")
        home.cocukSection().click()
        page = home.pageName().text
        log.info("Now you are in " + page)
        assert page in "ÇOCUK", "You are in the wrong page"
        sleep(1)

    def test_ev(self):
        home = HomePage(self.driver)
        log = self.getLogger()
        log.info("Now going to EV & YASAM's page")
        home.evSection().click()
        page = home.pageName().text
        log.info("Now you are in " + page)
        assert page in "EV & YAŞAM", "You are in the wrong page"
        sleep(1)

    def test_market(self):
        home = HomePage(self.driver)
        log = self.getLogger()
        log.info("Now going to SUPERMARKET's page")
        home.marketSection().click()
        page = home.pageName().text
        log.info("Now you are in " + page)
        assert page in "SÜPERMARKET", "You are in the wrong page"
        sleep(1)

    def test_kozmetik(self):
        home = HomePage(self.driver)
        log = self.getLogger()
        log.info("Now going to KOZMETIK's page")
        home.kozmetikSection().click()
        page = home.pageName().text
        log.info("Now you are in " + page)
        assert page in "KOZMETİK", "You are in the wrong page"
        sleep(1)

    def test_ayakkabi(self):
        home = HomePage(self.driver)
        log = self.getLogger()
        log.info("Now going to AYAKKABI & CANTA's page")
        home.ayakkabiSection().click()
        page = home.pageName().text
        log.info("Now you are in " + page)
        assert page in "AYAKKABI & ÇANTA", "You are in the wrong page"
        sleep(1)

    def test_saat(self):
        home = HomePage(self.driver)
        log = self.getLogger()
        log.info("Now going to SAAT & AKSESUAR's page")
        home.saatSection().click()
        page = home.pageName().text
        log.info("Now you are in " + page)
        assert page in "SAAT & AKSESUAR", "You are in the wrong page"
        sleep(1)

    def test_elektronik(self):
        home = HomePage(self.driver)
        log = self.getLogger()
        log.info("Now going to ELEKTRONIK's page")
        home.elektronikSection().click()
        page = home.pageName().text
        log.info("Now you are in " + page)
        assert page in "ELEKTRONİK", "You are in the wrong page"
        sleep(1)

