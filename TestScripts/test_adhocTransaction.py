import pytest
from Utility.actionKeys import MakeAction
from PageObject.Pages.loginPage import Login
from PageObject.Pages.adhocFundTransfer import AdhocFundTransfer

@pytest.mark.usefixtures("setup")
class TestLoginForm:
    wait = 4

    def test_login(self):
        driver = self.driver
        run = MakeAction(driver)

        my = Login()


        run.find_elements(my.usernameBy, my.usernameLoc)  # find username field
        run.find_element_and_input(my.usernameBy, my.usernameLoc, self.wait, my.username)  # enter valid username

        run.find_elements(my.passwordBy, my.passwordLoc)  # find password field
        run.find_element_and_input(my.passwordBy, my.passwordLoc, self.wait, my.password)  # enter valid password

        run.click_element(my.loginButtonBy, my.loginButtonLoc)  # click button to submit

        run.find_elements(my.otpBy, my.otpLoc)  # find otp field
        run.find_element_and_input(my.otpBy, my.otpLoc, self.wait, my.otpCode)  # enter otp by default

        run.click_element(my.otpButtonBy, my.otpButtonLoc)  # click otp submit button

    def test_adhoc_ubp(self):
        driver = self.driver
        run = MakeAction(driver)

        my = AdhocFundTransfer()















