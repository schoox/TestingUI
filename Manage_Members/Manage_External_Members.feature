Feature: UI
  # Enter feature description here

  @listing @users_listing @manage_members_listing @external_members
  Scenario Outline: I want to check the UI in Manage Members -> External Members
    Given I login as "<Role>"
    When I go to Manage Members Tab External Members
    Then I will check the page


    Examples:
      | Role      |
      | Admin     |