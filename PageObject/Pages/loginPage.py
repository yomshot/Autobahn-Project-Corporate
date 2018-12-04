from Utility.fileObjects import MyLocator

class Login():

    def __init__(self):

        exe = MyLocator()

        login = exe.login()
        credential = exe.loginCredential()
        otp = exe.otp()

        self.usernameLoc = login['usernameField']['locator']
        self.usernameBy = login['usernameField']['by']

        self.passwordLoc = login['passwordField']['locator']
        self.passwordBy = login['passwordField']['by']

        self.username = credential['credential']['validUsername'][0]
        self.password = credential['credential']['validPassword'][0]

        self.loginButtonLoc = login['submitButton']['locator']
        self.loginButtonBy = login['submitButton']['by']

        self.otpLoc = otp['otpField']['locator']
        self.otpBy = otp['otpField']['by']
        self.otpCode = otp['otpField']['code']

        self.otpButtonLoc = otp['otpButton']['locator']
        self.otpButtonBy = otp['otpButton']['by']