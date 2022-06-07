# Created by Анна at 6/5/2022
Feature: Amazon cart

  Scenario: User can add an item to the cart
    Given Open Amazon page
    When Search for Blanket
    And Click on the first item
    And Store item name
    And Click Add to cart button
    And Open Cart page
    Then Verify cart has 1 item
    And Verify cart has correct item