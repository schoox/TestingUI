Feature: UI
  # Enter feature description here

  @listing @my_courses_listing @my_training_listing
  Scenario Outline: I want to check the UI in My Training -> My Courses
    Given I login as "<Role>"
    When I go to Content Page
    Then I will check the page


    Examples:
      | Role      |
      | TM        |
      | CM        |