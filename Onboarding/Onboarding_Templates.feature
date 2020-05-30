Feature: UI
  # Enter feature description here

  @listing @onboarding @onboarding_templates
  Scenario Outline: I want to check the UI in Onboarding -> Onboarding Templates
    Given I login as "<Role>"
    When I go to Onboarding Templates
    Then I will check the page


    Examples:
      | Role      |
      | Admin     |