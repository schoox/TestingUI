Feature: UI_User
  # Enter feature description here

  @listing @profile @friend_list
  Scenario Outline: I want to check the UI in Profile -> User Friends
    Given I login as "<Role>"
    When I go to User Friends List
    Then I will check the page


    Examples:
      | Role      |
      | Admin     |