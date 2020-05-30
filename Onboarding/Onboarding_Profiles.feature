Feature: UI
  # Enter feature description here

  @listing @onboarding @onboarding_profiles
  Scenario Outline: I want to check the UI in Onboarding -> Onboarding Profiles
    Given I login as "<Role>"
    When I go to Onboarding Profiles
    Then I will check the page


    Examples:
      | Role      |
      | Admin     |