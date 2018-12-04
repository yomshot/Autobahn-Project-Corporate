import json

class MyLocator():

    def url(self):
        try:
            path = "C:\\Users\cheqws115-user\\PycharmProjects\\Autobahn-Project\\PageObject\\Locators\\url.json"

            with open(path, encoding='utf-8') as s:
                url = json.loads(s.read())
            return url
        except:
            return print('JSON File not existing')

    def login(self):
        try:
            path = "C:\\Users\\cheqws115-user\\PycharmProjects\\Autobahn-Project\\PageObject\\Locators\\loginPage.json"

            with open(path, encoding='utf-8') as s:
                login = json.loads(s.read())
            return login
        except:
            return print('JSON File not existing')

    def loginCredential(self):
        try:
            path = "C:\\Users\\cheqws115-user\\PycharmProjects\\Autobahn-Project\\PageObject\\Locators\\" \
                   "loginCredential.json"

            with open(path, encoding='utf-8') as s:
                credential = json.loads(s.read())
            return credential
        except:
            return print('JSON File not existing')

    def otp(self):
        try:
            path = "C:\\Users\\cheqws115-user\\PycharmProjects\\Autobahn-Project\\PageObject\\Locators\\otp.json"

            with open(path, encoding='utf-8') as s:
                otp = json.loads(s.read())
            return otp
        except:
            return print('JSON File not existing')