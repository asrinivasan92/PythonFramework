from selenium.webdriver.common.by import By


class Confirmpage:
    def __init__(self,driver):
        self.driver = driver

    CheckoutSuccess = (By.XPATH, "/html/body/app-root/app-shop/div/div/div/table/tbody/tr[3]/td[5]/button")

    def SuccessButton(self):
        self.driver.find_element(*Confirmpage.CheckoutSuccess).click()
