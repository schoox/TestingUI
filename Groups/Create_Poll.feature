Feature: UI

  @groups @create_poll @polls
  Scenario Outline: I want to check the UI in Group -> Polls -> Create Poll
    Given I login as "<Role>"
    When I go to Create Poll Page
    Then I will check the page


    Examples:
      | Role          |
      | Admin         |
      | Group Admin   |
      | Group Creator |