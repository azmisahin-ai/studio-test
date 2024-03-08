# features/package.feature
Feature: Trace Manager

  Scenario Outline: Should run in debug mode
    Given a Tracking instance is initialized
    When <method> method is called with <message> message
    Then it should write <display> message in console

    Examples:
      | method | message | display |
      | debug  | example | example |
      | info   | example | example |
      | warn   | example | example |
      | error  | example | example |
