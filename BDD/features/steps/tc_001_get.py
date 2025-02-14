from behave import given, when, then
from BDD.utils.endpoints import Endpoints
from BDD.utils.url_builder import URLBuilder
from BDD.utils.schema_validator import validate_response_schema
from BDD.data.schema.schema import create_response_schema
from BDD.data.payload.postdata import *

"""Scenario: Verify API is reachable"""
@given("the API client is initialized for TC_01 First Scenario")
def step_initialize_api_client(context):
    """API client is initialized via environment.py, no need to reinitialize."""
    assert context.api_client is not None, "API client was not initialized!"

@when("I send a GET request to the health check endpoint")
def step_send_health_check_request(context):
    """Send a GET request to the health check endpoint"""
    endpoint = URLBuilder.format(Endpoints.HEALTH_CHECK, page=2)
    context.response = context.api_client.get(endpoint)

@then("the response status should be 200")
def step_validate_response_status(context):
    """Validate that the API returns a 200 status"""
    assert context.response.status_code == 200, f"❌ API health check failed! Status: {context.response.status_code}"



"""2nd Scenario"""
@given("the API client is initialized for TC_01 Second Scenario")
def step_initialize_api_client(context):
    """Ensure API client is initialized"""
    assert context.api_client is not None, "API client was not initialized!"


@when("I send a POST request to create a user")
def step_create_user(context):
    """Send a POST request to create a new user"""

    context.response = context.api_client.post(Endpoints.USERS, create_user_payload)
    print(f"📨 Request URL: {context.api_client.base_url}{Endpoints.USERS}")
    print(f"📄 Response: {context.response.text}")


@then("the response status should be 201")
def step_validate_create_status(context):
    """Verify user creation status code"""
    assert context.response.status_code == 201, "❌ User creation failed!"


@then("the response schema should be valid")
def step_validate_schema(context):
    """Validate response schema"""
    response_data = context.response.json()
    validation_result = validate_response_schema(response_data, create_response_schema)
    assert validation_result is True, validation_result  # Assert schema validation



"""3rd Scenario"""
@given("the API client is initialized for TC_01 Third Scenario")
def step_initialize_api_client(context):
    """Ensure API client is initialized"""
    assert context.api_client is not None, "API client was not initialized!"


@when("I send a GET request to an invalid endpoint")
def step_invalid_endpoint(context):
    """Send a GET request to a non-existing endpoint"""
    context.response = context.api_client.get(Endpoints.INVALID)
    print(f"📢 Invalid endpoint test: {context.api_client.base_url}{Endpoints.INVALID}")


@then("the response status should be 404")
def step_validate_404_status(context):
    """Validate that an invalid endpoint returns 404"""
    assert context.response.status_code == 404, "❌ Invalid endpoint did not return 404!"