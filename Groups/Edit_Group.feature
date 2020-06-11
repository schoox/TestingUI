Feature: UI

  @groups @edit_group
  Scenario Outline: I want to check the UI in Group -> Edit Group
    Given I login as "<Role>"
    When I go to Edit Group Page
    Then I will check the page


    Examples:
      | Role          |
      | Admin         |
      | Group Admin   |
      | Group Creator |