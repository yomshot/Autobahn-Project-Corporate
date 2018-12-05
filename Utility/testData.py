from Utility.fileObjects import MyLocator

class AdhocFundTransferData():

    def __init__(self):

        # instance object for MyLocator class
        exe = MyLocator()
        dt = exe.fundTransferData()

        self.sourceAccount = dt['sourceAccounts']
        self.sourceAccountLen = len(self.sourceAccount)