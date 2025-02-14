@regression
Feature: Update User Endpoint

  @smoke
  Scenario: Verify user can be updated successfully
    Given the API client is initialized for TC_02 First Scenario
    When I send a PUT request to update a user
    Then the response status should be 200 for TC_02 First Scenario
    And the response data should be updated with the correct name
    And the response should match the updated schema
