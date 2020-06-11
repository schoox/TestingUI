Feature: UI

  @groups @group_content @content
  Scenario Outline: I want to check the UI in Group -> Content
    Given I login as "<Role>"
    When I go to Group Content Page
    Then I will check the page


    Examples:
      | Role          |
      | Admin         |
      | Group Admin   |
      | Group Creator |
      | Group Member  |