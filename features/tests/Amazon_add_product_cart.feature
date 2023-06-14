Feature: Test Scenarios for Amazon cart functionality

  Scenario: Verify number of items in a cart
    Given Goto Amazon page
    When enter the product coffee powder in the search field
    And enter on search icon
    Then choose your product
    Then click add to cart icon
    Then confirm that selected product in the cart