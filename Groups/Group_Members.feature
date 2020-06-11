Feature: UI

  @groups @group_members
  Scenario Outline: I want to check the UI in Group -> Group Members
    Given I login as "<Role>"
    When I go to Group Members Page
    Then I will check the page


    Examples:
      | Role          |
      | Admin         |
      | Group Admin   |
      | Group Creator |
      | Group Member  |