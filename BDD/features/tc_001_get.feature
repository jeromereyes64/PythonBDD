@regression
Feature: GET User List, User Login and Invalid Endpoint Test

  Scenario: Verify API is reachable
    Given the API client is initialized for TC_01 First Scenario
    When I send a GET request to the health check endpoint
    Then the response status should be 200

  Scenario: Verify user login functionality
    Given the API client is initialized for TC_01 Second Scenario
    When I send a POST request to create a user
    Then the response status should be 201
    And the response schema should be valid

  @smoke
  Scenario: Verify API handles invalid endpoint
    Given the API client is initialized for TC_01 Third Scenario
    When I send a GET request to an invalid endpoint
    Then the response status should be 404