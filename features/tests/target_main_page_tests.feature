# Created by Jeimi at 7/5/2024
Feature: Target Main Page Tests
  # Enter feature description here

  Scenario: User verify empty cart on main page
    Given Open Target page
    When Click on cart icon
    Then Verify empty cart message shown is shown

