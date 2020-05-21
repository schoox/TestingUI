Feature: UI
  # Enter feature description here

  Scenario Outline: I want to check the UI in My Training -> My Curricula
    Given I login as "<Role>"
    When I go to My Training Page Tab My Curricula
    Then I will check the page


    Examples:
      | Role      |
      | Admin     |
      | TM        |
      | Manager   |
      | Employee  |