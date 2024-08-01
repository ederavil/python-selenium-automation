# Created by Jeimi at 7/31/2024
Feature: Target Product Page Tests

  Scenario: Verify colors for T-shirt
    Given Open product page for A-91270565
    Then Verify the colors can be chosen


  Scenario: Verify search product features
    Given Open Target Main Page
    When Search for cups
    Then Verify product image displays for each
    Then Verify product name displays for each