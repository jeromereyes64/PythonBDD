import pytest
import requests

@pytest.mark.Smoke
def test_TC02_Login(api_url):
    print(f"Testing API at: {api_url}")
    response = requests.get(f"{api_url}")
    print(response.text)
    assert response.status_code == 200  # Example of asserting a successful response
