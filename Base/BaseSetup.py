from appium import webdriver
from util.Config import Config

class BaseSetup(object):

    def __init__(self,phoneName):
        self.driver = self.getDriver(phoneName)

    def getDriver(self,phoneName):

        self.desireCap = Config.getDesiredCap(phoneName)

        try:
            self.driver = webdriver.Remote(self.desireCap['url'],self.desireCap)
        except Exception as err:
            print("Initializing Driver error")

        return self.driver

    def exitDriver(self):
        self.driver.quit()

if __name__ == '__main__':
    test = BaseSetup('MX6')
