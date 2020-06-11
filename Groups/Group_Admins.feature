Feature: UI

  @groups @group_admins
  Scenario Outline: I want to check the UI in Group -> Admins
    Given I login as "<Role>"
    When I go to Group Admins Page
    Then I will check the page


    Examples:
      | Role          |
      | Admin         |
      | Group Admin   |
      | Group Creator |
      | Group Member  |