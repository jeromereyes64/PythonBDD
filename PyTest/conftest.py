import pytest

# Register the --env argument
def pytest_addoption(parser):
    parser.addoption(
        "--env", action="store", default="qa", help="Set the environment (qa or uat)"
    )

# Fixture to provide the API base URL based on the environment
@pytest.fixture(scope="session")
def api_url(pytestconfig):
    env = pytestconfig.getoption("env")
    if env == "qa":
        return "https://api.qa.example.com"
    elif env == "uat":
        return "https://api.uat.example.com"
    else:
        pytest.exit("Invalid environment! Use --env=qa or --env=uat")