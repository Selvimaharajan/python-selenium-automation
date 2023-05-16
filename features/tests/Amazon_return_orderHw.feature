Feature: Test Scenarios for Signin functionality

  Scenario: Verify that logged out user sees Sign In when clicking on Returns and Orders
    Given Open Amazon page
    When Click on Return and order icon
    Then Signin page is open
    And Signin header is visible
    And email field is exist