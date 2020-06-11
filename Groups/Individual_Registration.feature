Feature: UI

  @groups @registration @individual
  Scenario Outline: I want to check the UI in Group -> Register Members -> Individual registration
    Given I login as "<Role>"
    When I go to Individual Registration Page
    Then I will check the page


    Examples:
      | Role          |
      | Admin         |
      | Group Admin   |
      | Group Creator |