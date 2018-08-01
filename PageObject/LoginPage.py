from selenium.webdriver.common.by import By
from Base.BaseSetup import BaseSetup

class LoginPage(BaseSetup):

    loginButton = "com.yoosee:id/btn_login"
    passWordTextField = "com.yoosee:id/et_pwd"
    userNameTextField = "com.yoosee:id/et_account"

    def __init__(self,phoneName):
        super(LoginPage,self).__init__(phoneName)

    def setUserName(self,username):
        self.driver.implicitly_wait(15)
        name = self.driver.find_element_by_id(self.userNameTextField)
        name.clear()
        name.send_keys(username)

login_page = LoginPage("MX6")
login_page.setUserName("just for test")
login_page.exitDriver()

