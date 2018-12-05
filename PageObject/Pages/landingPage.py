from Utility.fileObjects import MyLocator

class LandingComponents():

    def __init__(self):

        exe = MyLocator()

        lc = exe.landingComponent()


        # Organization Icon
        self.orgIconLoc = lc['topBar']['orgIcon']['locator']
        self.orgIconBy = lc['topBar']['orgIcon']['by']

        # Select the organization in the list
        self.orgSelectionLoc = lc['topBar']['organization']['locator']
        self.orgSelectionBy = lc['topBar']['organization']['by']

        # Logo for home button
        self.logoHomeButtonLoc = None
        self.logoHomeButtonBy = None

        # Accounts BTR
        self.accountButtonLoc = None
        self.accountButtonBy = None

        # Fund Transfer
        self.ftButtonLoc = lc['leftSideBar']['fundTransfer']['locator']
        self.ftButtonBy = lc['leftSideBar']['fundTransfer']['by']






