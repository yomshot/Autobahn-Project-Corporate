import json

class MyLocator():

    def url(self): # this method will access url.json
        try:
            path = "C:\\Users\cheqws115-user\\PycharmProjects\\Autobahn-Project\\PageObject\\Locators\\url.json"

            with open(path, encoding='utf-8') as s:
                url = json.loads(s.read())
            return url
        except:
            return print('JSON File not existing')

    def landingComponent(self):
        try:
            path = "C:\\Users\\cheqws115-user\\PycharmProjects\\Autobahn-Project\\PageObject\\Locators\\" \
                   "landingComponent.json"

            with open(path, encoding='utf-8') as s:
                lc = json.loads(s.read())
            return lc
        except:
            return print('JSON File not existing')

    def login(self): # this method will access loginPage.json
        try:
            path = "C:\\Users\\cheqws115-user\\PycharmProjects\\Autobahn-Project\\PageObject\\Locators\\loginPage.json"

            with open(path, encoding='utf-8') as s:
                login = json.loads(s.read())
            return login
        except:
            return print('JSON File not existing')

    def loginCredential(self): # this method will access loginCredential.json
        try:
            path = "C:\\Users\\cheqws115-user\\PycharmProjects\\Autobahn-Project\\PageObject\\Locators\\" \
                   "loginCredential.json"

            with open(path, encoding='utf-8') as s:
                credential = json.loads(s.read())
            return credential
        except:
            return print('JSON File not existing')

    def otp(self): # this method will access otp.json
        try:
            path = "C:\\Users\\cheqws115-user\\PycharmProjects\\Autobahn-Project\\PageObject\\Locators\\otp.json"

            with open(path, encoding='utf-8') as s:
                otp = json.loads(s.read())
            return otp
        except:
            return print('JSON File not existing')

    def fundTransferData(self):
        try:
            path = "C:\\Users\\cheqws115-user\\PycharmProjects\\Autobahn-Project\\PageObject\\Locators\\" \
                   "fundTransferData.json"

            with open(path, encoding='utf-8') as s:
                ft = json.loads(s.read())
            return ft
        except:
            return print('JSON File not existing')

    def fundTransferForm(self):
        try:
            path = "C:\\Users\\cheqws115-user\\PycharmProjects\\Autobahn-Project\\PageObject\\Locators\\" \
                   "fundTransferForm.json"

            with open(path, encoding='utf-8') as s:
                ft = json.loads(s.read())
            return ft
        except:
            return print('JSON File not existing')




