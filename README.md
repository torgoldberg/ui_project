# ui_project

Test UI in Python for rakuten.tv

## Table of Contents

- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)

## Description

This project uses the following tools and libraries to facilitate UI testing:

- **Unittest**: Unittest is a built-in Python testing framework that simplifies writing and running tests for your Python code.

- **Selenium**: Selenium is a popular web testing framework that enables browser automation for testing web applications.


## Installation

To install all project dependencies, navigate to the root project path and execute the following command:
```shell
pip install -r requirements.txt
```

## Usage

in the root path run the next command to run all tests from test_main:
```
python -m unittest
```

in the root path run the next command to run specific test from the test_main:
```
python -m unittest -k MyTestCase
```
