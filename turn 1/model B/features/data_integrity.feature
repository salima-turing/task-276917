Feature: Verify data integrity check

  Scenario: Verify data integrity check
    Given a financial model with transactions
    When I check the data integrity
    Then the data integrity check should pass
