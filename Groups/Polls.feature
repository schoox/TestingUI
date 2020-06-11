Feature: UI

  @groups @polls
  Scenario Outline: I want to check the UI in Group -> Polls
    Given I login as "<Role>"
    When I go to Polls Page
    Then I will check the page


    Examples:
      | Role          |
      | Group Member  |
