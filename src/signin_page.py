from seleniumpagefactory.Pagefactory import PageFactory


class SignInPage(PageFactory):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    locators = {
        'user_name': ('CSS', "#username input"),
        'password': ('CSS', '#password input'),
        'login_btn': ('ID', 'login-btn')
    }

    def select_username(self):
        self.user_name.set_text('demouser\n')

    def select_password(self):
        self.password.set_text('testingisfun99\n')

    def click_login(self):
        self.login_btn.click()

    def sign_in(self):
        self.select_username()
        self.select_password()
        self.click_login()
