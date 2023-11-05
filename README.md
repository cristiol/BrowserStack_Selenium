
---

# Selenium Test Suite for bstackdemo.com

This test suite is designed to automate various test scenarios for the [bstackdemo.com](https://bstackdemo.com/) website using Selenium and Pytest.

## Table of Contents

- [Test Overview](#test-overview)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Running the Tests](#running-the-tests)
- [Test Cases](#test-cases)
- [Contributing](#contributing)
- [License](#license)

## Test Overview

This Selenium test suite automates the following scenarios on the bstackdemo.com website:

1. Sign in with good credentials.
2. Perform a checkout process, including adding items to the cart, filling in billing information, and confirming the order.
3. Verify the copyright notice on the website.
4. Check the availability of product vendors.
5. Add items to the cart.
6. Add items to favorites.
7. Remove items from the cart.
8. Select quantity of items in the cart.

## Getting Started

### Prerequisites

To run the tests in this suite, you'll need the following:

- Python installed on your system.
- Selenium library (`pip install selenium`).
- Pytest (`pip install pytest`).
- Chrome WebDriver (Ensure the WebDriver version matches your Chrome browser version).

### Installation

1. Clone this repository to your local machine.

```shell
git clone <repository-url>
cd <repository-directory>
```

2. Install the required Python packages.

```shell
pip install -r requirements.txt
```

3. Download the Chrome WebDriver and ensure it's in your system's PATH or provide its path in the test scripts.

## Running the Tests

You can run the tests using Pytest. From the project directory, run the following command:

```shell
pytest
```

## Test Cases

Here is a brief overview of the test cases covered in this test suite:

- `test_checkout`: Perform a complete checkout process, including signing in, adding items to the cart, and confirming the order.
- `test_copyright`: Verify the copyright notice on the website's main page.
- `test_browserstack`: Sign in with good credentials and check the user's username.
- `test_vendors`: Sign in and check the availability of product vendors.
- `test_add`: Sign in and add items to the cart.
- `test_favourites`: Sign in, add items to favorites, and verify the favorites page.
- `test_remove_from_cart`: Sign in, add items to the cart, and remove items from the cart.
- `test_quantity_selection`: Sign in, add items to the cart, and select item quantities.

Feel free to modify and expand these test cases as needed.

## Contributing

If you'd like to contribute to this project, please open an issue or submit a pull request with your proposed changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

You can save this README in a file named `README.md` in your project directory, and it will serve as documentation for your Selenium test suite.
 
