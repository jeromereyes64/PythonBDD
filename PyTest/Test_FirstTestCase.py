import pytest

@pytest.fixture()
def fixture_code():
    print("execute this first")
    yield
    print("Will execute after")

@pytest.mark.Sanity
def test_TC01_Login(fixture_code):
    print('first test case to run')
    c = 1000
    assert c == 1000

@pytest.mark.Smoke
def test_TC03_Login(fixture_code):
    print('third test case to run')