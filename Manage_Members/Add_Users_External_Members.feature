Feature: UI
  # Enter feature description here

  @add_users @external_members
  Scenario Outline: I want to check the UI in Add Users -> External Members
    Given I login as "<Role>"
    When I go to Add Users Tab External Members
    Then I will check the page


    Examples:
      | Role      |
      | Admin     |