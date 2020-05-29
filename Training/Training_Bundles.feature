Feature: UI
  # Enter feature description here

  @listing @bundles_listing @training_listing
  Scenario Outline: I want to check the UI in Training -> Bundles
    Given I login as "<Role>"
    When I go to Training Page Tab Bundles
    Then I will check the page


    Examples:
      | Role      |
      | Admin     |

