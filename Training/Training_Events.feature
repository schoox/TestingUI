Feature: UI
  # Enter feature description here

  @listing @events_listing @training_listing
  Scenario Outline: I want to check the UI in Training -> Events
    Given I login as "<Role>"
    When I go to Training Page Tab Events
    Then I will check the page


    Examples:
      | Role      |
      | Admin     |
      | TM        |
      | Manager   |
      | Employee  |
