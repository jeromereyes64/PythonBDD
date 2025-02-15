from behave import *
from behave import given, when, then
from BDD.utils.api_constants import *
from BDD.utils.url_builder import URLBuilder
from BDD.data.schema.schema import *
from BDD.data import global_store

"""Scenario 1"""
@given("the API client is initialized for TC_03 First Scenario")
def step_initialize_api_client(context):
    """API client is initialized via environment.py, no need to reinitialize."""
    assert context.api_client is not None, "API client was not initialized!"


@when("I send a Get request to fetch a single user")
def step_send_get_request(context):
    """Send a GET request to the health check endpoint"""
    endpoint = URLBuilder.format(Endpoints.USERS, user_id= global_store.first_user_id)
    context.response = context.api_client.get(endpoint)
    print(f"Fetching user details for ID: {global_store.first_user_id}")


@then("the response status should be 200 for TC_03 First Scenario")
def step_validate_update_status(context):
    """Validate that response return code"""
    context.api_client.assert_stat_code(context.response, ResponseCode.OK,"Assertion Failed")


@step("the response should match the updated schema for TC_03 First Scenario")
def step_validate_updated_schema(context):
    """Use APIClient method to validate response schema"""
    context.api_client.assert_schema(context.response, get_single_user_response_schema)


@step("the response time should be less than 2 seconds for TC_03 First Scenario")
def step_validate_response_schema(context):
    """Validate API response time"""
    context.api_client.assert_response_time(context.response)


"""Scenario 2"""
@given("the API client is initialized for TC_03 Second Scenario")
def step_initialize_api_client(context):
    """API client is initialized via environment.py, no need to reinitialize."""
    assert context.api_client is not None, "API client was not initialized!"


@when("I send a Get request to fetch an invalid user")
def step_send_get_request(context):
    """Send a GET request to the health check endpoint"""
    endpoint = URLBuilder.format(Endpoints.USERS, user_id= global_store.invalid_user_id)
    context.response = context.api_client.get(endpoint)
    print(f"Fetching user details for ID: {global_store.invalid_user_id}")


@then("the response status should be 400 for TC_03 Second Scenario")
def step_validate_update_status(context):
    """Validate that response return code"""
    context.api_client.assert_stat_code(context.response, ResponseCode.NOT_FOUND,"Assertion Failed")


@step("the response should match the updated schema for TC_03 Second Scenario")
def step_validate_updated_schema(context):
    """Use APIClient method to validate response schema"""
    context.api_client.assert_schema(context.response, get_invalid_user_response_schema)

@step("the response time should be less than 2 seconds for TC_03 Second Scenario")
def step_impl(context):
    """Validate API response time"""
    context.api_client.assert_response_time(context.response)