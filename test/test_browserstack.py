from selenium import webdriver
from src.checkout_page import CheckOut
from src.homepage import Homepage
from src.signin_page import SignInPage
import pytest


# Define a Signin class that extends SignInPage
class Signin(SignInPage):
    def __init__(self, driver):
        super().__init__(driver)

    # Method for signing in with good credentials
    def signin_with_good_credentials(self):
        # Navigate to the sign-in page
        self.driver.get('https://bstackdemo.com/signin')
        # Perform the sign-in
        self.sign_in()

# Fixture for managing the driver session
@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

# Test for the checkout process
def test_checkout(driver):

    check = CheckOut(driver)
    homepage = Homepage(driver)

    test = Signin(driver)
    test.signin_with_good_credentials()
    # Add items to the cart and proceed to the checkout process
    homepage.add_to_cart()
    homepage.click_checkout()
    # Fill in billing information
    check.select_firs_name()
    check.select_last_name()
    check.select_address()
    check.select_state()
    check.select_postal_code()
    check.click_submit()
    check.get_confirmation_message()

# Test for checking copyright
def test_copyright(driver):
    # Open the main page
    driver.get('https://bstackdemo.com/')
    # Check the copyright notice
    homepage = Homepage(driver)
    homepage.copyright()

# test for sign in
def test_browserstack(driver):

    test = Signin(driver)
    test.signin_with_good_credentials()

    homepage = Homepage(driver)
    homepage.get_username()

# Test for checking vendors
def test_vendors(driver):

    test = Signin(driver)
    test.signin_with_good_credentials()

    vendor = Homepage(driver)
    vendor.check_vendor()

# Test for adding items to the cart
def test_add(driver):

    test = Signin(driver)
    test.signin_with_good_credentials()

    cart = Homepage(driver)
    cart.click_cart()

# Test for adding items to favorites
def test_favourites(driver):

    test = Signin(driver)
    test.signin_with_good_credentials()

    homepage = Homepage(driver)
    homepage.add_to_favourites()
    homepage.click_favourites_btn()
    homepage.check_favourite_page()

# Test for removing items from the cart
def test_remove_from_cart(driver):

    test = Signin(driver)
    test.signin_with_good_credentials()

    homepage = Homepage(driver)
    homepage.add_to_cart()
    homepage.remove_cart()

# Test for selecting quantity
def test_quantity_selection(driver):

    test = Signin(driver)
    test.signin_with_good_credentials()

    homepage = Homepage(driver)
    homepage.add_to_cart()
    homepage.quantity_selection()




















