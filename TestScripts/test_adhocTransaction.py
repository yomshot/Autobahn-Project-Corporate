import pytest
from Utility.actionKeys import MakeAction
from PageObject.Pages.loginPage import Login
from PageObject.Pages.adhocFundTransfer import AdhocFundTransfer
from PageObject.Pages.landingPage import LandingComponents
from Utility.testData import AdhocFundTransferData

@pytest.mark.usefixtures("setup")
class TestLoginForm:
    wait = 4

    def test_login(self):
        driver = self.driver
        run = MakeAction(driver)
        lc = LandingComponents()
        ft = AdhocFundTransfer()
        my = Login()

        run.find_elements(my.usernameBy, my.usernameLoc)  # find username field
        run.find_element_and_input(my.usernameBy, my.usernameLoc, self.wait, my.username)  # enter valid username

        run.find_elements(my.passwordBy, my.passwordLoc)  # find password field
        run.find_element_and_input(my.passwordBy, my.passwordLoc, self.wait, my.password)  # enter valid password

        run.click_element(my.loginButtonBy, my.loginButtonLoc)  # click button to submit

        run.find_elements(my.otpBy, my.otpLoc)  # find otp field
        run.find_element_and_input(my.otpBy, my.otpLoc, self.wait, my.otpCode)  # enter otp by default

        run.click_element(my.otpButtonBy, my.otpButtonLoc)  # click otp submit button

        run.click_element(lc.orgIconBy, lc.orgIconLoc) # click the circle for org selection

        run.find_item_in_elements_and_get(lc.orgSelectionBy, lc.orgSelectionLoc, self.wait, "Test Org 11-21 16:57")

        run.click_element(lc.ftButtonBy, lc.ftButtonLoc) # going to fund transfer

        run.click_element(ft.btnNewTransactionBy, ft.btnNewTransactionLoc) # new transaction

   # @pytest.mark.skip(reason="no way of currently testing this")
    def test_adhoc_ubp(self):
        driver = self.driver
        run = MakeAction(driver)
        ft = AdhocFundTransfer()
        dt = AdhocFundTransferData()

        num_of_accounts = dt.sourceAccountLen
        select_account = dt.sourceAccount

        run.click_element(ft.chUbpBy, ft.chUbpLoc)
        run.click_element(ft.sourceAccountBy, ft.sourceAccountLoc)

        for i in range(num_of_accounts):
            run.find_item_in_elements_and_get(ft.selSourceAccountBy, ft.selSourceAccountLoc, self.wait, select_account[i])
