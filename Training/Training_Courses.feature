Feature: UI
  # Enter feature description here

  Scenario Outline: I want to check the UI in Training -> Courses
    Given I login as "<Role>"
    When I go to Training Page Tab Courses
    Then I will check the page


    Examples:
      | Role      |
      | Admin     |
      | TM        |
      | Manager   |
      | Employee  |
