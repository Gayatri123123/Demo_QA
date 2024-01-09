import pytest
from selenium import webdriver
#from pytest_metadata.plugin import metadata_key


#To RUN Particularly on Chrome browser
@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    return driver

'''
@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver=webdriver.Chrome()
        print("lanching chrome browser")
    elif browser=='edge':
        driver=webdriver.Edge()
        print("lanching firefox browser")
    else:
        driver=webdriver.Chrome()
    #driver = webdriver.Edge()
    return driver
def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")
    
'''
