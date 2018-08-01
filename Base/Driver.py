from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Driver():

    def setDriver(self,driver):
        self.driver = driver

    def id(self,id,time):
        locator = (By.ID, id)
        WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator))
        return self.driver.find_element_by_id(id)