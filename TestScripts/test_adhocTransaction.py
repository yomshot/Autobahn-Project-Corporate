import pytest
from Utility.actionKeys import MakeAction
from PageObject.Pages.loginPage import Login
from PageObject.Pages.adhocFundTransfer import AdhocFundTransfer
from PageObject.Pages.landingPage import LandingComponents
from PageObject.Pages.otp import MyOTP
from Utility.testData import AdhocFundTransferData
import datetime
import time


@pytest.mark.usefixtures("setup")
class TestLoginForm:
    wait = 7
    organization = "DEMO ACCOUNT 11-23 16:29"
    timeAndDate = datetime.datetime.now().strftime("%m-%d-%y %H:%M")
    dateAndTimeToday = str(timeAndDate)

    def test_login(self):
        driver = self.driver
        run = MakeAction(driver)
        lc = LandingComponents()
        ft = AdhocFundTransfer()
        my = Login()

        run.find_element_and_input(my.usernameBy, my.usernameLoc, self.wait, my.username)  # enter valid username
        run.find_element_and_input(my.passwordBy, my.passwordLoc, self.wait, my.password)  # enter valid password
        run.click_element(my.loginButtonBy, my.loginButtonLoc)  # click button to submit

        run.find_element_and_input(my.otpBy, my.otpLoc, self.wait, my.otpCode)  # enter otp by default

        run.click_element(my.otpButtonBy, my.otpButtonLoc)  # click otp submit button

        run.click_element(lc.orgIconBy, lc.orgIconLoc) # click the circle for org selection

        run.find_item_in_elements_and_click(lc.orgSelectionBy, lc.orgSelectionLoc, self.wait, self.organization)
        time.sleep(2)
        run.click_element(lc.ftButtonBy, lc.ftButtonLoc) # going to fund transfer

        run.click_element(ft.btnNewTransactionBy, ft.btnNewTransactionLoc) # new transaction

   # @pytest.mark.skip(reason="no way of currently testing this")
    def test_adhoc_ubp(self):
        driver = self.driver
        run = MakeAction(driver)
        ft = AdhocFundTransfer()
        dt = AdhocFundTransferData()
        otp = MyOTP()

        num_of_accounts = dt.phpSourceAccountLen
        select_account = dt.phpSourceAccount

        num_of_target = dt.phpTargetAccountLen
        select_target = dt.phpTargetAccount

        run.click_element(ft.chUbpBy, ft.chUbpLoc)
        run.click_element(ft.sourceAccountBy, ft.sourceAccountLoc)

        for i in range(num_of_accounts):
            source = run.find_item_in_elements_and_click(ft.selSourceAccountBy, ft.selSourceAccountLoc, self.wait, select_account[i])
            if source:
                break

        run.find_elements(ft.receiverAccountBy, ft.receiverAccountLoc)

        for i in range(num_of_target):
            target = run.find_element_and_input(ft.receiverAccountBy, ft.receiverAccountLoc, self.wait, select_target[i])
            if target:
                break

        run.find_element_and_input(ft.amountBy, ft.amountLoc, self.wait, dt.amount)

        run.find_element_and_input(ft.remarksBy, ft.remarksLoc, self.wait, dt.remarks)

        run.click_element(ft.nextButtonBy, ft.nextButtonLoc)

        time.sleep(3)
        overlay = run.wait_until_element_visible(ft.formOverlayBy, ft.formOverlayLoc)

        while overlay:
            print("displaying")
            pass
        else:
            run.click_element(ft.submitBy, ft.submitLoc)

        run.find_element_and_input(otp.otpBy, otp.otpLoc, self.wait, otp.otpCode)  # enter otp by default

        run.click_element(otp.otpButtonBy, otp.otpButtonLoc)  # click otp submit button
        time.sleep(2)
        run.click_element(ft.makeAnotherTransferBy, ft.makeAnotherTransferLoc)
