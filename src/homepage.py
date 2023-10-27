from seleniumpagefactory.Pagefactory import PageFactory


class Homepage(PageFactory):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    locators = {
        "sign_in": ("ID", "signin"),
        "user_name": ("CSS", ".username"),
        "apple": ('XPATH', '//*[@id="__next"]/div/div/main/div[1]/div[1]/label/span'),
        "samsung": ('XPATH', '//*[@id="__next"]/div/div/main/div[1]/div[2]/label/span'),
        "google": ('XPATH', '//*[@id="__next"]/div/div/main/div[1]/div[3]/label/span'),
        "oneplus": ('XPATH', '//*[@id="__next"]/div/div/main/div[1]/div[4]/label/span'),
        "add_to_cart_btn": ('XPATH', '//*[@id="1"]/div[4]'),
        "cart": ('XPATH', '//*[@id="__next"]/div/div/div[2]/span/span'),
        "checkout": ('XPATH', '//*[@id="__next"]/div/div/div[2]/div[2]/div[3]/div[3]'),
        "add_favourite_btn": ('XPATH', '//*[@id="1"]/div[1]/button'),
        "favourites_btn": ('ID', 'favourites'),
        "products_found": ('XPATH', '//*[@id="__next"]/div/div/main/div[1]/div[1]/small'),
        "remove_cart_btn": ('class_name', 'shelf-item__del'),
        "empty_card": ('class_name', 'shelf-empty'),
        "remove_quantity": ('XPATH', '//*[@id="__next"]/div/div/div[2]/div[2]/div[2]/div/div[4]/div/button[1]'),
        "add_quantity": ('XPATH', '//*[@id="__next"]/div/div/div[2]/div[2]/div[2]/div/div[4]/div/button[2]'),
        "bag__quantity": ('class_name', 'bag__quantity'),
        "copyright_text": ('XPATH', '//*[@id="__next"]/div/div/footer/div/div/div/span')
    }

    def click_sign_in(self):
        self.sign_in.click()

    def get_username(self):
        retrieved_username = self.user_name.get_text()
        assert retrieved_username == "demouser"

    def check_vendor(self):
        retrieved_apple = self.apple.get_text()
        assert retrieved_apple == 'Apple'

        retrieved_samsung = self.samsung.get_text()
        assert retrieved_samsung == 'Samsung'

        retrieved_google = self.google.get_text()
        assert retrieved_google == 'Google'

        retrieved_oneplus = self.oneplus.get_text()
        assert retrieved_oneplus == 'OnePlus'

    def add_to_cart(self):
        self.add_to_cart_btn.click()

    def click_cart(self):
        self.cart.click()

    def copyright(self):
        copyright_text = self.copyright_text.get_text()
        assert '2023' in copyright_text
        self.driver.quit()

    def remove_cart(self):
        self.remove_cart_btn.click()
        empty_card_message = self.empty_card.get_text()
        assert 'Add some products in the bag' in empty_card_message

    def quantity_selection(self):
        self.add_quantity.click()
        assert self.bag__quantity.get_text() == '2'

        self.remove_quantity.click()
        assert self.bag__quantity.get_text() == '1'

    def click_checkout(self):
        self.checkout.click()

    def add_to_favourites(self):
        self.add_favourite_btn.click()

    def click_favourites_btn(self):
        self.favourites_btn.click()

    def check_favourite_page(self):
        products_found = self.products_found.get_text()
        assert products_found == '1 Product(s) found.'















