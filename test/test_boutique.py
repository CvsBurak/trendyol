from utilities.BaseClass import BaseClass
from pageObjects.BoutiquePage import BoutiquePage

from time import sleep


class TestBouqtique(BaseClass):

    def test_boutique_page(self):
        page = BoutiquePage(self.driver)
        log = self.getLogger()
        log.info("Selecting boutique randomly")
        page.randSection().click()
        sleep(1)
        page.boutiqueClick().click()
        sleep(1)
        assert page.checkPage().is_displayed , "You could't reach random boutique"
