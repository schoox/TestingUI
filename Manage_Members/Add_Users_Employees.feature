Feature: UI
  # Enter feature description here

  @add_users
  Scenario Outline: I want to check the UI in Add Users -> Employees
    Given I login as "<Role>"
    When I go to Add Users Tab Employees
    Then I will check the page


    Examples:
      | Role      |
      | Admin     |