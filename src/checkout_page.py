from src.homepage import Homepage


class CheckOut(Homepage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Define locators for web elements on the checkout page
    locators = {
        "first_name_field": ('ID', 'firstNameInput'),
        "last_name_field": ('ID', 'lastNameInput'),
        "address_field": ('ID', 'addressLine1Input'),
        "state_field": ('ID', 'provinceInput'),
        "postal_code_field": ('ID', 'postCodeInput'),
        "submit_btn": ('ID', 'checkout-shipping-continue'),
        "confirmation_message": ('ID', 'confirmation-message')
    }

    # Set the first name in the first name field
    def select_firs_name(self):
        self.first_name_field.set_text('Dele\n')

    # Set the last name in the last name field
    def select_last_name(self):
        self.last_name_field.set_text('Ali\n')

    # Set the address in the address field
    def select_address(self):
        self.address_field.set_text('London\n')

    # Set the state in the state field
    def select_state(self):
        self.state_field.set_text('England\n')

    # Set the postal code in the postal code field
    def select_postal_code(self):
        self.postal_code_field.set_text('100032216\n')

    # Click the submit button to place the order
    def click_submit(self):
        self.submit_btn.click()

    # Get and assert the confirmation message after placing the order
    def get_confirmation_message(self):
        retrieved_confirmation_message = self.confirmation_message.get_text()
        assert retrieved_confirmation_message == 'Your Order has been successfully placed.'
