'''
Basic Tests for Alfresco, using selenium.
'''

from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

class BasicSeleniumTest():
    '''
    Class for Basic tests for Alfresco with Selenium.
    '''

    def __init__(self):
        '''
        Initiation of selenium
        '''
        options = Options()
        options.add_argument("--headless")
        self.driver = webdriver.Firefox(options=options)



    def test_get(self):
        '''
        Checking if the /share/ URL is available.
        Should return code 200.
        '''
        self.driver.set_page_load_timeout(30)
        self.driver.get("https://localhost/share")
        assert "Alfresco" in self.driver.title

    def close(self):
        '''
        Close firefox when done.
        '''
        self.driver.close()



if __name__ == '__main__':
    bot = BasicSeleniumTest()
    bot.test_get()
    bot.close()
