# Created by Jeimi at 7/6/2024
Feature: Target Sign In

  Scenario: Verify logged out user can sign in
    Given Open Target page
    When Click on Sign in
    And Click on Sign in from side menu
    Then Verify sign in form opens