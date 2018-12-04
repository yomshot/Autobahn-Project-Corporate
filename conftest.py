from selenium.webdriver import Chrome
from Utility.fileObjects import MyLocator
import pytest
import time

@pytest.fixture(scope="class")
def setup(request):

    exe = MyLocator()

    link = exe.url()

    url = link['url']['corporate'][0]
    path = 'D:\\chromedriver.exe'

    driver = Chrome(executable_path=path)
    driver.get(url)
    driver.maximize_window()
    request.cls.driver = driver

    yield driver
    time.sleep(10)
    driver.close()