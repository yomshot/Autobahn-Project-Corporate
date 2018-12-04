from Utility.fileObjects import MyLocator

class AdhocFundTransfer():

    def __init__(self):

        # instance object for MyLocator class
        exe = MyLocator()

        ft = exe.fundTransferForm()

        self.sourceAccountLoc = ft['sourceAccount']['locator']
        self.sourceAccountBy = ft['sourceAccount']['by']

        self.receiverAccountLoc = ft['receiverAccount']['locator']
        self.receiverAccountBy = ft['receiverAccount']['by']

        self.amountLoc = ft['amount']['locator']
        self.amountBy = ft['amount']['by']

        self.remarksLoc = ft['remarks']['locator']
        self.remarksBy = ft['remarks']['by']

        self.nextButtonLoc = ft['submitToConfirmation']['locator']
        self.nextButtonBy = ft['submitToConfirmation']['by']

        self.submitButtonLoc = ft['submitToSummary']['locator']
        self.submitButtonBy = ft['submitToSummary']['by']

