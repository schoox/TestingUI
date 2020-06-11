Feature: UI

  @groups @edit_image
  Scenario Outline: I want to check the UI in Group -> Edit Image
    Given I login as "<Role>"
    When I go to Edit Image Page
    Then I will check the page


    Examples:
      | Role          |
      | Admin         |
      | Group Admin   |
      | Group Creator |