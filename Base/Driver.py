class Driver():

    def setDriver(self,driver):
        self.driver = driver

    def id(self,id):
        return self.driver.find_element_by_id(id)