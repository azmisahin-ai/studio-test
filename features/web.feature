# features/app.feature
Feature: Home Endpoint Test
  As a user
  I want to test the home endpoint
  So that I can verify the response from the web service

  Scenario: Accessing the home endpoint
    Given the web service is running
    When I access the home endpoint
    Then the response status code should be 200
