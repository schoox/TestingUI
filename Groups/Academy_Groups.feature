Feature: UI
  # Enter feature description here

  @listing @groups
  Scenario Outline: I want to check the UI in Academy Groups Page
    Given I login as "<Role>"
    When I go to Academy Groups Page
    Then I will check the page


    Examples:
      | Role      |
      | Admin     |
      | TM        |
      | Manager   |
      | Employee  |