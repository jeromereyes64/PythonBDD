import json
from behave import given, when, then
from BDD.utils.endpoints import Endpoints
from BDD.utils.url_builder import URLBuilder
from BDD.utils.schema_validator import validate_response_schema
from BDD.data.schema.schema import *
from BDD.data.payload.postdata import *

@given("the API client is initialized for TC_02 First Scenario")
def step_initialize_api_client(context):
    """API client is initialized via environment.py, no need to reinitialize."""
    pass  # You can leave this empty or remove it completely if it's redundant.

@when("I send a PUT request to update a user")
def step_send_put_request(context):
    """Send a PUT request to update a user"""
    # Format the endpoint with the user ID (Assuming user ID 2 in this case)
    endpoint = URLBuilder.format(Endpoints.UPDATE_USER, user_id=2)

    # Send the PUT request
    context.response = context.api_client.put(endpoint, update_user_payload)

@then("the response status should be 200 for TC_02 First Scenario")
def step_validate_update_status(context):
    """Validate that the user was updated successfully"""
    assert context.response.status_code == 200, "❌ Update Failed!"
    print(f"✅ Response status code: {context.response.status_code}")


@then("the response data should be updated with the correct name")
def step_validate_updated_data(context):
    """Validate the updated data in the response"""
    response_data = context.response.json()
    assert response_data["name"] == "neo", f"❌ Expected name 'neo', but got {response_data['name']}"


@then("the response should match the updated schema")
def step_validate_updated_schema(context):
    """Validate the response schema against the expected schema"""
    response_data = context.response.json()
    validation_result = validate_response_schema(response_data, updated_response_schema)

    assert validation_result is True, f"❌ Schema validation failed: {validation_result}"
    print("✅ Schema validation passed!")