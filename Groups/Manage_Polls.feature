Feature: UI

  @groups @manage_polls @polls
  Scenario Outline: I want to check the UI in Group -> Polls -> Manage Polls
    Given I login as "<Role>"
    When I go to Manage Polls Page
    Then I will check the page


    Examples:
      | Role          |
      | Admin         |
      | Group Admin   |
      | Group Creator |