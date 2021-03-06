from utilities.BaseClass import BaseClass
from pageObjects.ProductPage import ProductPage

from selenium.webdriver import ActionChains
from time import sleep

class TestProduct(BaseClass):

    def test_go_to_product(self):
        log = self.getLogger()
        log.info("Going for boutique page")
        page = ProductPage(self.driver)
        actions = ActionChains(self.driver)
        page.goToBoutique()
        log.info("Going for product page")
        element = page.goToProduct()
        actions.move_to_element(element).click().perform()
        sleep(1)

        assert page.checkPage().is_displayed , "You are not in the product page"

    def test_add_to_basket(self):
        page = ProductPage(self.driver)
        log = self.getLogger()
        check = page.addToBasket().text
        if check == "Tükendi":
            assert 1 == 2 , "Item has sold out, you can add this item to your basket"
        else:
            log.info("Adding product to basket")
            page.addToBasket().click()

        page.checkItemAdded().click()

        assert page.confirmItem().is_displayed , "You couldn't add the item to your basket"
        sleep(2)
