import pytest
from Utility.actionKeys import MakeAction
from PageObject.Pages.loginPage import Login

@pytest.mark.usefixtures("setup")
class TestLoginForm:

    @pytest.mark.skip(reason="no way of currently testing this")
    def test_valid_login(self):
        driver = self.driver
        run = MakeAction(driver)
        my = Login()
        wait = 4

        run.find_element_and_input(my.usernameBy, my.usernameLoc, wait, my.username) # enter valid username

        run.find_element_and_input(my.passwordBy, my.passwordLoc, wait, my.password) # enter valid password

        run.click_element(my.loginButtonBy, my.loginButtonLoc) # click button to submit

        run.find_element_and_input(my.otpBy, my.otpLoc, wait, my.otpCode) # enter otp by default

        run.click_element(my.otpButtonBy, my.otpButtonLoc) # click otp submit button

