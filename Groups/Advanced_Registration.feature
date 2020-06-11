Feature: UI

  @groups @registration @advanced
  Scenario Outline: I want to check the UI in Group -> Register Members -> Advanced registration
    Given I login as "<Role>"
    When I go to Advanced Registration Page
    Then I will check the page


    Examples:
      | Role          |
      | Admin         |
      | Group Admin   |
      | Group Creator |