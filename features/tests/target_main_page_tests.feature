# Created by Jeimi at 7/5/2024
Feature: Target Main Page Tests
  # Enter feature description here

  Scenario: User verify empty cart on main page
    Given Open Target Main page
    When Click on cart icon
    Then Verify empty cart message shown is shown


  Scenario: User search for chips on main page
    Given Open Target Main page
    When Search for chips
    Then Verify search results show chips
    Then Verify intended URL is shown with chips within


  Scenario: User add chips to cart
    Given Open Target Main page
    When Search for chips
    Then Add Doritos cool ranch to cart
    And Verify Doritos cool ranch is in cart


  Scenario: User opens Target circle page
    Given Open Target Main page
    When Click on Target circle icon from top of page
    Then Verify Target circle page is opened
    And Verify there is 10 links on page

