from Utility.fileObjects import MyLocator

class Login():

    def __init__(self):

        # instance object for MyLocator class
        exe = MyLocator()

        # these three lines of code are accessing the json file from Utility/fileObjects.py
        login = exe.login()
        credential = exe.loginCredential()
        otp = exe.otp()

        # get username field's location by xpath
        self.usernameLoc = login['usernameField']['locator']
        self.usernameBy = login['usernameField']['by']

        # get password field's location by xpath
        self.passwordLoc = login['passwordField']['locator']
        self.passwordBy = login['passwordField']['by']

        # get username and password credentials
        self.username = credential['credential']['validUsername'][0]
        self.password = credential['credential']['validPassword'][0]

        # get login button's location by xpath
        self.loginButtonLoc = login['submitButton']['locator']
        self.loginButtonBy = login['submitButton']['by']

        # get otp field's location by xpath
        self.otpLoc = otp['otpField']['locator']
        self.otpBy = otp['otpField']['by']
        self.otpCode = otp['otpField']['code']

        # get otp button's location by xpath
        self.otpButtonLoc = otp['otpButton']['locator']
        self.otpButtonBy = otp['otpButton']['by']