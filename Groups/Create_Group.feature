Feature: UI
  # Enter feature description here

  @create_group
  Scenario Outline: I want to check the UI in Groups -> Create New Group Page
    Given I login as "<Role>"
    When I go to Create New Group Page
    Then I will check the page


    Examples:
      | Role      |
      | Admin     |
      | TM        |
      | Manager   |