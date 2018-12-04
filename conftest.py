from selenium.webdriver import Chrome
from Utility.fileObjects import MyLocator
import pytest
import time

@pytest.fixture(scope="class")
def setup(request):

    # instance object for MyLocator class
    exe = MyLocator()

    # assign url
    link = exe.url()

    # get the url from url.json
    url = link['url']['corporate'][0]
    path = 'D:\\chromedriver.exe'

    driver = Chrome(executable_path=path)
    driver.get(url)
    driver.maximize_window()
    request.cls.driver = driver

    yield driver
    time.sleep(10)
    driver.close()