Feature: UI
  # Enter feature description here

  @listing @my_events_listing @my_training_listing
  Scenario Outline: I want to check the UI in My Training -> My Events
    Given I login as "<Role>"
    When I go to My Training Page Tab My Events
    Then I will check the page


    Examples:
      | Role      |
      | Admin     |
      | TM        |
      | Manager   |
      | Employee  |