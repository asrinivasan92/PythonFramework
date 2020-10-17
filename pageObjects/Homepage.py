from selenium.webdriver.common.by import By

from pageObjects.Checkout import Checkoutpage


class Homepage:

    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    name = (By.CSS_SELECTOR, "[name='name']")
    email = (By.NAME, "email")
    check = (By.ID, "exampleCheck1")
    gender = (By.ID, "exampleFormControlSelect1")
    submit = (By.XPATH, "//input[@value='Submit']")
    successMessage = (By.CSS_SELECTOR, "[class*='alert-success']")

    def shopitems(self):
        self.driver.find_element(*Homepage.shop).click()
        checkoutpage = Checkoutpage(self.driver)
        return checkoutpage
        #self.driver.find_element_by_css_selector("a[href*='shop']").click()

    def getName(self):
        return self.driver.find_element(*Homepage.name)

    def getEmail(self):
        return self.driver.find_element(*Homepage.email)

    def getCheckBox(self):
        return self.driver.find_element(*Homepage.check)

    def getGender(self):
        return self.driver.find_element(*Homepage.gender)

    def submitForm(self):
        return self.driver.find_element(*Homepage.submit)

    def getSuccessMessage(self):
        return self.driver.find_element(*Homepage.successMessage)