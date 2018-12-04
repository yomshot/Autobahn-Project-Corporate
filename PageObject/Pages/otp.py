from Utility.fileObjects import MyLocator

class AdhocFundTransfer():

    def __init__(self):

        # instance object for MyLocator class
        exe = MyLocator()

        otp = exe.otp()

        # get otp field's location by xpath
        self.otpLoc = otp['otpField']['locator']
        self.otpBy = otp['otpField']['by']
        self.otpCode = otp['otpField']['code']

        # get otp button's location by xpath
        self.otpButtonLoc = otp['otpButton']['locator']
        self.otpButtonBy = otp['otpButton']['by']