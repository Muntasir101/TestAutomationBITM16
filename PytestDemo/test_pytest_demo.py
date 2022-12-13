import pytest


@pytest.fixture()
def browser_config():
    print("Browser launch Successfully")

    yield
    print("Test Done.Browser Closed.")


@pytest.mark.order(3)
def test_login_valid_testCase01():
    print("Login test case 01 Executed")


@pytest.mark.order(1)
def test_login_invalid_testCase02():
    print("Login test case 02 Executed")


@pytest.mark.order(2)
def test_login_invalid_testCase03():
    print("Login test case 03 Executed")


