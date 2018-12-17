from Utility.fileObjects import MyLocator

class AdhocFundTransfer():

    def __init__(self):

        # instance object for MyLocator class
        exe = MyLocator()
        ft = exe.fundTransferForm()

        ftField = ft['reuseField']
        ftButton = ft['reuseButton']
        ftChannel = ft['reuseButton']['channels']

        self.formOverlayLoc = ft['reuseOverlay']['locator']
        self.formOverlayBy = ft['reuseOverlay']['by']

        self.btnNewTransactionLoc = ftButton['newTransaction']['locator']
        self.btnNewTransactionBy = ftButton['newTransaction']['by']

        self.chUbpLoc = ftChannel['chUbp']['locator']
        self.chPesonetLoc = ftChannel['chPesonet']['locator']
        self.chSwiftLoc = ftChannel['chSwift']['locator']
        self.chPddtsLoc = ftChannel['chPddts']['locator']

        self.chUbpBy = ftChannel['chUbp']['by']
        self.chPesonetBy = ftChannel['chPesonet']['by']
        self.chSwiftBy = ftChannel['chSwift']['by']
        self.chPddtsBy = ftChannel['chPddts']['by']

        self.sourceAccountLoc = ftField['sourceAccount']['locator']
        self.sourceAccountBy = ftField['sourceAccount']['by']

        self.nextButtonLoc = ftButton['submitToConfirmation']['locator']
        self.nextButtonBy = ftButton['submitToConfirmation']['by']

        self.receiverAccountLoc = ftField['receiverAccount']['locator']
        self.receiverAccountBy = ftField['receiverAccount']['by']

        self.submitLoc = ftButton['submitToSummary']['locator']
        self.submitBy = ftButton['submitToSummary']['by']

        self.selSourceAccountLoc = ftField['selectSource']['locator']
        self.selSourceAccountBy = ftField['selectSource']['by']

        self.makeAnotherTransferLoc = ftButton['makeAnotherTransfer']['locator']
        self.makeAnotherTransferBy = ftButton['makeAnotherTransfer']['by']

        self.amountLoc = ftField['amount']['locator']
        self.amountBy = ftField['amount']['by']

        self.remarksLoc = ftField['remarks']['locator']
        self.remarksBy = ftField['remarks']['by']






