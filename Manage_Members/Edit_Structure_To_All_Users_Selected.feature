Feature: UI
  # Enter feature description here

  @manage_members_listing @structure
  Scenario Outline: I want to check the UI in Manage Members -> Employees
    Given I login as "<Role>"
    When I go to Manage Members Tab Employees
    And I select all users to Add structure
    Then I will check the page
    When I cancel the Add structure
    And I select all users to Remove structure
    Then I will check the page


    Examples:
      | Role      |
      | Admin     |