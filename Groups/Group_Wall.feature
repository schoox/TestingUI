Feature: UI

  @wall @groups
  Scenario Outline: I want to check the UI in Group Wall Page
    Given I login as "<Role>"
    When I go to Group Wall Page
    Then I will check the page


    Examples:
      | Role          |
      | Admin         |
      | Group Admin   |
      | Group Creator |
      | Group Member  |