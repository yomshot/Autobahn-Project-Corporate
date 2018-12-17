from Utility.fileObjects import MyLocator
import datetime

class AdhocFundTransferData():

    def __init__(self):

        # instance object for MyLocator class
        exe = MyLocator()
        dt = exe.fundTransferData()
        ch = dt['channels']

        self.phpSourceAccount = dt['phpSourceAccounts']
        self.phpSourceAccountLen = len(self.phpSourceAccount)

        self.phpTargetAccount = dt['phpTargetAccounts']
        self.phpTargetAccountLen = len(self.phpTargetAccount)

        self.usdTargetAccount = dt['usdTargetAccounts']
        self.usdTargetAccountLen = len(self.usdTargetAccount)

        self.amount = ch['ftUbp']['amount']
        self.remarks = ch['ftUbp']['remarks']