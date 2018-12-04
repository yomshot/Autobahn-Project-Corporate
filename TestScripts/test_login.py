import pytest
from Utility.actionKeys import MakeAction
from PageObject.Pages.loginPage import Login

@pytest.mark.usefixtures("setup")
class TestLoginForm:

    def test_valid_login(self):
        driver = self.driver
        run = MakeAction(driver)
        my = Login()
        wait = 4

        run.find_elements(my.usernameBy, my.usernameLoc)
        run.find_element_and_input(my.usernameBy, my.usernameLoc, wait, my.username)

        run.find_elements(my.passwordBy, my.passwordLoc)
        run.find_element_and_input(my.passwordBy, my.passwordLoc, wait, my.password)

        run.click_element(my.loginButtonBy, my.loginButtonLoc)

        run.find_elements(my.otpBy, my.otpLoc)
        run.find_element_and_input(my.otpBy, my.otpLoc, wait, my.otpCode)

        run.click_element(my.otpButtonBy, my.otpButtonLoc)

