@regression
Feature: GET SINGLE USER
  # Enter feature description here

  Scenario: Verify user can fetch single user
    Given the API client is initialized for TC_03 First Scenario
    When I send a Get request to fetch a single user
    Then the response status should be 200 for TC_03 First Scenario
    And the response should match the updated schema for TC_03 First Scenario
    And the response time should be less than 2 seconds for TC_03 First Scenario