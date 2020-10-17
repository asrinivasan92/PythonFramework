import pytest
from Testdata.Homepagedata import HomePageData
from pageObjects.Homepage import Homepage
from utilities.base import BaseClass


class Homepagesubmit(BaseClass):

    def test_formSubmission(self,getData):
        log = self.getLogger()
        homepage = Homepage(self.driver)
        log.info("Fill the form")
        homepage.getName().send_keys(getData["firstname"])
        homepage.getEmail().send_keys(getData["lastname"])
        homepage.getCheckBox().click()
        self.selectOptionByText(homepage.getGender(),getData["gender"])
        homepage.submitForm().click()

        alertText = homepage.getSuccessMessage().text
        log.info("Assert Verified")
        assert ("Success" in alertText)
        self.driver.refresh()

    @pytest.fixture(params = HomePageData.test_HomePage_data)
    def getData(self, request):
        return request.param