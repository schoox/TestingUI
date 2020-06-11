Feature: UI

  @groups @invitations @individual
  Scenario Outline: I want to check the UI in Group -> Send Invitations -> Individual Invite
    Given I login as "<Role>"
    When I go to Individual Invite Page
    Then I will check the page


    Examples:
      | Role          |
      | Admin         |
      | Group Admin   |
      | Group Creator |