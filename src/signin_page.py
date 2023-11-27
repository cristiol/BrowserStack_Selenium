from seleniumpagefactory.Pagefactory import PageFactory


class SignInPage(PageFactory):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    # Define locators for web elements on the sign-in page
    locators = {
        'user_name': ('CSS', "#username input"),
        'password': ('CSS', '#password input'),
        'login_btn': ('ID', 'login-btn')
    }

    # Set the username in the username field
    def select_username(self):
        self.user_name.set_text('demouser\n')

    # Set the password in the password field
    def select_password(self):
        self.password.set_text('testingisfun99\n')

    # Click the login button to initiate the sign-in process
    def click_login(self):
        self.login_btn.click()

    # Perform the sign-in by calling the individual steps
    def sign_in(self):
        self.select_username()
        self.select_password()
        self.click_login()
