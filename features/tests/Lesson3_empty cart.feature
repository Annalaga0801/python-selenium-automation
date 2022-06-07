# Created by Анна at 6/7/2022
Feature: Amazon cart

  Scenario: Verify that Amazon cart is empty
    Given open Amazon page
    When Click on Cart icon
    Then Verify Cart has 0 item(s)