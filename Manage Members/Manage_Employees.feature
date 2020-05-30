Feature: UI
  # Enter feature description here

  @listing @users_listing @manage_members_listing
  Scenario Outline: I want to check the UI in Manage Members -> Employees
    Given I login as "<Role>"
    When I go to Manage Members Tab Employees
    Then I will check the page


    Examples:
      | Role      |
      | Admin     |