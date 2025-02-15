from behave import given, when, then
from BDD.utils.api_constants import *
from BDD.utils.url_builder import URLBuilder
from BDD.data.schema.schema import create_response_schema
from BDD.data.payload.postdata import *
from BDD.data import global_store

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
    # Extract JSON response
    response_data = context.response.json()

    # Fetch the first ID from the "data" array
    if "data" in response_data and response_data["data"]:
        global_store.first_user_id = response_data["data"][0]["id"]
        print(f"Extracted Test Data First User ID: {global_store.first_user_id}")
    else:
        global_store.first_user_id = None
        print("No user data found in response")

@then("the response status should be 200")
def step_validate_response_status(context):
    """Validate that response return code"""
    context.api_client.assert_stat_code(context.response, ResponseCode.OK,"Assertion Failed")



"""2nd Scenario"""
@given("the API client is initialized for TC_01 Second Scenario")
def step_initialize_api_client(context):
    """Ensure API client is initialized"""
    assert context.api_client is not None, "API client was not initialized!"


@when("I send a POST request to create a user")
def step_create_user(context):
    """Send a POST request to create a new user"""

    context.response = context.api_client.post(Endpoints.USERS, create_user_payload)
    print(f"Request URL: {context.api_client.base_url}{Endpoints.USERS}")
    print(f"Response: {context.response.text}")


@then("the response status should be 201")
def step_validate_create_status(context):
    """Verify user creation status code"""
    context.api_client.assert_stat_code(context.response, ResponseCode.CREATED,"Assertion Failed")


@then("the response schema should be valid")
def step_validate_schema(context):
    """Use APIClient method to validate response schema"""
    #response_data = context.response.json()
    context.api_client.assert_schema(context.response, create_response_schema)


"""3rd Scenario"""
@given("the API client is initialized for TC_01 Third Scenario")
def step_initialize_api_client(context):
    """Ensure API client is initialized"""
    assert context.api_client is not None, "API client was not initialized!"


@when("I send a GET request to an invalid endpoint")
def step_invalid_endpoint(context):
    """Send a GET request to a non-existing endpoint"""
    context.response = context.api_client.get(Endpoints.INVALID)
    print(f"Invalid endpoint test: {context.api_client.base_url}{Endpoints.INVALID}")


@then("the response status should be 404")
def step_validate_404_status(context):
    """Validate that an invalid endpoint returns 404"""
    context.api_client.assert_stat_code(context.response, ResponseCode.NOT_FOUND,"Assertion Failed")