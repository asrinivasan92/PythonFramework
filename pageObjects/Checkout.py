from selenium.webdriver.common.by import By

from pageObjects.Confirmpage import Confirmpage


class Checkoutpage:
    def __init__(self,driver):
        self.driver = driver

    Checkout = (By.XPATH, "//*[@id='navbarResponsive']/ul/li/a")

    def CheckoutButton(self):
        self.driver.find_element(*Checkoutpage.Checkout).click()
        confirmpage = Confirmpage(self.driver)
        return confirmpage


