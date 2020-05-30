# Created by panos at 14-May-20
Feature: UI
  # Enter feature description here

  @listing @curricula_listing @training_listing
  Scenario Outline: I want to check the UI in Training -> Curricula
    Given I login as "<Role>"
    When I go to Training Page Tab Curricula
    Then I will check the page


    Examples:
      | Role      |
      | Admin     |
      | TM        |
      | Manager   |
      | Employee  |
