Feature: UI

  @groups @invitations @advanced
  Scenario Outline: I want to check the UI in Group -> Send Invitations -> Advanced Invite
    Given I login as "<Role>"
    When I go to Advanced Invite Page
    Then I will check the page


    Examples:
      | Role          |
      | Admin         |
      | Group Admin   |
      | Group Creator |