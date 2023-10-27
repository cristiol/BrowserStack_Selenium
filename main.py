# from selenium import webdriver
# from src.checkout_page import CheckOut
# from src.homepage import Homepage
# from src.signin_page import SignInPage
# import pytest
#
#
# class Signin(SignInPage):
#     def __init__(self, driver):
#         super().__init__(driver)
#
#     def signin_with_good_credentials(self):
#         self.driver.get('https://bstackdemo.com/signin')
#         self.sign_in()
#
#
#     def test_browserstack(self):
#         driver = webdriver.Chrome()
#         test = Signin(driver)
#         test.signin_with_good_credentials()
#
#         homepage = Homepage(driver)
#         homepage.get_username()
#
#
#     def test_vendors(self):
#         driver = webdriver.Chrome()
#         test = Signin(driver)
#         test.signin_with_good_credentials()
#
#         vendor = Homepage(driver)
#         vendor.check_vendor()
#
#
#     def test_add(self):
#         driver = webdriver.Chrome()
#         test = Signin(driver)
#         test.signin_with_good_credentials()
#
#         cart = Homepage(driver)
#         cart.click_cart()
#
#
#     def test_favourites(self):
#         driver = webdriver.Chrome()
#         test = Signin(driver)
#         test.signin_with_good_credentials()
#
#         homepage = Homepage(driver)
#         homepage.add_to_favourites()
#         homepage.click_favourites_btn()
#         homepage.check_favourite_page()
#
#
#     def test_remove_from_cart(self):
#         driver = webdriver.Chrome()
#         test = Signin(driver)
#         test.signin_with_good_credentials()
#
#         homepage = Homepage(driver)
#         homepage.add_to_cart()
#         homepage.remove_cart()
#
#
#     def test_quantity_selection(self):
#         driver = webdriver.Chrome()
#         test = Signin(driver)
#         test.signin_with_good_credentials()
#
#         homepage = Homepage(driver)
#         homepage.add_to_cart()
#         homepage.quantity_selection()
#
#
#     def test_copyright(self):
#         driver = webdriver.Chrome()
#         driver.get('https://bstackdemo.com/')
#
#         homepage = Homepage(driver)
#         homepage.copyright()
#
#
#     def test_checkout(self):
#         driver = webdriver.Chrome()
#         check = CheckOut(driver)
#         homepage = Homepage(driver)
#
#         test = Signin(driver)
#         test.signin_with_good_credentials()
#
#         homepage.add_to_cart()
#         homepage.click_checkout()
#
#         check.select_firs_name()
#         check.select_last_name()
#         check.select_address()
#         check.select_state()
#         check.select_postal_code()
#         check.click_submit()
#         check.get_confirmation_message()







