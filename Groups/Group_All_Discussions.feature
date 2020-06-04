Feature: UI

  @listing @groups @group_discussions @discussions
  Scenario Outline: I want to check the UI in Group -> All Discussions
    Given I login as "<Role>"
    When I go to Group All Discussions Page
    Then I will check the page


    Examples:
      | Role          |
      | Admin         |
      | Group Admin   |
      | Group Creator |
      | Group Member  |