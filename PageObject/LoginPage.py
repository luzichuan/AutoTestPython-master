from Base.BaseSetup import BaseSetup

class LoginPage(BaseSetup):

    loginButton = "com.yoosee:id/btn_login"
    passWordTextField = "com.yoosee:id/et_pwd"
    userNameTextField = "com.yoosee:id/et_account"

    def __init__(self,phoneName):
        super(LoginPage,self).__init__(phoneName)

    def setUserName(self,username):
        userNameElement = self.driver.find_element_by_id(self.userNameTextField)
        userNameElement.clear()
        userNameElement.send_keys(username)

    def setPassword(self,password):
        passWordElement = self.driver.find_element_by_id(self.passWordTextField)
        passWordElement.clear()
        passWordElement.send_keys(password)

login_page = LoginPage("MX6")
login_page.setUserName("just for test")
login_page.exitDriver()

