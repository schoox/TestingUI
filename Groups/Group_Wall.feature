Feature: UI_Group
  # Enter feature description here

  @listing @groups
  Scenario Outline: I want to check the UI in Group Wall Page
    Given I login as "<Role>"
    When I go to Group Wall Page
    Then I will check the page


    Examples:
      | Role      |
      | Admin     |
      | TM        |
      | Manager   |
      | Employee  |