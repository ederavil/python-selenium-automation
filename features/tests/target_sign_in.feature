# Created by Jeimi at 7/6/2024
Feature: Target Sign In

  Scenario: Verify logged out user can sign in
    Given Open Target Main page
    When Click on Sign in
    And Click on Sign in from side menu
    Then Verify sign in form opens


  Scenario: User can open and close Terms and Conditions from sign in page
    Given Open Target Main page
    When Click on Sign in
    And Click on Sign in from side menu
    And Store original window
    And Click Terms and Conditions link
    And Switch to new window
    Then Verify Terms and Conditions page opened
    And Close current page
    And Return to original window