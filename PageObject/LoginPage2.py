from Base.BaseSetup import BaseSetup
from Base.Driver import Driver

class LoginPage(BaseSetup,Driver):

    loginButton = "com.yoosee:id/btn_login"
    passWordTextField = "com.yoosee:id/et_pwd"
    userNameTextField = "com.yoosee:id/et_account"

    def __init__(self,phoneName):
        super(LoginPage,self).__init__(phoneName)
        self.setDriver(self.driver)

    def setUserName(self,username):
        self.driver.implicitly_wait(15)
        userNameElement = self.id(self.userNameTextField)
        userNameElement.clear()
        userNameElement.send_keys(username)

    def setPassword(self,password):
        passWordElement = self.id(self.passWordTextField)
        passWordElement.clear()
        passWordElement.send_keys(password)

login_page = LoginPage("MX6")
login_page.setUserName("just for test")
login_page.exitDriver()

