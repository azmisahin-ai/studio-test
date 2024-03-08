# features/web.api.v1.time_service.feature
Feature: Time Service API
  As a user of the Time Service API
  I want to be able to retrieve the current time
  So that I can use it in my applications

  Scenario: Retrieve current time
    Given the Time Service API is running
    When I request the current time
    Then the response should contain the current time in string format
